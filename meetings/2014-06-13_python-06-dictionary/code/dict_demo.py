info_dict = {"name": "Bob", "age": 30, "height": 6, "hobbies" : ["golf", "tennis"]}

for key in info_dict.keys():
	print(key)

print("-") * 10

for values in info_dict.values():
	print(values)
	
print("-") * 10

for key, value in info_dict.items():
	print("Key {} maps to value {}".format(key, value))
	
print("-") * 10

for key, value in info_dict.iteritems():
	print("Key {} maps to value {}".format(key, value))

print("-") * 10

states = {"Kentucky": "KY", "Indiana": "IN"}
cities = {"KY": "Louisville", "IN": "Indianapolis"}

states["Ohio"] = "OH"
cities["OH"] = "Columbus"

print(states)
print(cities)

print("")
print("Abbreviation for Kentucky is: {}".format(states["Kentucky"]))
print("City in Indiana is: {}".format(cities["IN"]))

print("")
print("Kentucky has city: {}".format(cities[states["Kentucky"]]))

