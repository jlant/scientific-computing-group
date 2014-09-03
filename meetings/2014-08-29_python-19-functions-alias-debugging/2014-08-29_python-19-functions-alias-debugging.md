Python - Aliasing
==================

Objectives
----------

* Understand aliasing in Python

* Define debugging and debugger.


*****
Notes
-----

**aliasing** - a second name for the same piece of data; occurs when two variable names refer to the same value.

**reasons why aliasing is allowed:** Please also see [Software Carpentry - Python: Alias]

1. Having an alias for a very large list (millions of elements) is more efficient than copying it

2. You may actually want to update an existing structure in place

**debugging** – a methodical process of finding and reducing the number of bugs in a computer program thus making it 
behave as expected. 

**debugger** –  a computer program that is used to test and debug other programs.


*****
Examples
--------

	# aliasing with strings
	string1 = "Jeremiah"
	string2 = string1			# string2 is now an alias for the value Jeremiah
	print(string1)				# string1 is Jeremiah
	print(string2)				# string2 is Jeremiah; string2 points to same value as string1
	
	string1 = "Dave"			# alias is broken by assignment
	print(string1)				# string1 is Dave
	print(string2)				# string2 is Jeremiah; string2 points to different value than string1

	# aliasing with numbers
	number1 = 10
	number2 = number1			# number2 is now an alias for the value 10
	print(number1)				# number1 is 10
	print(number2)				# number2 is 10; number2 points to same value as number1
	
	number1 = 25				# alias is broken by assignment
	print(number1)				# number1 is 25
	print(number2)				# number2 is 10; number2 points to different value than number1
	
	# aliasing with lists; lists are mutable
	list1 = [2, 4, 6, 8]
	list2 = list1				# list2 is now an alias for the list [2, 4, 6, 8]
	list1.append(10)			# mutate list1 which will also mutate list2 
	print(list1)				# list1 is [2, 4, 6, 8, 10]
	print(list2)				# list2 is [2, 4, 6, 8, 10]

	# can eliminate aliasing in lists by making an explicit copy; 2 ways to copy a list
	list3 = [1, 3, 5, 7]
	list4 = list(list3)			# copy method 1 - copy list using list() function
	list3.append(9)
	print(list3)				# list3 is [1, 3, 5, 7, 9]
	print(list4)				# list4 is [1, 3, 5, 7]
	
	list5 = list3[:]			# copy method 2 - copy list using slicing
	list3.append(11)
	print(list3)				# list3 is [1, 3, 5, 7, 9, 11]
	print(list5)				# list5 is [1, 3, 5, 7, 9]
	
		
*****
References
----------

* [Software Carpentry - Python: Alias]
* [Software Carpentry - Python: Using a debugger]


[Software Carpentry - Python: Alias]:http://software-carpentry.org/v4/python/alias.html
[Software Carpentry - Python: Using a debugger]:http://software-carpentry.org/v4/python/debugger.html
