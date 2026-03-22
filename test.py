Inventory = {
        
    "Bag":{
        "Gold":{"Value": 50
        },
        "Dagger":{"Value": 1
        },
        "Hp potion": {"Value": 3
        },
        }
    }

Chest = {}

loop = True

while loop is True:

    def move_inventory_to_chest(Item_name, num_items):
        
        if Inventory["Bag"][Item_name]["Value"] <= 0:
            print ("You have none of this item")
        else: 
            if Item_name in Chest:
                Chest[Item_name] += Inventory["Bag"][Item_name]["Value"][num_items]
                Chest[Item_name]["Value"] += num_items
                Inventory[Item_name]["Value"] -= num_items


            elif Item_name not in Chest:
                Chest[Item_name] = {"Value": Inventory["Bag"][Item_name]["Value"] }
                Chest[Item_name]["Value"] = num_items
                Inventory["Bag"][Item_name]["Value"] -= num_items


    player_choice = input("What item from inventory would you like to keep on your chest?\n").capitalize()
    num_items = int(input("How many do you want to move?\n"))
    move_item = move_inventory_to_chest(player_choice, num_items)

    print (f"Current items in chest: {Chest}")
    print (f"Current items in inventory: {Inventory}")
