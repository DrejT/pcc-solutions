#deli
sandwich_orders = ["plain sandwich","chicken sandwich","paneer sandwich","plain sandwich"]

orders_done = []

while sandwich_orders:
	for sandwich in sandwich_orders:
		order = sandwich_orders.pop()
		print(f"your {sandwich} is ready!")
		orders_done.append(order)


print(orders_done)
orders_done.reverse()
print(orders_done)
orders_done.sort(reverse= True)
print(orders_done)


#pastrami sandwich

sandwich_orders.append("pastrami sandwich")
sandwich_orders.append("chicken sandwich")
sandwich_orders.append("pastrami sandwich")
sandwich_orders.append("pastrami sandwich")
print("sorry we are not taking pastrami sandwich orders for now")
while "pastrami sandwich" in sandwich_orders:
				sandwich_orders.remove("pastrami sandwich")
				
while sandwich_orders:
				for sandwich in sandwich_orders:
					done = sandwich_orders.pop()
					print(f"your {sandwich} is read!")
					orders_done.append(done)
					
print(sandwich_orders)
print(orders_done)

#poll


prompt = "If you could visit one place on earth what would it be?\n"
nprompt = "what is your name?\n"
cprompt= "is there anyone else who would you like to give this poll?(yes/no)\n"
records = {}
active = True
while active:
		name = input(nprompt)
		place = input(prompt)
		records[name] = place
		cont = input(cprompt)
		if cont == "no":
			active = False

for names,places in records.items():
	print(f"{names} loves {places}")ces}")