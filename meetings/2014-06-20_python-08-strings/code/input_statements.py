# Demo - input from user

# ask for user's name
name = raw_input("What is your name? ")
print("Your name is: {}".format(name))
print("")

# ask for user's age
age = raw_input("How old are you? \n")
print("Your age is: {}".format(age))
print("")

# ask for user's hobbies
hobbies_str = raw_input("List a few of your hobbies separated by commas: \n")
print("Your hobbies (as a string) are: {}".format(hobbies_str))
print("")

hobbies_list = hobbies_str.split(",")
print("Your hobbies (as a list) are: {}".format(hobbies_list))
print("The first hobby in your list is: {}".format(hobbies_list[0]))
print("")

# ask for user's favorite floating point number and print it out to 5 decimal places
number_str = raw_input("What is your favorite floating point number? \n")
number = float(number_str)
print("Your favorite floating point number is: {0:.5f}".format(number))
print("")

# collect all this information about the user and print it as a simple report/summary
info = {"name": name, "age": age, "hobbies": hobbies_list, "number": number}

for key, value in info.items():
	print("Your {0} is {1}".format(key, value))

# A little better 
for key, value in info.items():
	if key == "hobbies":
		print("Your {0} are {1}".format(key, value))
	else:
		print("Your {0} is {1}".format(key, value))