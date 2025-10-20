from cave import Room, PuzzleRoom, LockedRoom
from character import Enemy, Friend, Character
from item import Item, Weapon, Healing, Armour
import random
import os


#GLOBAL VARIABLES
DEAD = False
INVENTORY = []
WEAPON = None
MAX_HEALTH = 10
HEALTH = 10
ARMOUR = None


# SUBROUTINES

def game_state():
    print("\n")
    print("----- Room -----")
    if isinstance(current_room, PuzzleRoom) and current_room.puzzle_question != None:
        current_room.get_details()
        current_room.present_puzzle()
    elif isinstance(current_room, Room) and current_room != None:
        current_room.get_details()
        
    print("\n")

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        print(f"----- Interaction -----")
        if isinstance(inhabitant, Enemy):
            inhabitant.describe()
            print(f"{inhabitant.name} is willing to fight!")
        else:
            inhabitant.describe()
    
    item_in_room = current_room.get_item()
    if item_in_room is not None:
        print("\n")
        print("----- Item -----")
        item_in_room.describe()
        print(f"You've taken {item_in_room.name} and put it in your inventory")
        INVENTORY.append(item_in_room)
        current_room.set_item(None)
    return inhabitant
def move(current_room):
    directions = ["forward", "backwards", "right", "left"]
    found_direction = None
    for direction in directions:
        if direction in command:
            found_direction = direction
            break
    
    if found_direction:
        next_room = current_room.linked_rooms.get(found_direction)

        if isinstance(next_room, LockedRoom) and next_room.locked:
            if next_room.key in INVENTORY:
                print(f"You used {next_room.key.name} to unlock {next_room.name}.")
                next_room.unlock_room(next_room.key)
                current_room = next_room
            else:
                print(f"The {next_room.name} is locked. You need the correct key to enter.")
                cont = input("\x1B[3mPress enter to continue\x1B[0m\n")
        elif isinstance(next_room, Room) and next_room != None:
            print(f"Heading {found_direction}...")
            current_room = next_room
        else:
            print(f"Thats not a viable path {name}, try another direction")
    return current_room
def introduction():
    print("\n")
    print("Welcome to the haunted house, traveller...")
    print("What should we call you?")
    name = input("> ").capitalize()
    if name == "Beau":
        print("I appreciate trying to be me, but try something else.")
    elif name == "Nick":
        print("You wish you were a high distinction student.")
    elif "dwyer" in name.lower():
        print("Welcome sir... we've been expecting you.")
        print('Anytime you get stuck or need to know what you can do just type "help"!')
        print("to navigate simply type the direction you choose to go in")
        print(f"Best of luck out there, {name}")
        cont = input("\x1B[3mPress enter to continue\x1B[0m\n")
    else:
        print(f"hmmmm, {name}. It suits you.")
        print('Anytime you get stuck or need to know what you can do just type "help"!')
        print("to navigate simply type the direction you choose to go in")
        print(f"Best of luck out there, {name}")
        cont = input("\x1B[3mPress enter to continue\x1B[0m\n")
    return name
