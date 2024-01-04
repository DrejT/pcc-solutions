

#TUPLES CANNOT BE EDITED
menu= ("bhaji","misal","roti","chai","Vada")
for food in menu:
	print(food)

menu[0]="now"#will give error


#TUPLES CAN BE ASSIGNED NEW VALUES ONLY BY CHANGING ENTIRE VALUES
menu = ("keviv","vivek","atharva","Aditya","patel") 

for food in menu:
	print(food)