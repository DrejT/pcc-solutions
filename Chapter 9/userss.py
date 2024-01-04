class Users:
	def __init__(self,first_name,last_name,email,passkey):
		'''user description'''
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.passkey = passkey
		self.login_attempts = 0
	
	def describe_user(self):
		'''print user details'''
		print(self.first_name)
		print(self.last_name)
		print(self.email)
		print(self.passkey)
		
	def greet_user(self):
		'''greeting a user'''
		print(f"Hello " + self.first_name+" "+self.last_name+"!")
		
	def increment_login_attempts(self):
		'''increments login attempts'''
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		'''resets login attempt to 0'''
		self.login_attempts = 0
		
#creating an instance of class Users
user = Users("Vivek","Patel","v8383!ndne9@gmail.com","password")
#calling the method using class instance
user.describe_user()
user.greet_user()

print("\n")
#creating another instance of class Users
meow = Users("Drej","Tolvel","nowhut#hmsma","1245567")
#calling method using class instance
meow.describe_user()
meow.greet_user()

#**************************
kev = Users("keviv", "twice", "82✓|{`✓%✓@bdjwmail.com", "£829#)@3(")
kev.increment_login_attempts()
kev.increment_login_attempts()
kev.increment_login_attempts()
print(kev.login_attempts)
kev.reset_login_attempts()
print(kev.login_attempts)
kev.increment_login_attempts()
print(kev.login_attempts)
print("\n")

#Inheritance

class Admin(Users):
	'''creating a child class'''
	def __init__(self, first_name, last_name, email, passkey):
		super().__init__(first_name, last_name,email, passkey)
		self.privileges = Privileges()

class Privileges:
	def __init__(self, privileges =[]):
		self.privileges = privileges
	def show_privilege(self):
		'''prints privileges'''
		if self.privileges:
			for privileges in self.privileges:
				print(privileges)
		else:
			print("user has no privileges")

users_privileges = Admin("Drej","TolVel","$=${¥¶¶$∆@maol.com","3+82(#!")
users_privileges.describe_user()
users_privileges.privileges.show_privilege()
users_privileges.privileges.privileges = ["user is an admin"]
users_privileges.privileges.show_privilege()