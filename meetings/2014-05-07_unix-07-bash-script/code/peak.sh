# Script to find the peak discharge value in the file 03290500_dv.txt 
grep -v -e "#" -e "agency_cd" -e "5s" 03290500_dv.txt | cut -f 3-4 | sort -n -k2 | tail -1 

