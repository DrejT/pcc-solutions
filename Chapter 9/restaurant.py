class Restaurant:
	def __init__(self, restaurant_name,
cuisine_type):
		'''creating a restaurant method'''
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	
	def describe_restaurant(self):
		'''restaurant description'''
		print("It's a great restaurant!")
		print(self.restaurant_name)
		print(self.cuisine_type)
		
	def open_restaurant(self):
		'''restaurant status'''
		print("it's open 9am to 10pm")
		
	def set_number_served(self,serves):
		'''sets number of serves from args passed'''
		self.number_served = serves
		print(self.number_served)
		
	def increment_number_served(self,increment):
		'''increments to numbers and prints it'''
		self.increment_number = increment
		self.number_served += self.increment_number
		print(self.number_served)
		
#creating an instance of class Restaurant
restaurant = Restaurant("Samrat","Indian")

#restaurant 1
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\n")

#creating second instance of Restaurant class
restaurants = Restaurant("Ram","Multi")
#calling describe_restaurant for second instance
restaurants.describe_restaurant()

#creating 3 instance
rest = Restaurant("Sanskriti","Local")
#calling describe_restaurant method
rest.describe_restaurant()
print("\n")
print("\n")

#*******************
print(restaurant.number_served)
restaurant.number_served = 230
print(restaurant.number_served)
restaurant.set_number_served(244442)
print(restaurant.increment_number_served(20))
print("\n")

#******inheritance********
'''defining a child class'''
class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		'''Inheriting from parent class'''
		super().__init__(restaurant_name,cuisine_type)
		'''declaring a list as attribute'''
		self.flavors = ["Vanilla","Chocolate","Butter Scotch","Raj Bhog","Pista Kulfi"]
		
	def flavours_list(self):
			'''calling the list in a method'''
			print(f"This is the List of Ice Cream Flavours Available:\n {self.flavors}")

ice_cream_stand = IceCreamStand("Chilled One","Ice Cream Parlour")
ice_cream_stand.flavours_list()