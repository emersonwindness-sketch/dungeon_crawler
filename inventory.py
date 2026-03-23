Inventory = {

        "Gold":{"Value": 50
        },
        "Dagger":{"Value": 1
        },
        "HP potion": {"Value": 3
        },

        }

Chest = {}


def transfer_items(source, destination, item_name, num_item):

    if item_name not in source:
        print (f"The item '{item_name}' does not exist.\n")
        return
    if source[item_name]["Value"] <= 0:
        print (f"You have no {item_name}\n")
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


overview = ", " .join(Inventory)
