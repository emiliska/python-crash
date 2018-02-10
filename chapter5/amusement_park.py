age = 91
if age < 4:
	admission = 0
elif age >= 4 and age <=18:
	admission = 5
elif age < 65:
	admission = 10
else:
	admission = 5

print("The cost of admission is $" + str(admission) + ".")
