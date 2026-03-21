Inventory = {
        
    "Bag":{
        "Gold":{"Value": 50
        },
        "Dagger":{"Value": 1
        },
        "HP Potion": {"Value": 3
        },
        }
    }

Chest = {}

def access_inventory(access):
    access = ", " .join(Inventory["Bag"])
    print (access)
    #Place holder for modifying inventory.

overview = ", " .join(Inventory["Bag"])