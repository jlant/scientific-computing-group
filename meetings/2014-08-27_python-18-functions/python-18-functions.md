Python - Functions
==================

Objectives
----------

* Write and call functions with named arguments, unnamed arguments, and no arguments

*****
Notes
-----

**function syntax**

    def function_name(parameter1, parameter2, ...):
		""" Document the function """
		<statements>
		return <return_value>
		

*****
Examples
--------

	# define a function called average
	def average(numbers):
		""" Compute the average for a list of numbers """
		result = sum(numbers) / len(numbers)
		
		return result

	# call the function
	avg = average(numbers = [1, 2, 3])
	print("The average is: {0:.2f}".format(avg))
		
*****
References
----------

* [Software Carpentry - Python: Functions]



[Software Carpentry - Python: Functions]:http://software-carpentry.org/v4/python/func.html
