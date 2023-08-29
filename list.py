# declare a list variable
cities = ["Agartala", "pune", "Mumbai"]
print(cities)
print(type(cities))
print(cities[1])

cities.append("Nagpur")
cities.append(True)
print(cities)
cities.insert(3,"Delhi")
print(cities)

cities.pop(1)
cities.pop()
print(cities)

# Using for loop

for city in cities:
    print("the current city is:")
    print(city)
print("process complete")