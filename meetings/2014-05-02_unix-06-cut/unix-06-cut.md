Unix commands
=============

*****
Objectives
----------

1. Learn some more Unix commands
	* Cut out columns of interest from a data file

*****
Notes
-----

**Unix Commands**

	cut			-	extract (cut) sections (columns) from a file; <tab> is default delimiter

*****
Examples
--------

	$ cat 2014-measurements-bob.txt
	date, parameter, value
	2014-04-01,stage,17
	2014-04-02,stage,20
		.
		.
		.
	
	$ cut -d , -f 1 2014-measurements-bob.txt
	2014-04-01
	2014-04-02

*****
References
----------

* [cut]


[cut]:http://en.wikipedia.org/wiki/Cut_%28Unix%29