#!/bin/bash

# Use Ken Mankoff's discharge script and data to access freshwater discharge into fjords
# See https://github.com/GEUS-Glaciology-and-Climate/freshwater
#
# USAGE
# Iterate (f) over list of fjord numbers
# Input (FIN): fjord boundaries (ours have 500m buffer, as KML, created by Ben Cohen)
# Output (FOUT): time series of fjord discharge (from MAR and RACMO, ice and land basins) as .txt
# In command, paths are to Mankoff's discharge script and base directory

for f in {1..52}
do
    echo "Fjord $f"
    
    # filenames
    FIN=$(printf "./buffered_fjords/Fjord_%d.kml" $f)
    FOUT=$(printf "./fjord_discharge/fjord%02d_discharge.txt" $f)

    # run Mankoff's discharge script to get fjord discharge in our buffered fjord
    python3 ../freshwater/discharge.py --base ../freshwater --roi=$FIN -d > $FOUT

    # run our helper script to calculate total MAR/RACMO discharge in the fjord
    python3 ./calculate_total_FWdischarge.py --fjord=$f
done