Inventory = {

        "Gold": 50,
        "Dagger": 1,
        "Hp potion": 3,
        }

Chest = {}

Loot = {
    "Old key": 1,
}

def transfer_items(source, destination, item_name, num_item):

    if item_name not in source:
        print (f"The item '{item_name}' does not exist.\n")
        return
    if source[item_name] <= 0:
        print (f"You have no {item_name}\n")
    else:

        if item_name in destination:
            destination[item_name] += num_item
            source[item_name] -= num_item
            if source[item_name] <= 0 and source[item_name] != "Gold":
               del source[item_name]
            return

        if item_name not in destination:
            destination[item_name] = {"Value": 0}
            destination[item_name] = num_item
            source[item_name] -= num_item
            if source[item_name] <= 0 and source[item_name] != "Gold":
               del source[item_name]
            return

def item_overview(source):
    if source == Inventory:
        print ("\n----Inventory----\n")
    elif source == Chest:
        print ("\n------Chest------\n")
    for item in source:
        value = source[item]
        overview = f"{item}: {value}"
        print (overview)

def chest_interaction(source):
    pass
        