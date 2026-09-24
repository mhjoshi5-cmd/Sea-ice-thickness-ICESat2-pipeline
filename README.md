# ICESat-2 Sea-Ice Thickness Retrieval and Field Validation

A Python-based research pipeline for retrieving Antarctic sea-ice thickness from ICESat-2 ATL10 freeboard observations using an improved buoyancy approach. The project supports satellite-based investigations of sea-ice thickness variability in the Weddell Sea and comparisons with independent field observations.

**Associated publication**

Joshi, M., Mestas-Nuñez, A. M., Ackley, S. F., Arndt, S., Macdonald, G. J., & Haas, C. (2024). Seasonal and Interannual Variations in Sea Ice Thickness in the Weddell Sea, Antarctica (2019–2022) Using ICESat-2. *Remote Sensing, 16*(20), 3909.

## 1. Research overview

* Reliable observations of Antarctic sea-ice thickness are essential for investigating sea-ice variability and understanding interactions between the atmosphere, ocean and cryosphere.
* Satellite laser altimetry provides measurements of sea-ice freeboard, which can be converted to thickness estimates using hydrostatic equilibrium assumptions and information about snow loading.
* This repository implements a processing workflow for ICESat-2 ATL10 observations, including data extraction, quality filtering, snow-depth estimation, thickness estimation and preparation of geospatial outputs.
* The resulting thickness estimates were compared with ship-based electromagnetic measurements and snow-buoy observations from the 2019–2024 study period.
* The repository demonstrates the ICESat-2 ATL10 component of this research.

## 2. Research objectives

* Process ICESat-2 ATL10 HDF5 files to extract sea-ice freeboard and associated geolocation and segment information.
* Estimate sea-ice thickness using an improved buoyancy approach incorporating empirical snow-depth estimation.
* Automate the processing of multiple satellite files.
* Prepare datasets for spatial analysis and comparison with field observations.
* Support investigations of seasonal and interannual sea-ice thickness variability.

## 3. Satellite and field observations

### ICESat-2 observations

The pipeline processes the ATL10 sea-ice freeboard product and extracts:

* Freeboard height
* Latitude and longitude
* Height-segment length
* Associated segment metadata

### Independent field observations

Field comparisons incorporate observations from 2019, 2021 and 2022, including snow-depth and sea-ice thickness measurements.

Snow depth was measured using a GPS-equipped Magna Probe, with a reported horizontal resolution of 1–2 m. Total sea-ice thickness was measured using ground-based multi-frequency electromagnetic induction instruments.

Relevant datasets:

* [PANGAEA dataset 929010](https://doi.pangaea.de/10.1594/PANGAEA.929010)
* [PANGAEA dataset 946177](https://doi.pangaea.de/10.1594/PANGAEA.946177)

Additional methodological details are provided in the associated publication.

## 4. Processing methodology

The pipeline follows five principal stages.

**Stage 1 —Read and extract Satellite data**

Read ICESat-2 ATL10 HDF5 files and extract the required geophysical and geolocation variables.

**Stage 2 — Data preparation**

Identify and remove invalid observations and organize the extracted measurements for subsequent processing.

**Stage 3 — Snow-depth estimation**

Estimate snow depth from satellite-derived freeboard using an empirical relationship.

**Stage 4 — Sea-ice thickness retrieval**

Apply the improved buoyancy approach, based on hydrostatic equilibrium between seawater, sea ice and snow, to estimate sea-ice thickness.

**Stage 5 — Output generation**

Process multiple ATL10 files and export structured CSV datasets containing geolocation, freeboard, segment length and estimated sea-ice thickness.

## 5. Comparison with field measurements

* Satellite derived thickness estimates were compared with independent ship-based electromagnetic observations and snow-buoy data.
* Spatial comparisons were conducted in ArcGIS Pro using buffer analysis and a minimum-distance criterion to identify ICESat-2 observations closest to field measurement locations.
* The field comparisons provide an observational basis for evaluating satellite-derived thickness estimates. The associated publication provides the broader scientific context and analysis.

## 6. Technical implementation

**Language:** Python

**Core libraries:** NumPy, Pandas and h5py

**Geospatial analysis:** ArcGIS Pro

**Processing capabilities:**

* Automated processing of multiple ATL10 HDF5 files
* Extraction and filtering of satellite observations
* Empirical snow-depth estimation
* Physics-based sea-ice thickness retrieval
* Structured CSV export
* Error handling and logging

## 7. Research outputs

The workflow producesdatasets suitable for mapping sea-ice freeboard and thickness and for subsequent spatial analysis.

Example outputs include:

* Sea-ice freeboard maps
* A processing workflow diagram
* A sample CSV dataset for the eastern Weddell Sea in February 2024 (The sample CSV includes latitude, longitude, freeboard, segment length and estimated thickness in metres.)

## 8. Scientific context

This repository is associated with the peer-reviewed study:

**Seasonal and Interannual Variations in Sea Ice Thickness in the Weddell Sea, Antarctica (2019–2022) Using ICESat-2**

Joshi et al. (2024), *Remote Sensing*, 16(20), 3909.

The study provides the scientific context for the satellite retrieval methodology and investigation of sea-ice thickness variability in the Weddell Sea.

## 9. Citation

If you use this repository, please cite the associated publication and acknowledge the software:

Joshi, M. (2026). *ICESat-2 Sea-Ice Thickness Pipeline*. GitHub. https://github.com/mhjoshi5-cmd/Sea-ice-thickness-ICESat2-pipeline

## Author

**Mansi Joshi, PhD**

Geospatial Data Scientist | Satellite Remote Sensing | Sea-Ice Observations | Python
