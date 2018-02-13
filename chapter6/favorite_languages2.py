favorite_languages = {
	'emily': 'python',
	'kent': 'golang',
	'jessica': 'python',
	'seth': 'bash',
	'alex': 'perl',	
	}

friends = ['emily', 'kent', 'april', 'brittany', 'michael', 'jessica', 'alex']

# loop through each element in list friends
for name in friends:
# if an element is not a key in dictionary favorite_languages
	if name not in favorite_languages.keys():
		print(name.title() + " please take our poll!")
	else:
		print(name.title() +"'s favorite language is "
				+ favorite_languages[name].title()
				+ ".")