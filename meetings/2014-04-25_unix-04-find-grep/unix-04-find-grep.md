Unix commands
=============

*****
Objectives
----------

1. Learn some more Unix commands
	* Creating aliases and variables
	* Finding matching text in files
	* Find files themselves whose name matches a pattern

*****
Notes
-----

**Unix Commands**

	.bashrc		-	bash initialization file containing shell commands to execute upon startup; located in users home directory 
	grep		-	stands for **g**lobal **re**gular expression **p**rint; finds matching text
	find		-	find files themselves; use -name flag to file files matching a giving pattern

*****
Examples
--------

	$ cd ~
	$ cat .bashrc
	$ export MYPROJ=/c/path/to/some/project
	$ cd $MYPROJ
	
	$ cat 2014_measurements-bob.txt
	date		temperature (celsius)
	2014-01-01	-3
	2014-01-02	-5
	    .
		.
		.
	2014-12-31	2
	
	$ grep 2014-04-16 2014_measurements-bob.txt
	2014-04-16	12
	
	$ grep *-04-* 2014_measurements-bob.txt
	2014-04-01	10
		.
		.
		.
	2014-04-30	16
	
	$ ls data-folder
	2009_measurements-tom.txt
	2010_measurements-linda.txt
	2011_measurements-jerry.txt
	2012_measurements-tom.txt
	2013_measurements-sara.txt
	2014_measurments-bob.txt
	
	$ find data-folder -name *tom.txt
	2009_measurements-tom.txt
	2012_measurements-tom.txt	

*****
References
----------

* [Software Carpentry - Unix Shell: Find]
* [grep]


[Software Carpentry - Unix Shell: Find]:http://software-carpentry.org/v4/shell/find.html	
[grep]:http://en.wikipedia.org/wiki/Grep