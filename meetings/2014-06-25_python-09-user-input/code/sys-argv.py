# Demo of sys.argv

import sys

# Print out the filename
filename = sys.argv[0]
print("The file name is: {}".format(filename))

# Print out the rest of the arguments
arguments = sys.argv[1:]
print("The rest of the arguments are: {}".format(arguments))

