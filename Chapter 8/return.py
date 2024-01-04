#city country
def city_country(city,country):
	location = f"{city}, {country}"
	return location

city = city_country("Vasai","Bharat")
print(city)
city = city_country("Mumbai","Bharat")
print(city)
city = city_country("Tokyo","Japan")
print(city)

#make_album
def make_album(artist,album,num=None):
	album_dict = {}
	if num == None:
		album_dict["artist"] = artist
		album_dict["album"] = album
		return album_dict
	else:
		num = int(num)
		album_dict["artist"] = artist
		album_dict["album"] = album
		album_dict["num"] = num
		return album_dict

record = make_album("amjad","moksh")
print(record)
record = make_album("kaushiki chakraborty","salona sa sajan hai","1")
print(record)
record = make_album("Claude Debussy","Clair de lune")
print(record)

#make_album 2

while True:
	artist = input("who's your favourite music artist?")
	if artist == "q":
		break
	album =  input("your favourite album by that artist?")
	if album == "q":
		break
	profile = make_album(artist,album)
	print(profile)