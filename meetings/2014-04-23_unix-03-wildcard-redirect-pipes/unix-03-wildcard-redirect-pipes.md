Unix commands
=============

*****
Objectives
----------

1. Learn some more Unix commands
	* Wildcard commands
	* Redirect output from a command to a file
	* Append the output from a command to a file
	* Take output from one command and “pipe” it as input to another command

*****
Notes
-----

**Unix Commands**

	*		-	matches any number of characters
	>		-	redirect standard output to a file
	>>		-	append standard output to a file
	|		-	take output from a command (on the left of the pipe) and "pipe" it as input to command (on the right of the pipe)
	sort	- 	sorts in alphabetical order; use -n flag to sort in numeric order

*****
Examples
--------

	$ ls *.txt
	$ echo hello > hello.txt
	$ echo world >> hello.txt
	
	$ ls *.txt | wc -l
	
	$ history > 2014-04-16_command-history.txt
	
	$ cat datafile.txt
	20
	14
	18
	
	$ sort datafile.txt
	14
	18
	20

*****
References
----------

* [Software Carpentry - Pipes and Filters]
* [Introduction to Unix/Wildcards]
* [Redirection]
* [Pipeline]
* [Sort]

[Software Carpentry - Pipes and Filters]: http://software-carpentry.org/v4/shell/pipefilter.html
[Introduction to Unix/Wildcards]:http://en.wikibooks.org/wiki/A_Quick_Introduction_to_Unix/Wildcards
[Redirection]:http://en.wikipedia.org/wiki/Redirection_%28computing%29
[Pipeline]:http://en.wikipedia.org/wiki/Pipeline_%28Unix%29
[Sort]:http://en.wikipedia.org/wiki/Sort_%28Unix%29