def fight_enemy(WEAPON, HEALTH, ARMOUR, DEAD):
    proceed = False
    if inhabitant is not None and isinstance(inhabitant, Enemy):
        updated_health = None
        if WEAPON == None:
            print(f"{name} you need to equip a weapon before you can fight!")
            fighting = False
        else:
            fighting = True
        if WEAPON.durability <= 0 or WEAPON == fist:
            WEAPON = fist
            print("Youre going to begin fighting with your fist. Id look for a weapon!")
        while fighting:
            print("\n")
            print("\x1B[3mType the number infront of the option you wish to take\x1B[0m\n")
            print("----- Fighting -----")
            print(f"1. Attack {inhabitant.name}\n2. Heal\n3. Run")
            choice = input("> ")
            print("\n")


            

            # IF THE PlAYER CHOOSES TO SWING
            if choice == "1":
                if WEAPON.durability > 0:
                    WEAPON.durability -= 1
                else:
                    print(f"Your {WEAPON.name} broke! leave the fight and equip another weapon!")
                    WEAPON = fist

                fight_result, updated_health = inhabitant.fight(WEAPON.damage, HEALTH, ARMOUR) # CALCULATE THE RESULTS AND THE PLAYER HEALTH
                HEALTH = updated_health # UPDATE HEALTH BEFORE EACH ROUND
                
                if fight_result is True:
                    print(f"Well done {name}, you won the fight against {inhabitant.name}!")
                    INVENTORY.append(inhabitant.item)
                    print(f"You took the {inhabitant.item.name} from {inhabitant.name}, its now in your inventory.")
                    print(f"Your {WEAPON.name} is at {WEAPON.durability} durability")
                    current_room.set_character(None)
                    fighting = False
                    
                elif fight_result is False or HEALTH <= 0:
                    print(f"{inhabitant.name} has defeated you!")
                    print("Game over")
                    fighting = False
                    DEAD = True

                else:
                    HEALTH = updated_health  # CHANGE HEALTH IF THE FIGHT CONTINUES ON
                    print(f"The fight isn't over, {name}! Keep going!")
                    fighting = True
                    


            # IF THE PLAYER CHOOSES TO HEAL
            elif choice == "2":
                healing = True
                while healing:
                    for item in INVENTORY:
                        if isinstance(item, Healing):
                            found = True
                    
                    
                    if len(INVENTORY) == 0:
                        print("You have no items in your inventory")
                        healing = False
                        break
                    elif found == True:
                        print("----- Inventory -----")
                        for index, item in enumerate(INVENTORY):
                            if isinstance(item,Healing): # HANDLES WEAPONS AND DAMAGE
                                print(f"{index + 1}. {item.name} - HEALING: {item.healing}")
                    else:
                        print("You have no healing items in your inventory!")
                        healing = False
                        break

                    
                    # FINDS THE ITEM TO CONSUME
                    try:
                        consume = int(input("Enter the number of the item to consume\n> "))
                        item_found = False
                        for index, item in enumerate(INVENTORY):
                            if index + 1 == consume:  
                                if isinstance(item, Healing):  # CHECK THE SELECTED ITEM WAS A HEALING ITEM
                                    healed_amount = min(item.healing, MAX_HEALTH - HEALTH)  # ENSURE THE HEAL ONLY GOES TO MAX
                                    HEALTH += healed_amount
                                    print(f"You healed for {healed_amount} HP!")  # CONFIRM THE HEAL
                                    print(f"You have {HEALTH} health remaining")
                                    item_found = True
                                    healing = False
                                    
                                else:
                                    print("That item cannot be consumed for healing.")
                                
                                break  
                                
                        if not item_found:
                            print("No Heal Occurred")  
                    except ValueError:
                        print("Invalid Number...")
                
            elif choice == "3":
                fighting = False
                print("Running away...")
                return updated_health, WEAPON, ARMOUR, DEAD
            
                
            else:
                print("Select a valid option...")
        if updated_health != None: # IF THE USER DOESNT FIGHT AT ALL DONT RETURN HEALTH UPDATE
            return updated_health, WEAPON, ARMOUR, DEAD

    else:
        print("There is no one here to fight with...")
def inv():
    if len(INVENTORY) != 0:
            print("----- Inventory -----")
            for index, item in enumerate(INVENTORY):
                if isinstance(item,Weapon): # HANDLES WEAPONS AND DAMAGE
                    print(f"{index + 1}. {item.name} - DMG: {item.damage}")
                    # ADD HEALING ITEMS!!
                elif isinstance(item, Healing): #HANDLES HEALING ITEMS AND HP REGEN
                    print(f"{index + 1}. {item.name} - HEALING: {item.healing}")
                else: # HANDLES REGULAR ITEMS.
                    print(f"{index + 1}. {item.name}")
            print("\n")
            if WEAPON == None:
                print("Weapon: None")
            else:
                print("Weapon: "  + WEAPON.name)
            print(f"Health: {HEALTH}")
            if ARMOUR != None:
                print(f"Armour: {ARMOUR.name}")
            else:
                print(f"Armour: None")
            cont = input("\x1B[3mPress enter to continue\x1B[0m\n")
                
                
            
    else:
        print("----- Inventory -----")
        print("There's nothing in your inventory...")
def talk():
    if inhabitant is not None:
            print("----- Talking -----")
            inhabitant.talk()
            cont = input("\x1B[3mPress enter to continue\x1B[0m\n")
