# Sea-ice-thickness-ICESat2-pipeline
Python pipeline to process ICESat-2 satellite data and estimate sea ice thickness using Improved Buoyancy equation.
# Sea Ice Thickness Processing Pipeline

## Overview

This project implements a Python-based geospatial data pipeline to process ICESat-2 satellite observations and estimate sea ice thickness using hydrostatic balance equations. These estimations were compared with ship based EM data and snowbuoy data from 2019-2024. The field comparisons were performed using ArcGIS Pro.
This pipeline demonstrates only ICESat-2 ATL10 data. 

The workflow integrates satellite remote sensing data, geophysical modeling, and automated batch processing to generate analysis-ready environmental datasets.

---

## Objectives

- Process ICESat-2 ATL10 HDF5 datasets
- Extract freeboard, latitude, longitude, and segment metadata
- Estimate sea ice thickness using Improved Buoyancy equation i.e. using empirical equation to estimate snow depth. 
- Automate batch processing for large-scale satellite datasets
- Export structured CSV outputs for further geospatial analysis

---

## Data Sources

- ICESat-2 (ATL10 Freeboard Products)
- For each ATL10 file, the following variables are extracted:
  1. Freeboard height
  2. Along-track distance
  3. Latitude
  4. Longitude
  5. Height-segment length
  

---

## Methodology

1. Load HDF5 satellite datasets
2. Extract geophysical variables
3. Clean invalid observations
4. Sea ice thickness is calculated using the buoyancy principle by assuming that water, ice, and snow are in isostatic equilibrium:
   - Freeboard → Snow depth (empirical parameters) → Ice thickness
5. Aggregate and export results into csv

---

## Technologies

- Python
- NumPy
- Pandas
- h5py
- Geo-spatial data processing
- Satellite remote sensing workflows

---

## Key Features

- Automated batch processing of HDF5 files
- Robust error handling and logging
- Scalable pipeline for large datasets
- Physics-based sea ice thickness estimation

---

## Example Output
- Sea ice thickness maps
- Processing workflow diagram
- Sample CSV output

## Related publication:

Joshi, M., Mestas-Nuñez, A. M., Ackley, S. F., Arndt, S., Macdonald, G. J., & Haas, C. (2024).
Seasonal and Interannual Variations in Sea Ice Thickness in the Weddell Sea, Antarctica (2019–2022)
Using ICESat-2. Remote Sensing, 16(20), 3909.

If you use this code, please cite:

Joshi, M. (2026). Sea Ice Thickness Processing Pipeline (Version 1.0).
GitHub: [https://github.com/mhjoshi5-cmd/ICESat-2-Lidar-Processing-Pipeline_
/Sea ice thickness_IS2.py](https://github.com/mhjoshi5-cmd/ICESat-2-Lidar-Processing-Pipeline_/blob/main/Sea%20ice%20thickness_IS2.py)

## Author

Mansi Joshi, PhD  
Geospatial Data Scientist | Remote Sensing | GIS | Python
