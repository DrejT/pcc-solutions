guests= ["Swami","J Sai Deepak","Dharmveer"]
print(f"{guests[0]},{guests[1]}, {guests[2]}, you are invited to dinner on Monday")

print(f"{guests[0]} will not be able to attend the dinner")

guests.remove("Swami")
guests.insert(0,"darcy")
print(guests)

print(f"Hey {guests[0]},{guests[1]} and {guests[2]},will be attending the dinner")

print("hey we have some more guests")
guests.append("Thakur")
guests.insert(0,"Chandar")
guests.insert(2,"Vivek")
print(guests)

print("due to enough space on my table there are some change in the guests list")

g = guests.pop(0)
print(f"i am sorry but we don't have enough space {g}")
G1 = guests.pop(0)
print(f"i am sorry but we don't have enough space {G1}")
G2 = guests.pop(2)
print(f"i am sorry {G2} we don't have space")
G3 = guests.pop(2)
print(f"we don't have enough space {G3} sorry for the inconvenience")
print(guests)
print(f"hey {guests} you are still invited to the dinner")
del guests[0]
print(guests)
del guests[0]
print(guests)
