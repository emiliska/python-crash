motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# replace element in list
motorcycles[0] = 'ducati'
print(motorcycles)

# append element to end of list
motorcycles.append('honda')
print(motorcycles)

# inserting elements into a list
motorcycles.insert(4, 'ford')
print(motorcycles)
motorcycles.insert(5, 'bmw')
motorcycles.insert(6, 'chevy')

# removing elements from list
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# pop() method to remove element
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# popping items from any position
popped_motorcycle2 = motorcycles.pop(0)
print(popped_motorcycle2)

# removing the first occurance an item by value
motorcycles.remove('honda')
print(motorcycles)

