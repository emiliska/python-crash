guest = ['cathy', 'michael', 'dorothy']

for i in guest:
    message = "Hey " + i.title() + ", please come to my party!"
    print(message)

# remove guest from list and save in var
absent_guest = guest.pop(0)
err_message = "Oh no, " + absent_guest.title() + " can't make it!"
print(err_message)

# replace missing guest
guest.insert(0, 'gene')

# reprint list
for i in guest:
    message = "Hey " + i.title() + ", please come to my party!"
    print(message)

print("I have " + str(len(guest)) + " guests coming to my party!")
