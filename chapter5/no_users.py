username = []

if username:
	for user in username:
		if user == 'admin':
			print("Welcome, admin!", end = "") 
			print("Would you like to see a status report?")
		else:
			print("ACCESS DENIED")
else:
	print("No users stored!") 
