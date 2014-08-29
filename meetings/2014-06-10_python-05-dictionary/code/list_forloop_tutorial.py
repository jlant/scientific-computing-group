cities = ["Louisville", "London", "Paris", "New York", "Barcelona"]

print("{} is a great city".format(cities[2]))

print("-") * 10

print("{} is another great city".format(cities[-1]))

print("-") * 10

print("Let's do some slicing: {}".format(cities[0:3]))

print("-") * 10

cities.append("Chicago")
print("Let's append another city: {}".format(cities))

print("-") * 10

cities.sort()
print("Let's sort cities: {}".format(cities))

print("-") * 10

print("Length of cities list is: {}".format(len(cities)))

print("-") * 10

for city in cities:
	print(city)

print("-") * 10

for i in range(len(cities)):
	print(cities[i])

print("-") * 10

print("Original cities list is {}".format(cities))
new_cities = ["London", "Detroit", "Miami", "Cincinnati"]
for city in new_cities:
	if city in cities:
		print("City {} is already in list cities".format(city))
	else:
		cities.append(city)
		print("Added the city {} to the list cities".format(city))

print("Final cities list is {}".format(cities))