stuff = {'rope':1, 'torch':6, 'gold coin':4, 'dagger':1, 'arrow':1}

def display_inventory(inventory):
	print("Inventory:\n")
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
	print("Total number of items: " + str(item_total))

# display_inventory(stuff)

def add_2_inventory(inventory, added_items):
	for i in added_items:
		if i in inventory:
			inventory[i] += 1
		else:
			inventory[i] = 1
	return inventory

inv = {'gold coin':42, 'rope':1}			 
dragonLoot = ['gold coin', 'dagger','gold coin','gold coin','ruby']

inv = add_2_inventory(inv, dragonLoot)
display_inventory(inv)