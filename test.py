Inventory = {
    
        "Gold":{"Value": 50
        },
        "Dagger":{"Value": 1
        },
        "Hp potion": {"Value": 3
        },

        }

Chest = {}

loop = True

while loop is True:

    def move_inventory_to_chest(Item_name, num_items):

        if Inventory["Bag"][Item_name]["Value"] <= 0:
            print ("You have none of this item")
        else: 
            if Item_name in Chest:
                Chest[Item_name]["Value"] += num_items
                Inventory["Bag"][Item_name]["Value"] -= num_items

            elif Item_name not in Chest:
                Chest[Item_name] = {"Value": Inventory["Bag"][Item_name]}
                Chest[Item_name]["Value"] = num_items
                Inventory["Bag"][Item_name]["Value"] -= num_items

    def transfer_items(source, destination, item_name, num_item):

        if item_name not in source:
            print (f"The item '{item_name}' does not exist.")
            return
        if source[item_name]["Value"] <= 0:
            print (f"You have no {item_name}")
        else:

            if item_name in destination:
                destination[item_name]["Value"] += num_item
                source[item_name]["Value"] -= num_item
                return

            if item_name not in destination:
                destination[item_name] = {"Value": 0}
                destination[item_name]["Value"] = num_item
                source[item_name]["Value"] -= num_item
                return


    source = input("You want to move your inventory or take from chest?\nMove / Take: ").capitalize()
    item_name = input("What item?").capitalize()
    num_item = int(input("How many?"))

    if source == "Move":
        source = Inventory
        destination = Chest
        transfer_items(source, destination, item_name, num_item)

    elif source == "Take":
        source = Chest
        destination = Inventory
        transfer_items(source, destination, item_name, num_item)

    print (f"Your inventory:\n {Inventory}")
    print (f"Your chest:\n {Chest} ")

