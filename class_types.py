class small_enemy:
    health = 50
    damage = 30

    def hp_debuff(self, hex_value):
        self.health -= hex_value

    def dmg_debuff(self, hex_value):
        self.damage -= hex_value

goblin = small_enemy()

print (f"Goblin health: {goblin.health}")

hex_value = int(input("Hex value for health: "))

goblin.hp_debuff(hex_value)

print (goblin.health)

class map:

    def __init__ (self, name, dest_1, dest_2):
        self.name = name
        self.dest_1 = dest_1
        self.dest_2 = dest_2