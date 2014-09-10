# Demo of Python scoping
# Run the program and the output will be:
#
#	$ python scoping2.py
#	local c: 2
#	global c: 1

def add(a, b):
	""" Return sum of two numbers, a and b"""
	d = a + b

	# c is a local variable because of the assignment; only known in scope of add() function because  
	# there is no global declaration; global variable c is NOT reassigned
	c = 2		
	print("local c: {}".format(c)) 
	
	return d

# main program
c = 1			# c is a global variable
ans = add(1, 2)
print("global c: {}".format(c))		
