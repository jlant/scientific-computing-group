# demo of module and __name__

__version__ = "1.0"
__date__ = "2014-09-12"
#print("Using {} version: {}, {}".format(__name__, __version__, __date__))


def add(a, b):
	""" Add two numbers a and b"""
	return a + b

def multiply(a, b):
	""" Multiply two numbers a and b"""
	return a * b

def main():
	print("inside module1 - module1 __name__ is {}".format(__name__))
	
if __name__ == "__main__":
	main()


