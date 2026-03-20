Inventory = {
    
    "Bag":{
        "Gold":{"Value": 50
        },
        "Dagger":{"Value": 1
        },
        "HP Potion": {"Value: 3"
        },
    }
}

def access_inventory(access):
    access = Inventory["Bag"]
    print (access)


userinput = input("Choose something in the bag: ").capitalize()
access_inventory(userinput)


