# Demo of sys.argv
# Note: Providing arguments to programs are usually to:
#		1. send in data file(s) to process
#		2. provide options that determine various behaviors for the program
#			a. write output to the screen
#			b. save output to a file
#			c. show plots to the screen
#           d. compute stats
#           e. show results to the screen
#           f. compute stats and save to a file
#           g. ... and many more

import sys

# Print out the filename
filename = sys.argv[0]
print("The file name is: {}".format(filename))

# Print out the rest of the arguments
arguments = sys.argv[1:]
print("The rest of the arguments are: {}".format(arguments))

print("")

# Example usage of command line arguments
file_to_process = arguments[0]
options = arguments[1:]

print("Processing file: {}".format(file_to_process))

if "-stats" in options:
	# do some stats
	print("Computing stats and saved stats to a file called: stats.txt")

if "-plot" in options:
	# plot stuff
	print("Plotting results and saving to the following directory: ./plots/")
	
	