# Demo of Python scoping
# Run the program and the output will be:
#
#	$ python scoping3.py
#	local c: 2
#	global c: 1		

def add(a, b):
	""" Return sum of two numbers, a and b"""
	d = a + b

	c = 2			# c is a local variable to add() function	
	print("local c: {}".format(c))  
	
	return d

def main():
	c = 1			# c is a local variable to main() function; NO GLOBAL VARIABLES!
	ans = add(1, 2)
	print("global c: {}".format(c))	

if __name__ == "__main__":
	main()
