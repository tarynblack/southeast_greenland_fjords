# southeast_greenland_fjords
Code and data for analysis of freshwater runoff and solid ice discharge in fjords in southeast Greenland.

This repository contains three Jupyter Notebooks which perform freshwater and solid ice discharge analysis on fjords in southeast Greenland.

## `freshwater_discharge.ipynb`
This notebook generates figures and spreadsheets of freshwater discharge for each fjord in the study. The figures show freshwater discharge (from both MAR and RACMO) derived from ice basins, from land basins, and from combined ice+land basins. The spreadsheets describe the cumulative, mean, and seasonal freshwater discharge in each fjord.

This notebook uses the text files in `./buffered_fjords` and `./fjord_discharge`. The files in `./buffered_fjords` represent fjord boundaries plus a 500m buffer. The files in `./fjord_discharge` represent freshwater discharge time series for each fjord, and can alternately be created by the user using [this repository](https://github.com/GEUS-Glaciology-and-Climate/freshwater) and by following the instructions provided within the notebook. Note that we used v2.1 of the data associated with that repository, whereas users generating new data should use v3.

## `freshwater_runoff_depth.ipynb` 
This notebook generates figures and spreadsheets of freshwater discharge as a function of depth for each fjord in the study, and cumulatively across all fjords.

This notebook uses the text files in `./fjord_outlets`, which contain lists of land/ice discharge outlets in each fjord. This notebook also requires the use of [this repository](https://github.com/GEUS-Glaciology-and-Climate/freshwater) (the same as for `freshwater_discharge.ipynb`) to complete the data analysis. Note that we used v2.1 of the data associated with that repository, whereas users generating new data should use v3.

## `solid_ice_discharge.ipynb` 
This notebook generates figures and spreadsheets of solid ice discharge for each fjord in the study. The plots show the discharge time series as well as the mean annual, mean hydrological year, and mean seasonal discharge for each fjord. The spreadsheets contain cumulative and per-fjord statistics about solid ice discharge.

This notebook analyzes data from Mankoff _et al._ (2020) which can be downloaded here: https://doi.org/10.22008/promice/data/. This notebook also uses the files `./glaciers_fjords.txt` and `./relate_pointID_glacierID.txt` to associate glaciers and fjords together and to translate across different glacier identification schemes.

## Output
These notebooks will save figures under `../figures/` and summary data under `../databases/`.

