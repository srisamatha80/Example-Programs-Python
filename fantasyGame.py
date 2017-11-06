import pprint
def displayInventory():
	total = 0 
	for k,v in inventory.items():
		#inventory.setdefault(v,0)
		#inventory[v] += 1
		total += v
	pprint.pprint(inventory, width=1)
	print('Total items the player has: '+ str(total))

inventory = { 'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 
'arrow': 12}

displayInventory()
