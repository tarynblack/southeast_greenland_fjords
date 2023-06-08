# This file is called within generate_fjord_FWdischarge.sh to calculate total freshwater discharge from MAR and from RACMO
# The output is used in freshwater_discharge.ipynb

import argparse
import pandas as pd

# Command-line argument (fjord number)
parser = argparse.ArgumentParser(description="subset original MAR and RACMO files in ../freshwater by time")
parser.add_argument("-f", "--fjord", help="fjord ID number")
args = parser.parse_args()

fjord_number = int(args.fjord)

# Read in fjord discharge file (created in generate_fjord_FWdischarge.sh), add MAR/RACMO totals columns, write
fjord_discharge = pd.read_csv(f'./fjord_discharge/fjord{fjord_number:02}_discharge.txt').set_index('time')
fjord_discharge.index = pd.to_datetime(fjord_discharge.index)
if ('MAR_ice' in fjord_discharge.keys()) & ('MAR_land' in fjord_discharge.keys()):
    fjord_discharge['MAR_total'] = fjord_discharge['MAR_land'] + fjord_discharge['MAR_ice']
elif ('MAR_ice' in fjord_discharge.keys()) & ('MAR_land' not in fjord_discharge.keys()):
    fjord_discharge['MAR_total'] = fjord_discharge['MAR_ice']
elif ('MAR_ice' not in fjord_discharge.keys()) & ('MAR_land' in fjord_discharge.keys()):
    fjord_discharge['MAR_total'] = fjord_discharge['MAR_land']
if ('RACMO_ice' in fjord_discharge.keys()) & ('RACMO_land' in fjord_discharge.keys()):
    fjord_discharge['RACMO_total'] = fjord_discharge['RACMO_land'] + fjord_discharge['RACMO_ice']
elif ('RACMO_ice' in fjord_discharge.keys()) & ('RACMO_land' not in fjord_discharge.keys()):
    fjord_discharge['RACMO_total'] = fjord_discharge['RACMO_ice']
elif ('RACMO_ice' not in fjord_discharge.keys()) & ('RACMO_land' in fjord_discharge.keys()):
    fjord_discharge['RACMO_total'] = fjord_discharge['RACMO_land']
fjord_discharge.to_csv(f'./fjord_discharge/fjord{fjord_number:02}_discharge_total.txt')