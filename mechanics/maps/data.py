# -- Instructions on how to create maps and npcs.

class Map:
    def __init__(self, name, description, access, has_container, container_name, has_trader, trader_name):
        self.name = name
        self.description = description
        self.access = access
        self.has_container = has_container
        self.container_name = container_name
        self.has_trader = has_trader
        self.trader_name = trader_name

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

# -- Definition to copy items and make it work with transfers.

