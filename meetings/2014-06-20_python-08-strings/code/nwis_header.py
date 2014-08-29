header = """


# ---------------------------------- WARNING ----------------------------------------
# The data you have obtained from this automated U.S. Geological Survey database
# have not received Director's approval and as such are provisional and subject to
# revision.  The data are released on the condition that neither the USGS nor the
# United States Government may be held liable for any damages resulting from its use.
# Additional info: http://waterdata.usgs.gov/nwis/?provisional
#
# File-format description:  http://waterdata.usgs.gov/nwis/?tab_delimited_format_info
# Automated-retrieval info: http://waterdata.usgs.gov/nwis/?automated_retrieval_info
#
# Contact:   gs-w_support_nwisweb@usgs.gov
# retrieved: 2014-03-13 15:51:26 EDT       (vaww01)
#
# Data for the following 1 site(s) are contained in this file
#    USGS 03287500 KENTUCKY RIVER AT LOCK 4 AT FRANKFORT, KY
# -----------------------------------------------------------------------------------
#
# Data provided for site 03287500
#    DD parameter   Description
#    01   00010     Temperature, water, degrees Celsius
#    02   00060     Discharge, cubic feet per second
#    07   00065     Gage height, feet
#    22   00045     Precipitation, total, inches
#
# Data-value qualification codes included in this output: 
#     P  Provisional data subject to revision.  
#     h  Value exceeds "high" threshold.  
#     ~  Value is a system interpolated value.  
# 


"""

# convert header to lower case and strip all the white space - can do this in 2 steps
header = header.lower()
header = header.strip()
print(header)

# convert header to lower case and strip all the white space - can do this in 1 step
header = header.lower().strip()
print(header)

# count the number of occurrences of the word "usgs"
print(header.count("usgs"))

# find the total number of parameters in the header - method 1 using .find method
possible_parameters = ["discharge", "gage height", "precipitation", "turbidity", "temperature", "dissolved oxygen"]
num_parameters = 0
for param in possible_parameters:
	if header.find(param) != -1:
		num_parameters += 1
	
print(num_parameters)

# find the total number of parameters in the header - method 2 
possible_parameters = ["discharge", "gage height", "precipitation", "turbidity", "temperature", "dissolved oxygen"]
parameter_counts = []
for param in possible_parameters:
	parameters_counts.append(header.count(param))

print(parameters_counts)
print(sum(parameters_counts))
	
# find the total number of parameters in the header - method 3; kind of a hack way and will break easily if other number as tripe 0's. 
print("--")
print(header.count("000"))	