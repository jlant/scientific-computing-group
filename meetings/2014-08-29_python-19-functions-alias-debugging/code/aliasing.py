# demo aliasing

string1 = "Jeremiah"
string2 = string1
print(string2)
string1 = "Dave"
print(string1)
print(string2)

# be careful with lists which are mutable
list1 = [2, 4, 6, 8]
list2 = list1
list1.append(10)
print(list1)
print(list2)

print("")

# 2 ways to make a copy of a list
list3 = [2, 4, 6, 8]
#list4 = list(list3)	# method 1 
list4 = list3[:]		# method 2
list3.append(10)
print(list3)
print(list4)