# Introduction to functions

def subtract(a, b):
	""" Subtract two numbers a and b, and return the result """
	result = a - b
	return result

answer1 = subtract(1, 2)			# unnamed arguments
print(answer1)

answer2 = subtract(a = 1, b = 2)	# named arguments
print(answer2)

answer3 = subtract(b = 2, a = 1)	# named arguments in reverse order
print(answer3)

answer4 = subtract(2, 1)			# unnamed arguments in reverse order
print(answer4)


def greet(name = "Bob"):
	""" Print a friendly greeting to the screen with a particular name """
	print("Hello there {}. Hope you are having a good day.".format(name))

greet(name = "Jeremiah")			# named argument
greet("Dave")						# unnamed argument
greet()


def average(numbers):
	""" Compute and return the average of a list of numbers """
	result = sum(numbers) / len(numbers)
	
	return result
	
avg1 = average(numbers = [1, 2, 3])
print("Average is: {}".format(avg1))


def test_average_normal():
	""" Test the functionality of the function called average """
	expected = 2						# expected result
	actual = average([1, 2, 3])			# actual result
	
	assert actual == expected, "actual: {0} does not equal expected {1}".format(actual, expected)

def test_average_with_nan():
	""" Test the functionality of the function called average """
	expected = 2						# expected result
	actual = average([1, 2, nan])			# actual result
	
	assert actual == expected, "actual: {0} does not equal expected {1}".format(actual, expected)

	
test_average_normal()
test_average_with_nan()