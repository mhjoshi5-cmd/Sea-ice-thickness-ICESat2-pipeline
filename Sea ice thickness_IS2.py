import os
import argparse
import glob
import logging
import h5py
import numpy as np
import pandas as pd
from typing import Tuple, List

# Configure structured logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SeaIceThicknessPipeline:
    """A production-grade ETL pipeline to process ICESat-2 satellite data 
    and calculate sea ice thickness metrics."""
    
    def __init__(self, c_const: float = -1.0, d_const: float = 0.87):
        # Constants for Eastern Weddell Sea
        self.c = c_const
        self.d = d_const
        self.RHO_ICE = 915.1    # kg/m^3
        self.RHO_WATER = 1023.9  # kg/m^3
        self.RHO_SNOW = 300.0   # kg/m^3
        self.FILL_VALUE = 3.40282e+38

    def calculate_thickness(self, freeboard: np.ndarray) -> np.ndarray:
        """Applies empirical equations to derive ice thickness from freeboard metrics."""
        # Handle fill/invalid values safely
        freeboard_clean = np.where(freeboard >= self.FILL_VALUE, np.nan, freeboard)
        
        # Calculate empirical snow depth (converted to meters)
        snow_depth_cm = self.c + (self.d * (freeboard_clean * 100.0))
        snow_depth_m = snow_depth_cm * 0.01
        
        # Apply hydrostatic balance equation
        numerator = (self.RHO_WATER * freeboard_clean) - ((self.RHO_WATER - self.RHO_SNOW) * snow_depth_m)
        denominator = self.RHO_WATER - self.RHO_ICE
        
        return numerator / denominator

    def process_single_file(self, file_path: str, output_dir: str) -> float:
        """Extracts HDF5 beams, computes thickness statistics, and outputs structured CSV data."""
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        
        with h5py.File(file_path, 'r') as fi:
            # Query HDF5 using absolute beam telemetry nodes (Version 6 specification)
            fb_handle = fi.get('/gt3r/freeboard_segment/beam_fb_height')
            lat_handle = fi.get('/gt3r/freeboard_segment/latitude')
            lon_handle = fi.get('/gt3r/freeboard_segment/longitude')
            len_handle = fi.get('/gt3r/freeboard_segment/heights/height_segment_length_seg')
            
            if not fb_handle:
                logging.warning(f"Required datasets missing in beam telemetry: {base_name}")
                return np.nan

            # Convert to high-precision float64 numpy structures
            fr_arr = np.asarray(fb_handle[:], dtype=np.float64)
            lat_arr = np.asarray(lat_handle[:], dtype=np.float64)
            lon_arr = np.asarray(lon_handle[:], dtype=np.float64)
            l1_arr = np.asarray(len_handle[:], dtype=np.float64)

        if fr_arr.size == 0:
            logging.info(f"Skipping empty telemetry array: {base_name}")
            return np.nan

        # Process thickness calculations through the physics engine
        thickness_arr = self.calculate_thickness(fr_arr)
        
        # Structure payload into a flat dataframe matrix
        df = pd.DataFrame({
            'latitude': lat_arr,
            'longitude': lon_arr,
            'freeboard': fr_arr,
            'segment_length': l1_arr,
            'thickness': thickness_arr
        })
        
        # Export processed matrices safely to disk
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{base_name}_processed.csv")
        df.to_csv(output_file, index=False)
        
        return float(np.nansum(l1_arr) / len(l1_arr))

    def run_pipeline(self, input_pattern: str, output_dir: str) -> List[float]:
        """Executes full directory scanning batch operations with automated error safety nets."""
        target_files = glob.glob(input_pattern, recursive=True)
        logging.info(f"Discovered {len(target_files)} HDF5 source matrices for pipeline execution.")
        
        segment_lengths = []
        for file_path in target_files:
            try:
                mean_length = self.process_single_file(file_path, output_dir)
                if not np.isnan(mean_length):
                    segment_lengths.append(mean_length)
                logging.info(f"Successfully serialized telemetry: {os.path.basename(file_path)}")
            except Exception as e:
                logging.error(f"Execution fault encountered on {os.path.basename(file_path)}: {str(e)}", exc_info=True)
                
        return segment_lengths



if __name__ == "__main__":
    # 1. Initialize the argument parser
    parser = argparse.ArgumentParser(
        description="Production ETL pipeline for processing ICESat-2 satellite data."
    )
    
    # 2. Define the expected terminal inputs with default fallback values
    parser.add_argument(
        '--input', 
        type=str, 
        default="./data/raw/**/*.h5", 
        help="Glob pattern path for the input raw HDF5 satellite files."
    )
    parser.add_argument(
        '--output', 
        type=str, 
        default="./data/processed/", 
        help="Directory path where the processed CSV data matrices will be saved."
    )
    
    # 3. Parse the arguments passed from the terminal
    args = parser.parse_args()
    
    # 4. Execute the pipeline using the dynamic inputs
    pipeline = SeaIceThicknessPipeline()
    mean_segments = pipeline.run_pipeline(args.input, args.output)
    
    if mean_segments:
        logging.info(f"Global Pipeline Mean Segment Length: {np.mean(mean_segments):.4f} meters.")

    # Example local configurations
    #
    INPUT_GLOB = "E:/Sea ice/IS2 raw data/2022/east/oct/*.h5"
    OUTPUT_DIRECTORY = "E:/Sea ice/IS2 raw data/2022/east/oct/processed_new/"
    
    pipeline = SeaIceThicknessPipeline()
    mean_segments = pipeline.run_pipeline(INPUT_GLOB, OUTPUT_DIRECTORY)
    
    if mean_segments:
        logging.info(f"Global Pipeline Mean Segment Length: {np.mean(mean_segments):.4f} meters.")

    
    pipeline = SeaIceThicknessPipeline()
    mean_segments = pipeline.run_pipeline(INPUT_GLOB, OUTPUT_DIRECTORY)
    
    if mean_segments:
        logging.info(f"Global Pipeline Mean Segment Length: {np.mean(mean_segments):.4f} meters.")
