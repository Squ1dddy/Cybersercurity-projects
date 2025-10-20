class Room():

    # Room initialisation method
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.previous_room = None

    # Sets a character within the room
    def set_character(self, character):
        self.character = character
    
    # Returns the character within the room
    def get_character(self):
        return self.character
    
    # Sets an item within the room
    def set_item(self, item):
        self.item = item

    # Returns the item within the room
    def get_item(self):
        return self.item

    # Returns the description of the room
    def get_description(self):
        return self.description
    
    # Links the room to another room through a direction command
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
    
    # Returns the name of the room
    def get_name(self):
        return self.name
    
    # Sets the description of the room
    def set_description(self, room_description):
        self.description = room_description
    
    # States the name and description of the room
    def describe(self):
        return f"You've entered the {self.name} it's {self.description}"
    
    def set_name(self, room_name):
        self.name = room_name

    def get_details(self):
        print(self.describe())  
        print("\n")
        print("----- Alternate Path -----")
        print("\x1B[3mType the direction you want to go in\x1B[3m")
        for direction in self.linked_rooms:
                if direction == "backwards":
                    room = self.linked_rooms[direction]
                    print("The " + room.get_name() + " is " + direction + " - PREVIOUS ROOM")
                else:
                    room = self.linked_rooms[direction]
                    print("The " + room.get_name() + " is " + direction)
    
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You cant go that way")
        return self
    

class PuzzleRoom(Room):
    def __init__(self, room_name, puzzle_question, solution):
        super().__init__(room_name)

        self.puzzle_question = puzzle_question
        self.solution = solution
        self.prize = None

    def present_puzzle(self):
        print("\n")
        print("----- Puzzle -----")
        print(f"{self.puzzle_question}")

    def describe(self): # POLYMORPHISM EXAMPLE 1
        return f"You've entered the {self.name}, It's {self.description}.\nTheres a puzzle on the floor..."
        
    def solve_puzzle(self, guess):
        if guess.lower() == self.solution.lower():
            print("You solved the puzzle!")
            self.puzzle_question = None
            return True
        else:
            print("Incorrect answer, dont give up!")
            return False
    
    def set_prize(self, prize):
        self.prize = prize
    
    def get_prize(self):
        return self.prize

class LockedRoom(Room):
    def __init__(self, room_name):
        super().__init__(room_name)
        self.key = None
        self.locked = True

    def set_key(self, key):
        self.key = key
    
    def get_key(self):
        return self.key
    
    def unlock_room(self, player_key):
        if player_key != self.key:
            print("That key cannot open this door...")
            return True
        else:
            self.locked = False
            return self.locked

    def describe(self): # POLYMORPHISM EXAMPLE 2
        return f"You've entered the {self.name}, It's {self.description}.\nTheres a lock on the door..."
