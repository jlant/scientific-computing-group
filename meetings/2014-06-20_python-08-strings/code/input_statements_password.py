# Demo - user input 
# Purpose: More practice integrating user input with a while loop and a conditional

# Constants in Python are by convention specified by all caps
PASSWORD = "python!"

# Prompt user for a password until user enters a valid password
valid_password = False
while not valid_password:

	ans = raw_input("Please enter password: ")
	
	if ans == PASSWORD:
		valid_password = True
		print("Correct password!")
		
	else:
		print("Wrong password!\n")
	
		
