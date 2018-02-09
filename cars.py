cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

# reverse order
cars.sort(reverse=True)
print(cars)

# this order change is permanent
print(cars)

print("Here is the original list:")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# reverse the list order permanently
cars.reverse()
print(cars)

# find length of list
message = "The list is " + str(len(cars)) + " cars long."
print(message)

