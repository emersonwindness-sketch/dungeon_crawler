# -- Instructions on how to create items, consumables and keys.

class Items:
    def __init__(self, name, weight, value, quantity):
        self.name = name
        self.weight = weight
        self.value = value
        self.quantity = quantity

    def copy (self, amount):
        return type(self)(self.name, self.weight, self.value, amount)
       
class Consumables(Items):
    def __init__(self, name, weight, value, quantity, amount):
        super().__init__(name, weight, value, quantity)
        self.amount = amount

class Currency(Items):
    def __init__ (self, name, weight, value, quantity):
        super().__init__(name, weight = 0.0, value = value, quantity = quantity)

# -- Player starting kit -- #

starting_player_items = {

    "Gold": Currency("Gold", 0, 1, 50),
    "Dagger": Items("Dagger", 0.50, 0, 1),
    "Lamp": Items("Lamp", 1.50, 1, 1),
    "Broken lamp": Items("Broken lamp", 2.0, 0, 1)

}

trader_inventory = {
    
    "Key": Items("Key", 0, 30, 2),
    "Crown": Items("Crown", 2, 100, 1),
    "Restored lamp": Items("Restored Lamp", 4, 10, 1)

}
