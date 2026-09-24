# Sea ice thickness ICESat-2 pipeline
Python pipeline to process ICESat-2 satellite data and estimate sea ice thickness using Improved Buoyancy equation.


## Overview

This project implements a Python-based geospatial data pipeline to process ICESat-2 satellite observations and estimate sea ice thickness using hydrostatic balance equations. These estimations were compared with ship based EM data and snowbuoy data from 2019-2024. 
#### Field comparisons were conducted using the buffer analysis tool in ArcGIS Pro and a minimum-distance criterion to select IS2 data points closest to the field measurements for comparative analysis.
  - Field Data used for snow depth and sea ice thickness are from 2019,2021 and 2022. A GPS-equipped Magna Probe with a horizontal resolution of 1–2 m was used to measure snow depth. The total sea ice thickness was measured using ground-based multi-frequency electromagnetic induction measurements. More details can be found in the publication mentioned below as well as following links: a. https://doi.pangaea.de/10.1594/PANGAEA.929010, b. https://doi.pangaea.de/10.1594/PANGAEA.946177

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
- Sea ice freeboard maps
- Processing workflow diagram
- Sample CSV output (Eastern Weddell Feb 2024 CSV file. Contains latitude,, longitude, freeboard, segment_length, Thickness (m))

## Related publication:

Joshi, M., Mestas-Nuñez, A. M., Ackley, S. F., Arndt, S., Macdonald, G. J., & Haas, C. (2024).
Seasonal and Interannual Variations in Sea Ice Thickness in the Weddell Sea, Antarctica (2019–2022)
Using ICESat-2. Remote Sensing, 16(20), 3909.

If you use this code, please cite:

Joshi, M. (2026). GitHub: https://github.com/mhjoshi5-cmd/Sea-ice-thickness-ICESat2-pipeline

## Author

Mansi Joshi, PhD  
Geospatial Data Scientist | Remote Sensing | GIS | Python
