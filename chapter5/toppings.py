#requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']
requested_toppings = []
#if requested_toppings != 'anchovies':
#	print("Hold the anchovies!")

#if 'mushrooms' in requested_topping:
#	print("Adding 'mushrooms'")
#if 'pepperoni' in requested_topping:
#	print("Adding 'pepperoni'")
#if 'extra cheese' in requested_topping:
#	print("Adding extra cheese.")

if requested_toppings:
	for requested_topping in requested_toppings:
		if requested_topping == 'green peppers':
			print("Sorry, we are out of green peppers!")
		else:
			print("Adding " + requested_topping + ".")

	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")
