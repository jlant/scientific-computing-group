# Python - Read measurements project, refactoring

*****
## Objectives

1.  Refactor the read_measurements.py file to dynamically handle any order, number, or set of parameters.


*****
## Notes

* **7+-2 rule** - [The Magical Number Seven, Plus or Minus Two: Some Limits on our Capacity for Processing Information - George Miller]
    - most people can only retain 5 to 9 items in their short-term memory 
* Try to write small "chunks" of code (**functions**).  Having small(ish) chunks of code (**functions**) allows for you and others to more easily:
	1. read, understand, and comprehend your code
	2. [unit test] your functions.  Please see [Testing Your Code]
 

*****
## Examples

**Harder to understand** - nested for loops; outer loop loops through a dictionary and inner loop loops through a list
```python
def format_parameters(parameters):
	""" Return a dictionary with each key containing lists of floating point numbers """
	
	for key, values in parameters.iteritems():
		new_values = []
		for value in values:
			new_values.append(float(value))	

		parameters[key] = new_values
	
	return parameters
```

**Easier to understand** - create a second *understandable* and *readable* function that the other function uses
```python
def convert_to_float(str_list):
	""" Return a list of floats """
	values = []
	for value in str_list:
		values.append(float(value))	
	
	return values
	
def format_parameters(parameters):
	""" Return a dictionary with each key containing lists of floating point numbers """
	
	for key, values in parameters.iteritems():
		values = convert_to_float(values)
		parameters[key] = values
	
	return parameters
```

*****
## Questions / Comments


*****
## References
* [The Magical Number Seven, Plus or Minus Two: Some Limits on our Capacity for Processing Information - George Miller]
* [unit test]
* [Testing Your Code]

[unit test]:http://en.wikipedia.org/wiki/Unit_testing
[Testing Your Code]:http://docs.python-guide.org/en/latest/writing/tests/
[The Magical Number Seven, Plus or Minus Two: Some Limits on our Capacity for Processing Information - George Miller]:http://psychclassics.yorku.ca/Miller/
