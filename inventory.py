Inventory = {

        "Gold": 50,
        "Dagger": 1,
        "Hp potion": 3,
        
        }

Chest = {}


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

def container_overview(source):

    if source == Inventory:
        print ("\n----Inventory----\n")

    elif source == Chest:
        print ("\n------Chest------\n")

    for item in source:
        value = source[item]
        overview = f"{item}: {value}"
        print (overview)

def container_interaction(Inventory):
            
    inv_open = True
    while inv_open is True:
        player_choice = input("\n----To exit inventory, type 'Exit'----\nChest nearby! You want to store or take items?\n 'Take' or 'Store': ").capitalize()

        if player_choice == "Take":
            item_name = input("What item do you want to move?: ").capitalize()
            num_item = int(input("How many?: "))
            transfer_items(Chest, Inventory, item_name, num_item)
            container_overview(Inventory)
            container_overview(Chest)

        if player_choice == "Store":
            item_name = input("What item do you want to move?: ").capitalize()
            num_item = int(input("How many?: "))
            transfer_items(Inventory, Chest, item_name, num_item)
            container_overview(Inventory)
            container_overview(Chest)

        if player_choice == "Exit":
            inv_open = False