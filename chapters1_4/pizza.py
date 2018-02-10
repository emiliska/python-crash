pizza = ['pepperoni', 'cheese', 'sausage']
friends_pizza = pizza[:]
friends_pizza.append('veggie')
print("My pizzas:")
for i in pizza:
	print("\t" + i)
print("My friend's pizzas:")
for i in friends_pizza:
	print("\t" + i)
