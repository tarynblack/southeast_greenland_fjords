# southeast_greenland_fjords
Code and data for analysis of freshwater discharge and solid ice discharge in fjords in southeast Greenland.

This repository contains three Jupyter Notebooks which perform freshwater and solid ice discharge analysis on fjords in southeast Greenland, plus several helper scripts for generating your own data.

## Requirements

### Solid ice discharge
For the solid ice discharge analysis, you will need [ice discharge data](https://doi.org/10.22008/promice/data/ice_discharge/d/v02) [1,2]. We used v79 (published 2023-05-05) and stored at `../IceDischarge_Mankoff`.

The solid ice discharge analysis also uses `./glaciers_fjords.txt` (which links our glacier pointIDs to our Fjord IDs) and `./relate_pointID_glacierID.txt` (which relates our glacier pointIDs, Joughin glacierIDs, and Mankoff's gate IDs). If you are adapting this analysis for your own glaciers/fjords you will need to create your own versions of these files.

### Freshwater discharge
We used the [freshwater discharge data](https://doi.org/10.22008/FK2/XKQVL7) archived by GEUS [3,4]. We used v4.2 (published 2022-08-28) and stored at `../freshwater`. Because the NetCDF files are very large (several GB each), after downloading you may wish to subset them to your time frame of interest (we used 2015-2019), using `./subset_FWdischarge.py`. 

We used Ken Mankoff's [freshwater repository](https://github.com/GEUS-Glaciology-and-Climate/freshwater) [4] (installed from commit `d23db55`) to generate fjord discharge and outlet files. This is also stored at `../freshwater` (because the data archive and the repository are tied together and use the same name, and the structure just works...). This repository is not needed to run our analysis using our provided data, but is required to produce your own data files.

In order to access outlets and discharge from each fjord, we created fjord boundaries with a 500m buffer to ensure that they capture nearby outlets. These are stored in `./buffered_fjords`. Ben Cohen created these KMLs (thanks Ben!).

We used the `freshwater` repo and the boundaries in `./buffered_fjords` to create:
- `./fjord_discharge/*.txt`: time series of fjord discharge, including MAR and RACMO discharge sourced from ice and land basins, and summed across these basins.
- `./fjord_outlets/*.txt`: list of ice and land outlets within each fjord boundary

#### Generating your own freshwater discharge data
You will need to download the freshwater discharge data and repository, then we provide several helper scripts to process them.

1. Download the [freshwater repository](https://github.com/GEUS-Glaciology-and-Climate/freshwater) [4] (we installed from commit `d23db55`) and store it at `../freshwater`.

2. Download the [freshwater discharge data](https://doi.org/10.22008/FK2/XKQVL7) [3,4] (we used v4.2) and store it at `../freshwater`.

3. (optional) If you don't need the entire MAR/RACMO time series and want smaller files, you can subset them by time using `./subset_FWdischarge.py`. Command line usage (replace YYYY-MM-DD with your start and end dates, inclusive):  
```python3 ./subset_FWdischarge.py --tstart=YYYY-MM-DD --tend=YYYY-MM-DD```  
This will rename the original data files as `*_original.nc` and create new time-subsetted files named `MAR.nc` and `RACMO.nc` (we use this naming because the `freshwater` repo specifically looks for those filenames).

4. Store your fjord outlines under `./buffered_fjords`. The filenames should be `Fjord_#.kml`. We suggest applying a buffer to these outlines to ensure that nearshore outlets are captured (we used 500m).

5. Run `./generate_fjord_FWoutlets.sh` in the command line. This will find all land and ice outlets within each fjord boundary and save them to a .txt in `./fjord_outlets`. You will need to modify the .sh file for your fjord numbers.

6. Run `./generate_fjord_FWdischarge.sh` in the command line. This will create a time series of freshwater discharge into a fjord from land and ice outlets (and sum those together), for MAR and RACMO, and save them to a .txt in `./fjord_discharge`. You will need to modify the .sh file for your fjord numbers.

7. You're ready to run the analyses in `freshwater_discharge.ipynb` and `freshwater_discharge_depth.ipynb`! Modify the user parameters in these files as needed. See below for notebook descriptions.

## Analysis
Discharge analysis is performed in three different notebooks. Each of these notebooks contains a code cell of user parameters that you should modify before analyzing your own data.

- `freshwater_discharge.ipynb`  
**Input:** `./fjord_discharge`  
This notebook generates figures and spreadsheets of freshwater discharge for each fjord in the study. The figures show freshwater discharge (from both MAR and RACMO) derived from ice basins, from land basins, and from combined ice+land basins. The spreadsheets describe the cumulative, annual mean, and seasonal mean freshwater discharge in each fjord.  

- `freshwater_discharge_depth.ipynb`  
**Input:** `../freshwater/ice/*.nc`, `../freshwater/land/*.nc`, `./fjord_outlets`  
This notebook generates figures and spreadsheets of freshwater discharge as a function of depth for each fjord in the study, and cumulatively across all fjords. Figures represent time series of discharge above/below a threshold depth, and of discharge binned by depth.  

- `solid_ice_discharge.ipynb`  
**Input:** `../IceDischarge_Mankoff`, `./glaciers_fjords.txt`, `./relate_pointID_glacierID.txt`  
This notebook generates figures and spreadsheets of solid ice discharge for each glacier and fjord in the study. Glacier observations are interpolated and summed together to estimate fjord-level solid ice discharge. The plots show the discharge time series as well as the mean annual, mean hydrological year, and mean seasonal discharge for each fjord. The spreadsheets contain cumulative and per-fjord statistics about solid ice discharge.  

## Output
These notebooks will save figures under `../figures/` and summary data under `../databases/`. If you have all the data and run everything, the final structure will look like:
```
- project_directory/
  - southeast_greenland_fjords/ (this repository)
    - buffered_fjords/
    - fjord_discharge/
    - fjord_outlets/
    - (code files)
  - freshwater/ (freshwater discharge data and repository)
    - ice/
    - land/
    - (code files)
  - IceDischarge_Mankoff (solid ice discharge data)
  - figures/
    - fjord_FWdischarge/
    - fjord_FWdischarge_depthbinned_{MAR, RACMO}/
    - fjord_FWdischarge_depththreshold_{MAR, RACMO}/
    - glacier_icedischarge_interpolated/
    - glacier_icedischarge_observed/
    - allfjords_FWdischarge_depthbinned_{MAR, RACMO}_combined.png
    - allfjords_FWdischarge_depthbinned_{MAR, RACMO}_landvsice.png
  - databases/
    - fjord_FWdischarge_depthbinned_{MAR, RACMO}_combined/
    - fjord_icedischarge_components/
    - fjord_icedischarge_monthly/
    - fjord_FWdischarge_{cumulative, annualmean, seasonalmean}.csv
    - fjord_FWdischarge_mean_annual_deep_{MAR, RACMO}.csv
    - fjord_icedischarge_interp.csv
    - glacier_icedischarge_interp.csv
```

## References
[1] Mankoff, Ken; Solgaard, Anne; Larsen, Signe, 2020, "Greenland Ice Sheet solid ice discharge from 1986 through last month: Discharge", [doi:10.22008/promice/data/ice_discharge/d/v02](https://doi.org/10.22008/promice/data/ice_discharge/d/v02), GEUS Dataverse, V79

[2] Mankoff, K. D., Solgaard, A., Colgan, W., Ahlstrøm, A. P., Khan, S. A., and Fausto, R. S., 2020, "Greenland Ice Sheet solid ice discharge from 1986 through March 2020", Earth Syst. Sci. Data, 12, 1367–1383. [doi:10.5194/essd-12-1367-2020](https://doi.org/10.5194/essd-12-1367-2020)

[3] Mankoff, Ken, 2020, "Streams, Outlets, Basins, and Discharge [k=1.0]", [doi:10.22008/FK2/XKQVL7](https://doi.org/10.22008/FK2/XKQVL7), GEUS Dataverse, V4

[4] Mankoff, K. D., Noël, B., Fettweis, X., Ahlstrøm, A. P., Colgan, W., Kondo, K., Langley, K., Sugiyama, S., van As, D., and Fausto, R. S., 2020, "Greenland liquid water discharge from 1958 through 2019", Earth Syst. Sci. Data, 12, 2811–2841. [doi:10.5194/essd-12-2811-2020](https://doi.org/10.5194/essd-12-2811-2020)

