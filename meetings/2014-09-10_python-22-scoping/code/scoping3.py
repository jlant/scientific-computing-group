# Demo of Python scoping
# Run the program and the output will be:
#
#	$ python scoping3.py
#	local c: 1
#	global c: 1

c = 1			# c is a global variable

def add(a, b):
	""" Return sum of two numbers, a and b"""
	d = a + b

	# accessing global variable c here because there is no local assignment
	print("local c: {}".format(c)) 
	
	return d

# main program
ans = add(1, 2)
print("global c: {}".format(c))		
