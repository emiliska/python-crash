favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

# print("Sarah's favorite language is " +
#	favorite_languages['sarah'].title() +
#	".")

# loop through the dictionary
for name, language in favorite_languages.items():
	print(
		name.title() 
		+ "'s favorite language is " 
		+ language.title() 
		+ "."
	)

# alternative way to loop through a dictionary
# note: for funsises, .keys() is the default when looping through a dictionary
#	and as such, technically, .keys() need not be specified
#	however, ofc it is good for code clarity
# print out the keys in the dictionary
for name in favorite_languages.keys():
	print(name.title())
# print out the values in the dictionary
for language in favorite_languages.values():
	print(language.title())

# use dictionary look to greet and ACK user favorite language
# use a list to search through the dictionary
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() +
			", I see your favorite language is " +
			favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

# looping through a dictionary's keys in order

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

# looping through all values in a dictionary
# does not check for repeats
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

# to see values, no repeated we use a set
print("\nThe following languages have been mentioned: ")
for language in set(favorite_languages.values()):
	print(language.title())

