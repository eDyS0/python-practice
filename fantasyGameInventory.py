# displayInventory.py (idea from automatetheboringstuffwithpython)
# Takes an inventory (a dictionnary) and display it line by line with the total of items
# edit: added addToInvetory -- adds items to an inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(k, v)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)
