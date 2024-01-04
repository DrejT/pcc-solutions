#creating a persons dictionary
person ={
	"first_name": "Vivek",
	"last_name": "Patel",
	"city": "Vasai"
}
print(person["first_name"])

#favourite numbers
fav = {
	"vivek": 1,
	"atharva": 5,
	"aditya": 7
}

print(f"Aditya's favourite number is {fav['aditya']}!\n")

#Creating glossary

glossary = {
	"print": "used to print something",
	"for": "used to iterate",
	"list": "used to store values that can be edited",
	"tuples": "used to store values just like a list but cannot be edited, instead the whole tuple has to be assigned new set of values",
	"dictionaries": "used to store data i key-value pairs"
}
#LOOPING THROUGH DICTIONARIES
for key,value in glossary.items():
	print(f"{key} is {value}\n")
	

#RIVERS
rivers = {
	"Ganga": "Bharat",
	"Nile": "Egypt",
	"Brahmaputra": "India"
}
#looping through keys and values
for river,country in rivers.items(): 
	print(f"The {river} river flows in {country}")
#looping through keys only
for river in rivers.keys():
	print(river)
#looping though values only
for country in rivers.values():
	print(country)
print("\n\n")
#Polls
language = {
	"atharva": "python",
	"parth": "java",
	"sahil": "java",
	"karan": "c++",
}

friends = ["aditya","atharva","kaushal","sahil","parth","karan"]
#check if friend has taken poll or not
for name in friends:
	if name not in language:
		print(f"Hey {name}, please take the poll!")
	else:
		print(f"{name} thanks for taking the poll")
		