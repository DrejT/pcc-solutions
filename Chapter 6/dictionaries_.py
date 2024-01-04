#looping through dictionaries inside a list

vivek = {
	"username": "keviv",
	"password": "newpass"
}
aditya = {
	"username": "adi",
	"password": "nowhere"
}
atharva = {
	"username": "destro",
	"password": "@tharv@"
}
users = [vivek,atharva,aditya]

for user in users:
	print(f"{user['username']}'s password is {user['password']}")
print("\n")
#pets

dog = {
	"animal": "dog",
	"name": "sheru",
	"age": "6",
	"owner": "Rohit"
}
cat= {
	"animal": "cat",
	"name": "kitty",
	"age": "3",
	"owner": "Riya"
}
parrot= {
	"animal": "parrot",
	"name": "piku",
	"age": "2",
	"owner": "Nikunj"
}
pets = [dog , cat, parrot]

for pet in pets:
	print(f"{pet['owner']} owns a {pet['animal']} named {pet['name']},it is {pet['age']} years old")
print("\n")
#favourite places
fav_places = {
	"Mumbai": "Vivek",
	"Boisar": "Atharva",
	"Kolhapur": "Aditya"
}

for places,names in fav_places.items():
	print(f"{names} loves {places}")

#favourite numbers
fav_num = {
	"Vivek": [2,4,7],
	"Atharva": [69,420],
	"Aditya": [7,1]
}

for name,num in fav_num.items():
	print(f"{name}'s favourite numbers are \n{num}")
	
#cities
cities = {
	"Mumbai": {
		"country": "India",
		"population": "50 lakhs",
		"fact": "It is the financial captial of India."
	},
	"london": {
		"country": "United Kingdom",
		"population": "10 lakhs",
		"fact": "It is the capital of United Kingdom."
	},
	"Delhi": {
	"country": "India",
	"population": "1 crore",
	"fact": "It is the capital of India"
	}
}

for city,data in cities.items():
	print(f"{city} is located in {data['country']}.It has a population of {data['population']}.{data['fact']}")

