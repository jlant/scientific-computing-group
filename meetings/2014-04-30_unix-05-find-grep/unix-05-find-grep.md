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

	$ find data-folder -name *tom.txt | wc -l

*****
References
----------

* [Software Carpentry - Unix Shell: Find]
* [grep]


[Software Carpentry - Unix Shell: Find]:http://software-carpentry.org/v4/shell/find.html	
[grep]:http://en.wikipedia.org/wiki/Grep

