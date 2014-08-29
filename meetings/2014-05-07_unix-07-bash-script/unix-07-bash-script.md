Unix commands
=============

*****
Objectives
----------

1. Learn some more Unix commands
    * Write a bash script
	* Introduce the for loop

*****
Notes
-----

**Bash script** - file containing series of unix commands to execute

**For loop** - used to repeat a set of commands a certain number of times 

	for item in list-of-items
	
	do
		echo $item
	done

*****
**In shell as a one line command**

	$ for filename in *.txt; do echo $filename; done

*****
**In shell as a multiple line command**

	$ for filename in *.txt
	> do 
	>    echo $filename
	> done

*****
**In shell script**

    for filename in *.txt
	do 
	    echo $filename
	done

*****
Examples
--------

**Sample Measurements file:** 2012_measurements_bob.txt

	agency	site_num	date		discharge	approved_preliminary_flag
	USGS	03290500	2012-07-01	171	A
	USGS	03290500	2012-07-02	190	A
	USGS	03290500	2012-07-03	164	A
	USGS	03290500	2012-07-04	151	A
	USGS	03290500	2012-07-05	153	A

**find-max-measurement.sh**

	for filename in data-directory/*measurements*.txt
	
	do
		echo $filename
		grep ^USGS $filename | cut -f 4 | sort -n | uniq | tail -1
	done

**read-command-line-args.sh**

	# read command line arguments from command line
	ARG0=$0
	ARG1=$1
	ARG2=$2

	echo "Argument 0 is: " $ARG0
	echo "Argument 1 is: " $ARG1
	echo "Argument 2 is: " $ARG2

	# read user input from command line
	echo -n "Enter your name and press [ENTER]: "
	read name
	echo $name

	
*****
References
----------

* [Bash Shell Scripting]


[Bash Shell Scripting]:http://en.wikibooks.org/wiki/Bash_Shell_Scripting