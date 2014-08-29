Python - Read Measurements Project
==================================

Objectives
----------

1. Improve the python script that reads and processes a sample data file
2. Write a for loop to do stats and printing for each data parameter
3. Show how you can easily “redirect” the printed output to a file on the command line
4. Write the output to a file using python’s writeline and writelines
5. Write a for loop to handle multiple data files
6. Introduce and implement functions to do reading of file, stats, and printing 


*****
Notes
-----

**For loops** - use for loops instead of repeating code

**Redirection** - use to redirect standard output to a file

	$ python myscript.py > outputfile.txt

**Python - write files**

	file_obj = open("some-file.txt", mode = "w")
	
*****
Examples
--------

**Writing files**

	f = open("test.txt", "w")
	f.write("Hello everybody!\n")
	f.write("This is fun, right?")
	f.close()

	my_lines = ["go cats!\n", "go cornhuskers!\n", "go cardinals!"]
	f = open("cheers.txt", "w")
	f.writelines(my_lines)
	f.close()
