#car rentals
name = input("which car are you looking for?\n")
print(f"\nlet me check if we have {name} on sale right now.")

#restaurant seatings
intro = input("Hello friend, how many seats would your group require?\n")
intro = int(intro)
if intro > 8:
	print("Sorry friend your group will have to wait for a while")
else:
	print("Hey we have some seats vacant for you!")
	
#multiple of 10
num = input("Enter the number: ")
num = int(num)
if num % 10 == 0:
	print("it is a multiple of 10")
else:
	print("it is not a multiple of 10")