def weapon_equip():
    if len(INVENTORY) == 0:
        print("There's nothing in your inventory to use as a weapon...")
    else:
        print("----- Inventory -----")
        for index, item in enumerate(INVENTORY):
            if isinstance(item,Weapon): # HANDLES WEAPONS AND DAMAGE
                print(f"{index + 1}. {item.name} - DMG: {item.damage}")
        try:
            unverified_weapon = int(input("Type the number in front of the weapon you wish to use...\n> "))
            selected_item = INVENTORY[unverified_weapon - 1]  # Adjust for zero-indexing

            if isinstance(selected_item, Weapon):
                print(f"Equipped {selected_item.name}")
                return selected_item
            else:
                print("Item could not be equipped as a weapon.")
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a valid number.")
def armour_equip(HEALTH, MAX_HEALTH):
    INVENTORY.append(king_armour)
    if len(INVENTORY) == 0:
            print("There's nothing in your inventory...")
    else:
        print("----- Inventory -----")
        for index, item in enumerate(INVENTORY):
            if isinstance(item,Armour): # HANDLES ARMOUR AND DAMAGE REDUCTION
                print(f"{index + 1}. {item.name} - DMG REDUCTION: {item.damage_reduction}")
        try:
            unverified_armour = int(input("Type the number in front of the armour you wish to use...\n> "))
            selected_item = INVENTORY[unverified_armour - 1]  # ZERO INDEXING

            if isinstance(selected_item, Armour) and selected_item.health_increase > 0:
                print(f"Equipped {selected_item.name}")
                health_increase = selected_item.get_health_increase()
                MAX_HEALTH += health_increase
                HEALTH += health_increase
                print(f"Your max health is now {MAX_HEALTH}!")
                return selected_item, HEALTH, MAX_HEALTH
            elif isinstance(selected_item, Armour) and selected_item.health_increase == 0:
                print(f"Equipped {selected_item.name}")
                HEALTH = 10
                MAX_HEALTH = 10
                return selected_item, HEALTH, MAX_HEALTH
            else:
                print("Item could not be equipped as armour.")
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a valid number.")




# FIRST TIME PLAYING LOOP

    introduction()
def stats():
    if isinstance(inhabitant, Character):
        inhabitant.stats()
        cont = input("\x1B[3mPress enter to continue\x1B[0m\n")
    else:
        print("Theres no one here to check their stats...")
def guess():
    if isinstance(current_room, PuzzleRoom):
            split_guess = command.split() # STORE THE GUESS IN AN ARRAY TO GRAB THE PLAYERS GUESS
            if len(split_guess) > 1: # CHECK THE PLAYER ENTERED 2 WORDS
                guess = split_guess[1]
                answer = current_room.solve_puzzle(guess)
            else:
                print("You need to input a guess... ")
                answer = False

            if answer == True:
                prize = current_room.get_prize()
                print(f"The floor opened up and revealed a {prize.name}.")
                INVENTORY.append(prize)
                print(f"Added {prize.name} to your inventory!")
    else:
        print("There is no puzzle in this room!")
def steal():
    if isinstance(inhabitant, Friend):
        if inhabitant.item == None:
            print(f"Theres nothing in {inhabitant.name}'s pockets to steal.")
        else:
            item = inhabitant.steal()
            INVENTORY.append(item)
            print(INVENTORY)
            inhabitant.item = None
    elif isinstance(inhabitant, Enemy):
        print(f"I wouldn't get close to {inhabitant.name} without expecting a fight...")
    else:
        print("Nobody is here to steal from...")
def inspect():
    for item in INVENTORY:
        if isinstance(item, Weapon) or isinstance(item, Armour):
            item.inspect()
