Unix commands
=============

*****
Objectives
----------

1. Learn some basic Unix commands
	* Creating directories and files
	* Looking at file contents
	* Moving and copying files and directories
	* Deleting files and directories
	* Finding text in files
	* Count number of lines, words, and characters in files

*****
Notes
-----

**Unix Commands**

	mkdir	-	make directory
	touch	-	create empty file; modify file's access, modify timestamps
	cat		- 	output contents of a file; concatenate and list files
	head	- 	display beginning of a file; default is 10 lines
	tail	- 	display end of a file; default is 10 lines
	less	-	terminal pager program; allows you to scroll through files
	mv		- 	move or rename files
	cp		-	copy files
	rm		-	remove files
	rmdir	- 	remove directory
	grep	- 	search file(s) for matching text
	wc		- 	count the number of lines, words, and characters in files

*****
Examples
--------

	$ mkdir temp
	$ touch junk.txt
	$ rm some-file.txt
	
	$ cp junk.txt ../some-folder
	$ mv junk.txt ../my-junk-folder/
	$ mv data-file1.txt 2014-04-16_measurements_bob.txt
	
	$ cat 2014-04-16_measurements_bob.txt
	$ head 2014-04-16_measurements_bob.txt
	$ tail 2014-04-16_measurements_bob.txt
	$ less 2014-04-16_measurements_bob.txt
	
	$ wc -l 2014-04-16_measurements_bob.txt

*****
References
----------

* [Software Carpentry - Unix Shell: Creating and Deleting]


[Software Carpentry - Unix Shell: Creating and Deleting]:http://software-carpentry.org/v4/shell/makedel.html
