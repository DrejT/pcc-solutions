#arbitrary args
def toppings(*toppings):
	'''looping through parameters to print all the arbitrary values'''
	for topping in toppings:
		print(f"adding {topping} to your order...")

toppings("cheese","popcorn","capsules")
toppings("chilli")
toppings("chicken","pasta")

#user profile

def build_profile(first_name,last_name,**profile):
	'''storing values from parameters to dictionary'''
	profile["first name"] = first_name
	profile["last name"] = last_name
	return profile

profile = build_profile(first_name="Vivek",last_name="Patel",location = "Vasai", field="Information technology")
print(profile)

#cars

def car(manu,mod,**car_info):
	'''Car information dictionary'''
	car_info["manufacturer"]= manu
	car_info["model name"]= mod
	return car_info

car_info = car("Tata","nano",wheels = "four", max_speed = "30 kmph")
print(car_info)