# Script to find the peak discharge value in any file that ends in "dv.txt"
for filename in *dv.txt
do
	echo $filename
	grep -v -e "#" -e "agency_cd" -e "5s" $filename | cut -f 3-4 | sort -n -k2 | tail -1 
	echo
done

