age = [1, 3, 5, 14, 21, 66, 1]
for i in age:
	if i < 2:
		print("baby")
	elif i <= 4:
		print("toddler")
	elif i <= 13:
		print("kid")
	elif i <= 20:
		print("teenager")
	elif i <=65:
		print("adult")
	else:
		print("elder")

