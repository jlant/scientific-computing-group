names = ["Jeremiah", "Justin", "Dave", "Loren"]
group_member = "Loren"

if group_member in names:
	print("{} is already in list of names".format(group_member))
else:
	names.append(group_member)
	print("Added {} to list of names".format(group_member))

print(names)