def help_menu():
    print("----- Help Menu -----")
    print("talk - interact with character in the room\ninv - open your inventory to see items and your stats\nweapon - to equip a weapon for battle\nfight - begin fighting an enemy\nstats - view the stats of an enemy\nguess - take a guess at a puzzle, follow it with your guess\narmour - put on a piece of armour you found\nsteal - take an item from a friend")
    cont = input("\x1B[3mPress enter to continue\x1B[0m\n")          
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def setup():

    global library, corridor, mysterious_room, ominous_garden, multi_room, narrow_path, forgotten_vault, knights_hall, treasure_chambers, ghost_key, deadly_book, soul_sword, fist, magic_potion, skeleton_juice, king_armour, knight_armour, abhinav, knight, skeleton, magic_mop, WEAPON
    
    library = Room("Tomb of the Lost")
    library.set_description("a large library covered in cobwebs and books... spooky.")

    corridor = Room("Endless Hollow")
    corridor.set_description("a never ending corridor... how?")

    mysterious_room = Room("Veil of Shadows")
    mysterious_room.set_description("a dark room where only your hands are visible... why did you come in here?")

    ominous_garden = Room("Withered Grove")
    ominous_garden.set_description("a what once was a nice looking garden, now overrun with vines and scattered bones...")

    multi_room = Room("Gloaming Hall")
    multi_room.set_description("a large extending room with pathways in every direction...")

    narrow_path = Room("Thorned Passage")
    narrow_path.set_description("a tight walkway surrounded by sharp thorns... watch your step.")

    forgotten_vault = PuzzleRoom("Forgotten Vault", "You may break me, but I will never leave you. \nI reveal what is true, yet I hold only illusions. \nSpeak my name, and I shall show you.", "mirror")
    forgotten_vault.set_description("a sealed off vault, glistening diamonds and coins scatter the floors.")

    knights_hall = Room("Knights Hall")
    knights_hall.set_description("a hall covered in paintings of kings, a green glow emits from the walls.")

    treasure_chambers = LockedRoom("Treasure Chamber")
    treasure_chambers.set_description("a large room with gold details scaling the walls. Grab everything you can...")






    #Room system in movement order
    ominous_garden.link_room(mysterious_room, "forward") # MOVING INTO FIRST ROOM
    mysterious_room.link_room(multi_room, "forward") # MOVING INTO MULTI ROOM
    mysterious_room.link_room(ominous_garden, "backwards") # MOVING BACK TO GARDEN

    multi_room.link_room(corridor, "left") # LEFT FROM MULTIROOM
    multi_room.link_room(library, "forward") # MOVING FOWARD FROM MULTIROOM
    multi_room.link_room(narrow_path, "right") #RIGHT FROM MULTIROOM
    multi_room.link_room(mysterious_room, "backwards") # BACK TO MYSTERIOUS ROOM

    corridor.link_room(multi_room, "backwards") # LEAVING CORRIDOR BACK TO MULTIROOM
    library.link_room(multi_room, "backwards") # LEAVING LIBRARY BACK TO MULTIROOM
    narrow_path.link_room(multi_room, "backwards") # LEAVING NARROW PATH BACK TO MULTIROOM

    # RIGHT FROM MULTIROOM - FORGOTTEN FAULT
    narrow_path.link_room(forgotten_vault, "forward")
    forgotten_vault.link_room(narrow_path, "backwards")

    # LEFT FROM MULTIROOM - CORRIDOR
    corridor.link_room(knights_hall, "forward")
    knights_hall.link_room(corridor, "backwards")

    # FORWARD FROM MULTIROOM - LIBRARY
    library.link_room(multi_room, "backwards")
    library.link_room(treasure_chambers, "forward")

    # FORWARD FROM LIBRARY - TREASURE CHAMBER
    treasure_chambers.link_room(library, "backwards")


    #ITEM PROPERTIES
    ghost_key = Item("Ghost Key", "A fading key pulsing in your hand. I wonder what it opens?")


    #WEAPON PROPERTIES
    deadly_book = Weapon("Deadly Book", "A sharp looking book. Would be a great weapon.", 5)
    deadly_book.set_durability(7)
    soul_sword = Weapon("Soul Sword", "A glowing sword fueled by the soulds it claimed", 15)
    soul_sword.set_durability(25)
    forgotten_vault.set_prize(soul_sword)

    fist = Weapon("Fist", "Your hand and all your might", 1)
    fist.set_durability(100)
    WEAPON = fist
    #HEALING ITEMS
    magic_potion = Healing("Healing Potion", "A glowing red bottle, looks tasty.", 5)
    skeleton_juice = Healing("Skeleton Juice", "A disgusting bottle warm to the touch, its supposed to heal you?", 6)

    #ARMOUR ITEMS
    king_armour = Armour("Kings Armour", "A golden gown providing damage reduction from all attacks")
    king_armour.set_damage_reduction(2)
    king_armour.set_health_increase(0)
    king_armour.set_durability(10)


    knight_armour = Armour("Knights Armour", "A faint green glow emits from the hollow cavities")
    knight_armour.set_damage_reduction(5)
    knight_armour.set_health_increase(10)
    knight_armour.set_durability(20)

    # ITEM ALLOCATION
    multi_room.set_item(deadly_book)
    library.set_item(magic_potion)
    treasure_chambers.set_item(king_armour)
    treasure_chambers.set_key(ghost_key)






    #ENEMY PROPERTIES
    abhinav = Enemy("Abhinav", "a barely visible ghost, left to roam the halls. He looks lonely...")
    abhinav.set_conversation(f"Hello {name}, why would you come in here?")
    abhinav.set_health(15)
    abhinav.set_damage(2)
    abhinav.set_item(ghost_key)
    mysterious_room.set_character(abhinav)

    knight = Enemy("Soulless Knight", "a tall standing suit of armour, theres a faint green glow escaping from the chinks in the armour.")
    knight.set_conversation(f"Greetings {name}, i can escape my death, but you cant.")
    knight.set_health(60)
    knight.set_damage(4)
    knight.set_item(knight_armour)
    knights_hall.set_character(knight)




    #FRIENDLY PROPERTIES
    skeleton = Friend("Rattled Skeleton", "a shaken looking skeleton, hes got something to say...")
    skeleton.set_conversation(f"{name}! D-D- Do NOT go in t-t- there... \nThe Eternal Knight lays ready for combat! I-I- It's a death sentence!")
    skeleton.set_item(skeleton_juice)
    corridor.set_character(skeleton)

    magic_mop = Friend("Magic Mop", "a floating mop, dripping water from its head. \ntype 'talk' to hear what he has to say!")
    magic_mop.set_conversation(f"weclome {name}! I'm here to wish you on your journey. \nTo move around type the direction you want to go in.\nTheres lots to do here. i would type help to see everything you can do!\nGoodluck!!")
    magic_mop.set_item(magic_potion)
    ominous_garden.set_character(magic_mop)
