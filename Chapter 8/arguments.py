#T-shirt
def make_shirt(size,message):
	'''size of Tshirt and the message'''
	print(f"The size of the shirt is {size} and the message is '{message}'")

make_shirt("36 M","Keviv was here")
print("\n")
make_shirt(message="Keviv",size="38 M")

#large shirts

make_shirt(size="large",message="I love Python")
make_shirt(size="medium",message="i love Python")
make_shirt("small", message="Nowwhut")
print("\n")

#describe_city

def describe_city(city,country):
	print(f"{city} is in {country}")

describe_city("Mumbai",country="Bharat")
describe_city("Kolkata",country="Bharat")
describe_city("New York",country="Bharat")