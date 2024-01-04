#ALIEN COLOURS 1
alien_colour = "green"

if alien_colour== "green":
	print("new enemy appeared!")
	
if alien_colour=="red":
	print("you killed the boss")
	
#ALIEN COLOURS 2
alien_colour= "red"
if alien_colour=="red":
	points= 5
else:
	points=10
print(f"you just earned {points}!")


#ALIEN COLOURS 3
alien_colour="yellow"

if alien_colour=="red":
	points=1
elif alien_colour=="green":
	points=5
elif alien_colour=="yellow":
	points=10
print(f"you just earned {points}!")

#PERSONS AGE
age = 21

if age<2:
	print("baby")
elif age<4:
	print("toddler")
elif age<13:
	print("teenager")
elif age<20:
	print("adult")
else:
	print("elder")
	
#IF LISTS
fruits = ["mango","banana"]

if "apple" in fruits:
	print("it's an apple")
if "mango" in fruits:
	print("it's a mango")
if "banana" in fruits:
	print("it's a banana")
	
