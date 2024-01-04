#pizza 
'''
topping= "enter your toppings:"
topping += "\ntype 'quit' to exit: "
message = " "
while topping != "quit":
	message = input(topping)
	if message!="quit":
		print(f"\nadding {message} to your order")
	else:
		break

#movie tickets

intro = ("Enter your age\n")
intro += ("type 'quit' to exit: ")
age = " "

while age !="quit":
	age = input(intro)
	if age == "quit":
		break
	else:
		age = int(age)
		if age < 3:
			print("no charges applicable")
		elif age < 12:
			print("10$")
		else:
			print("15$")

#Three fairs

friends = ["Atharva","Aditya"]
prompt = "type 'quit' to exit\n"
prompt = "can you guess my friends name?"
name = " "

while name != "quit":
	name = input(prompt)
	if name == "quit":
		break
	else:
		for friend in friends:
			if friend == name.title():
				print("that's my friend")
				break
			elif friend != name.title():
				continue
'''
#flags 
flag = 8
flag = int(flag)
add = 0
add = int(add)
sec = " "
while flag:
		sec = input("enter the number to add: ")
		add = flag + int(sec)
		if add % 10 == 0 :
			print("The flag is now a multiple of 10!!")
			break
		else:
			print("try again")
			continue
		y again")
			continue
		