def fight_friend(WEAPON, HEALTH):
    return inhabitant.fight(WEAPON, HEALTH)
    
    

# FIRST LOOP
name = introduction()
# ROOM SETUPS, ROOM LINKS, ENEMY, FRIEND, AND ITEM PROPERTIES
setup()

# MAIN LOOP
current_room = ominous_garden # STARTING ROOM
while DEAD == False:
    # MAIN GAME LOOP
    inhabitant = game_state()
    
    # TAKE PLAYER COMMAND
    command = input("> ").lower()
    clear_console()

    # MOVEMENT SYSTEM
    current_room = move(current_room)

    # TALKING
    if command == "talk":
        talk()
    

    # FIGHTING
    elif command == "fight":
        if isinstance(inhabitant, Enemy): # FIGHT ENEMY
            HEALTH, WEAPON, ARMOUR, DEAD = fight_enemy(WEAPON,HEALTH,ARMOUR, DEAD)
        elif isinstance(inhabitant, Friend): # FIGHT FRIEND
            if fight_friend(WEAPON, HEALTH) == True: DEAD = True


    # INVENTORY SYSTEM
    elif command == "inv":
        inv()
    

    # EQUIPPING A WEAPON
    elif command == "weapon":
        WEAPON = weapon_equip()
    

    # EQUIPPING ARMOUR
    elif command == "armour":
        ARMOUR, HEALTH, MAX_HEALTH = armour_equip(HEALTH, MAX_HEALTH) 


    # CHECKING ENEMY STATS
    elif command == "stats":
        stats()


    # HANDLES GUESSES
    elif "guess" in command.lower():
        guess()

    # HELP 
    elif command == "help":
       help_menu()    

        
    # STEALING FROM FRIENDS
    elif command == "steal":
        steal()

    # CHECKING ITEM DURABILITY
    elif command == "inspect":
       inspect()
# WHEN PLAYER IS DEAD
print("Game Over")
    
    