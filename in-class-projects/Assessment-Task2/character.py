import os

#CHARACTER CLASS

class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
    
    # DESCRIBING THE CHARACTER

    def describe(self):
        print("You ran into " + self.name + " !")
        print( self.description )
    
    # SET WHAT THEY SAY WHEN TALKING TOO

    def set_conversation(self, conversation):
        self.conversation = conversation
    
    # TALK TO THE CHARACTER

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + "]: " + self.conversation)
        else:
            print("[" + self.name + "]: " + "...")
    
    # FIGHT THE CHARACTER

    def fight(self):
        print(self.name + " Knows your not worth it...")
        return True



# ENEMY CLASS
class Enemy(Character):

    enemies_to_defeat = 0


    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

        self.health = None
        self.damage = None
        self.item = None

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    
    def set_damage(self, damage):
        self.damage = damage
    
    def get_damage(self):
        return self.damage

    def set_health(self, health):
        self.health = health

    def get_health(self):
        return self.health

    def fight(self, player_damage, player_health, player_armour): # POLYMORPHISM EXAMPLE
        print(f"You deal {player_damage} DMG to {self.name}!")

        self.health -= player_damage  # ENEMY TAKES THE HIT FROM THE PLAYER

        if self.health <= 0:  # CHECKS IF THE ENEMY DIED
            print(f"You land the final blow on {self.name}!")
            print(f"You have {player_health} Health left!")
            return True, player_health  

        # ENEMY FIGHTS BACK ONLY IF ALIVE
        if player_armour != None:
            reduced_damage = self.damage - player_armour.damage_reduction
            player_health -= reduced_damage
            print(f"Your armour reduced the hit by {player_armour.damage_reduction}!")
            print(f"{self.name} hits you for {self.damage - player_armour.damage_reduction} DMG!")
            print(f"You now have {player_health} HP.")
            print(f"{self.name} has {self.health} HP left!")
            
        else:
            player_health -= self.damage  
            print(f"{self.name} hits you for {self.damage} DMG.")
            print(f"You now have {player_health} HP.")
            print(f"{self.name} has {self.health} HP left!")
           
        
        # WHEN THE ENEMY DIES
        if self.health <= 0:  
            print(f"You land the final blow on {self.name}!")
            
            return True, player_health

        # WHEN THE PLAYER DIES
        if player_health <= 0:  
            print(f"{self.name} lands the final blow onto you!")
            
            return False, player_health  
        
        return None, player_health  # CONTINUES FIGHT
        
    def steal(self):
        print("You steal from " + self.name)
    
    def stats(self):
        print(f"[{self.name}]: DMG: {self.damage}, HEALTH: {self.health}, ITEM: {self.item.name}")

# FRIEND CLASS
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.item = None
    
    def set_item(self, item):
        self.item = item
    
    def get_item(self):
        return self.item

    def pat(self):
        print(self.name + " pats you back!")
    
    def fight(self, WEAPON, PLAYER_HEALTH): #POLYMORPHISM EXAMPLE
        print(f"Are you sure you wish to fight {self.name}? They are a friend!")
        cont = input("1. Yes\n2. No\n> ")

        if cont == "1":
            fighting = True
            print(f"You attack with your {WEAPON.name}, dealing 0 damage?")
            print(f"{self.name} hits you for {PLAYER_HEALTH - 1} damage!!")
            print("You are on critical health! I'd escape this fight!")
        
            while fighting:
                print("1. Fight\n2.Run")
                cont = input("> ")

                if cont == "1":
                    print(f"You attack with your {WEAPON.name}, dealing 0 damage?")
                    print(f"{self.name} hits you for {PLAYER_HEALTH} damage!!")
                    print("You shouldnt hurt your friends...")
                    return True
                
                elif cont == "2":
                    print(f"[{self.name}] its too late to run away now... lets finish what you started.")
                    print(f"{self.name} hits you for {PLAYER_HEALTH} damage!!")
                    print("You shouldnt hurt your friends...")
                    return True
                
        elif cont == "2":
            print("That was the right choice...")
        else:
            print("Invalid Option")
    
    def steal(self):
        print(f"You reach down into {self.name}'s pockets and steal their {self.item.name}")
        return self.item
        
    
    def stats(self):
        print(f"[{self.name}]: DMG: 0, HEALTH: 10, ITEM:{self.item}")
        