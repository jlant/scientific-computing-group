# Author: Jeremiah Lant
# Purpose: Finding peak values for any NWIS daily value file.

for filename in *dv.txt
do
	echo $filename
	grep ^USGS $filename | cut -f 3-4 | sort -n -k2 | tail -1
	echo 
done
