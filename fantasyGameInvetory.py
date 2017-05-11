# inventory.py (idea from automatetheboringstuffwithpython)
# Takes an inventory (a dictionnary) and display it line by line with the total of items

stuff = {'rope': 1, 'torch': 6, 'gold coin': 99, 'arrow': 25, 'bow' : 2, 'sword' : 1, 'bottle of water' : 0}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(k, v)
        item_total += v
    print("Total number of items: " + str(item_total))


displayInventory(stuff)
