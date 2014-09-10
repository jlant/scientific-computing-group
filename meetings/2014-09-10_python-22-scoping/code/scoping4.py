# Demo of Python scoping
# Run the program and the output will be:
#
#	$ python scoping3.py
#	local c: 2
#	global c: 2

c = 1			# c is a global variable

def add(a, b):
	""" Return sum of two numbers, a and b"""
	d = a + b

	global c						# getting access to global variable c
	c = 2							# reassigning c which changes the global variable
	print("local c: {}".format(c))  
	
	return d

# main program
ans = add(1, 2)
print("global c: {}".format(c))		
