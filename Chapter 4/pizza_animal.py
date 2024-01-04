#using for loop to print pizza

pizzas = ["Plain pizza","NYC pizza","Italian Pizza"]
for pizza in pizzas:
	print(f"I like {pizza}!")
print("I really like pizza but never eaten one,but I am sure it's delicious")


#using for loop on animals
animals= ["dog","cat","cow"]
#for animal in animals:
#	print(f"A {animal} would make a great pet")
#print("these are domestic animals")

friend_pizza = pizzas[:]
pizzas.append("pepperoni pizza")
print(pizzas)
print(friend_pizza)
print("\n")
for pizza in pizzas:
	print(f"my favourite pizza is {pizza}")
for pizza in friend_pizza:
	print (f"my friend's favorite pizza is{pizza}")