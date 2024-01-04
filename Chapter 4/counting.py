#NUMERICAL FOR LOOPS
for numbers in range(1,21):
	print(numbers)

#one to one million
million = list(range(1,1000001))
#for numbers in million:
#	print(numbers)

#min max sum of lists
print(min(million))
print(max(million))
print(sum(million))

#print odd numbers
odd = []
for numbers in range(1,21,2):
	print(numbers)
	odd.append(numbers)
print(odd)

#print three multiples
three = [numbers for numbers in range(3,31,3)]
print(three)

#cubes
cube = [number**3 for number in range(1,11)]
print(cube)

#WORKING WITH PART OF LISTS
for numbers in cube[:3]:
	print(numbers)
	
for numbers in cube[-3:]:
	print(numbers)

for numbers in cube[3:-4]:
	print(numbers)

#