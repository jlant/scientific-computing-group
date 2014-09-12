# demo of __name__
# 
# Output: 
#
# $ python module_name.py
# This program is being run by itself

# $ python
# >>> import module_name
# I am being imported from another module
# >>>

if __name__ == "__main__":
	print("This module is being run by itself")
else:
	print("This module is being imported from another module")

	
