pokemon = ['pikachu', 'hunter', 'warturtle']

# test for equality
print("Is pokemon[0] == 'pikachu'? I predict true.")
print(pokemon[0] == 'pikachu')
print("Is pokemon[1] == 'gangar'? I predict false.")
print(pokemon[1] == 'gangar')

# test for inequality
print("Is pokemon[2] != 'gangar'? I predict true.")
print(pokemon[2] != 'gangar')

# test using the lower() function
pokemon.append('MEW')
print("Is pokemon[3].lower() == mew? I predict true.")
print(pokemon[3].lower() == 'mew')

# numerical tests involving equality and inequality
print("The following tests will all be true:")
print(2 + 5 == 7)
print(2 + 5 != 6)

# numerical tests involving less than and greater than
print(2 > 1)
print(1<2)

# numerical tests involving less than or equal to, greater than or equal to
print(2>=2)
print(2<=2)

# testing using the 'and' keyword and the 'or' keyword
# test whether an item is in a list
print('pikachu' in pokemon and 'warturtle' in pokemon)
print('pikachu' in pokemon or 'gangar' in pokemon)

# test whether an item in not in a list
print('gangar' not in pokemon)
