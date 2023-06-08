# Use this file if you have downloaded MAR and RACMO freshwater discharge data from GEUS (https://dataverse.geus.dk/dataset.xhtml?persistentId=doi:10.22008/FK2/XKQVL7) and want to subset it to your preferred time span. 
# This is useful for creating smaller files if you don't need the whole time series.
# The discharge.py script (from https://github.com/GEUS-Glaciology-and-Climate/freshwater) that is used to get fjord outlets and fjord discharge is specifically looking for files named MAR.nc and RACMO.nc, so we rename our original data files, and use MAR.nc and RACMO.nc for the subsets we produce.

import argparse
import pandas as pd
import xarray as xr
from pathlib import Path

# Command-line arguments (start date and end date)
parser = argparse.ArgumentParser(description="subset original MAR and RACMO files in ../freshwater by time")
parser.add_argument("--tstart", help="start date (YYYY-MM-DD)")
parser.add_argument("--tend", help="end date (YYYY-MM-DD)")
args = parser.parse_args()

# Convert date strings to datetime
start_date = pd.to_datetime(args.tstart)
end_date = pd.to_datetime(args.tend)

# Load original data files
# Note that loading without `engine='h5netcdf'` results in an error - issue with original data source
print('Loading original data under ../freshwater')
discharge_ice_mar = xr.open_dataset('../freshwater/ice/MAR.nc', engine='h5netcdf')
discharge_ice_racmo = xr.open_dataset('../freshwater/ice/RACMO.nc', engine='h5netcdf')
discharge_land_mar = xr.open_dataset('../freshwater/land/MAR.nc', engine='h5netcdf')
discharge_land_racmo = xr.open_dataset('../freshwater/land/RACMO.nc', engine='h5netcdf')

# Rename original data files
print('Renaming original data by appending \'_original\'')
Path('../freshwater/ice/MAR.nc').rename(Path('../freshwater/ice/MAR_original.nc'))
Path('../freshwater/ice/RACMO.nc').rename(Path('../freshwater/ice/RACMO_original.nc'))
Path('../freshwater/land/MAR.nc').rename(Path('../freshwater/land/MAR_original.nc'))
Path('../freshwater/land/RACMO.nc').rename(Path('../freshwater/land/RACMO_original.nc'))

# Subset to desired time range and save to new files
print('Subsetting to dates and saving under ../freshwater')
discharge_ice_mar.sel(time=slice(start_date, end_date)).to_netcdf(f'../freshwater/ice/MAR.nc', engine='h5netcdf')
discharge_ice_racmo.sel(time=slice(start_date, end_date)).to_netcdf(f'../freshwater/ice/RACMO.nc', engine='h5netcdf')
discharge_land_mar.sel(time=slice(start_date, end_date)).to_netcdf(f'../freshwater/land/MAR.nc', engine='h5netcdf')
discharge_land_racmo.sel(time=slice(start_date, end_date)).to_netcdf(f'../freshwater/land/RACMO.nc', engine='h5netcdf')

print('Done.')