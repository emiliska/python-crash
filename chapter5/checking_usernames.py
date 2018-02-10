current_users = ['zlocker', 'wild', 'nantucket', 'spacezone', 'picard', 'admin']
new_users = ['april', 'lucky', 'wild', 'nantucket', 'tulips']
count = 0
for userA in new_users:
	print("checking if " + userA + " is available:")
	count = 0
	for userB in current_users:
		count += 1
		if userA.lower() == userB.lower():
			print("NOT AVAILABLE")
			count -= 1
		if count == len(current_users):
			print("USERNAME AVAILABLE")
			
