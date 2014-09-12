import module1

def main():
	ans = module1.add(a = 2, b = 3)
	print("using the add() function in module1, the answer is {}".format(ans))
	
	print("inside module2 - module1 __name__ is: {}".format(module1.__name__))
	
	print("inside module2 - module2 __name__ is: {}".format(__name__))
	
	
if __name__ == "__main__":
	main()
