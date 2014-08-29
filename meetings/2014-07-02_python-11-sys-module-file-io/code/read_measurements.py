# Python script to read measurements file supplied by user
import sys

# get user supplied file
python_filename = sys.argv[0]
arguments = sys.argv[1:]
measurements_file = arguments[0]

# read file
file_obj = open(measurements_file)
file_lines = file_obj.readlines()

# extract the column names out of the file_lines and put into a list
column_names = file_lines.pop(0)
column_names = column_names.rstrip().split("\t")

# loop through data and get into respective lists
dates = []
discharge = []
stage = []
temperature = []

for line in file_lines:
	line_list = line.rstrip().split("\t")
	dates.append(line_list[0])
	discharge.append(float(line_list[1]))
	stage.append(float(line_list[2]))
	temperature.append(float(line_list[3]))

print("{}\n".format(measurements_file))
counter = 1
for parameter in [discharge, stage, temperature]:
	avg_param = sum(parameter) / len(parameter)
	
	max_param = max(parameter)
	max_param_index = parameter.index(max_param)
	max_param_date = dates[max_param_index]
	
	min_param = min(parameter)
	min_param_index = parameter.index(min_param)
	min_param_date = dates[min_param_index]
	
	print("  {}: ".format(column_names[counter]))
	print("     Average: {0:.3f}".format(avg_param))
	print("     Maximum: {} occurred on {}".format(max_param, max_param_date))
	print("     Minimum: {} occurred on {}".format(min_param, min_param_date))
	print("")
	
	counter += 1

	