#pylint:disable=E0001
#SPEACIAL VALUES IN THE SAME LIST
usernames= ["keviv","drej","vivek","admin","unbej"]

for username in usernames:
	if username=="admin":
		print(f"Hello {username}, glad you are back!")
	else:
		print(f"Hello {username},welcome!")

#CHECKING IF LIST IS EMPTY OR NOT
users =[]
if users:
	print("done")
else:
	print("There are no users\n")
	
#STIMULATING A WEBSITE (IMPORTANT TO USE IN KEYWORD IN IF LOOP)
current_users= ["Vivek","Atharva","Aditya","Kaushal","Parth"]
new_users =["drej","unbej","bruh","vivek","Parth"]
current_users_low = [user.lower() for user in current_users]

for user in new_users:
	if user.lower() in current_users_low:
		print("This username is already taken")
	else:
		print("your account has been successfully registered!")
		
#Ordinal number
numbers= []

for number in range(1,10):
	numbers.append(number)
	
print(numbers)
for number in numbers:
	if number ==1:
		print(f"{number}st")
	elif number== 2:
		print(f"{number}nd")
	elif number == 3:
		print(f"{number}rd")
	else:
		print(f"{number}th")