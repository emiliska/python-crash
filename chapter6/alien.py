# definied dictionary alien_0
#alien_0 = {'color': 'green', 'points': 5}

# print out dictionary alien_0
#print(alien_0['color'])
#print(alien_0['points'])

# example of point-tracking technique
#new_points = alien_0['points']
#print("You just earned " + str(new_points) + " points!")

# example of tracking position
#print(alien_0)
#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)

# undefined dictionary alien_0
#alien_0 = {}
# populate alien_0 dictionary afer initialization ^
#alien_0['color'] = 'green'
#alien_0['points'] = 5

#print(alien_0)

# modifying values in a dictionary
#print("The alien is " + alien_0['color'] + ".")

#alien_0['color'] = 'yellow'
#print("The alien is now " + alien_0['color'] + ".")

# NESTING

#alien_0 = {'color': 'green', 'points':5}
#alien_1 = {'color': 'yellow', 'points':10}
#alien_2 = {'color': 'red', 'points':15}

#aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
#	print(alien)
	
aliens = []

for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
	
# show first 5 aliens
for alien in aliens[:5]:
	print(alien)
print("...")

# show total created aliens
print("Total number of aliens: " + str(len(aliens)))