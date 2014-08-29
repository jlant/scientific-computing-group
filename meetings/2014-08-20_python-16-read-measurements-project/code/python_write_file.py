# writing line by line - f.write()
f = open("test.txt", "w")
f.write("Hello everybody!\n")
f.write("This is fun, right?")
f.close()

# writing lines to a file - f.writelines()
my_lines = ["go cats!\n", "go cornhuskers!\n", "go cardinals!"]
f = open("cheers.txt", "w")
f.writelines(my_lines)
