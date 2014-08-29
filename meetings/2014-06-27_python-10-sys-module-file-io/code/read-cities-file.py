# Demo on reading files
# Note: Common pattern
#		1. open the file
#       2. read its contents
#       3. do something with the contents, e.g. process, analyze, statistics, plot, etc.
#		4. close the file

# Read all the contents of cities.txt as a string
file_object = open("cities.txt")
file_text = file_object.read()
print(file_text)
file_object.close()

print("")

# Read 5 bytes of cities.txt as a string
file_object = open("cities.txt")
first_five_bytes = file_object.read(5)
print(first_five_bytes)

print("")

# Read the next 10 bytes of cities.txt
# Note: the starting location in our file is now at the 5th byte
next_ten_bytes = file_object.read(10)
print(next_ten_bytes)

print("")

# Return to beginning of file and print out first city
file_object.seek(0)
first_ten_bytes = file_object.read(10)
print(first_ten_bytes)

file_object.close()

print("")

#--------------------------------------------
# Read all the contents of cities.txt as a list of lines in the file
file_object = open("cities.txt")
file_list = file_object.readlines()
print("The following is the list of lines in the file:\n{}".format(file_list))
file_object.close()

print("")

# Read all the contents of cities.txt using splitlines(), which splits the new line character
file_object = open("cities.txt")
file_text = file_object.read()
print("The following is the list of lines in the file using splitlines:\n{}".format(file_text.splitlines()))
file_object.close()

print("")

# Let's capitalize each city name
print("The following is a print out of each line in the file:\n")

file_object = open("cities.txt")
lines = file_object.readlines()
for each_line in lines:
	#print(each_line.rstrip("\n"))
	#print(each_line.strip())
	print(each_line.strip().upper())
	
file_object.close()