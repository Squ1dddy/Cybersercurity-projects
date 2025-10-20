class Item:
    def __init__(self, item_name, item_description):
        self.name = item_name
        self.description = item_description
        self.durability = None

    def set_description(self, description):
        self.description = description
    
    def get_description(self):
        return self.description
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_durability(self, durability):
        self.durability = durability
    
    def get_durability(self):
        return self.durability

    def describe(self):
         print("You found a " + self.name + "! " + self.description)
        
    def inspect(self):
        print("This item doesnt have durability")


# WEAPON CLASS
class Weapon(Item):
    def __init__(self, item_name, item_description, damage):
        super().__init__(item_name, item_description)
        self.damage = damage
        self.weapon = True
        
    
    def set_damage(self, damage):
        self.damage = damage
    
    def get_damage(self):
        return self.damage
    
    def inspect(self):
        print(f"Weapon Durability is at {self.durability}")


# HEALING ITEM CLASS
class Healing(Item):
    def __init__(self, item_name, item_description, healing):
        super().__init__(item_name, item_description)
        self.healing = healing
        self.healing_item = True

    def set_healing(self, healing):
        self.healing = healing
    
    def get_healing(self):
        return self.healing


# ARMOUR CLASS
class Armour(Item):
    def __init__(self, item_name, item_description):
        super().__init__(item_name, item_description)
        self.damage_reduction = None
        self.health_increase = 0
    
    def set_health_increase(self, health_increase):
        self.health_increase = health_increase

    def set_damage_reduction(self, dmg_reduced):
        self.damage_reduction = dmg_reduced
    
    def get_damage_reduction(self):
        return self.damage_reduction
    
    def get_health_increase(self):
        return self.health_increase

    def inspect(self):
        print(f"Armour durability is at {self.durability}")

    
    
    