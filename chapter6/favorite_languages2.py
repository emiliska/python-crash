favorite_languages = {
	'emily': 'python',
	'kent': 'golang',
	'jessica': 'python',
	'seth': 'bash',
	'alex': 'perl',	
	}

friends = ['emily', 'kent', 'april', 'brittany', 'michael', 'jessica', 'alex']

for name in favorite_languages.keys():
	print(name.title())

for name in friends:
	if name not in favorite_languages.keys():
		print(name.title() + " please take our poll!")
	else:
		print(name.title() +"'s favorite language is "
			+ favorite_languages.values()
			+ ".")

