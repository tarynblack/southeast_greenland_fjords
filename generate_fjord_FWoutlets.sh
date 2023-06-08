#!/bin/bash

# Use Ken Mankoff's discharge script and data to identify freshwater discharge outlets inside fjord boundaries
# See https://github.com/GEUS-Glaciology-and-Climate/freshwater
#
# USAGE
# Iterate (f) over list of fjord numbers
# Input (FIN): fjord boundaries (ours have 500m buffer, as KML, created by Ben Cohen)
# Output (FOUT): list of fjord outlets as .txt
# In command, paths are to Mankoff's discharge script and base directory

for f in {1..52}
do
    echo "Fjord $f"
    
    FIN=$(printf "./buffered_fjords/Fjord_%d.kml" $f)
    FOUT=$(printf "./fjord_outlets/fjord%02d_outlets.txt" $f)

    python3 ../freshwater/discharge.py --base ../freshwater --roi=$FIN -o > $FOUT
done