inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

print ("here is inventory list")

print(inventory)

print ("Now let's add a new key: pocket")

inventory['pocket'] = ''

print (inventory)

print ("Now let's add more values for pocket")

listadd = ['seashell','strange berry','lint']

inventory['pocket'] = listadd

print (inventory)

print ("removing dagger in backpack")

inventory["backpack"].remove('dagger')

print (inventory)

print ("adding 50 to gold")

inventory['gold']+=50

print (inventory)
