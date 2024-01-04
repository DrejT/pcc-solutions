cities = ["Mumbai","Pune","vasai","nagpur","kolhapur"]
print(cities[0])
#remove
cities.remove("Mumbai")
print(cities)
#insert
cities.insert(0,"Mumbai")
print(cities)
#del
del cities[2]
print(cities)
#pop
city = cities.pop(3)
print(cities)
print(city)

#sort
cities.sort()
print(cities)
#sorted
print("new")
print(sorted(cities))
#reverse
cities.reverse()
print(cities)
print("\n")
#reverse sorting
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)

#length of lists
print(len(cities))
