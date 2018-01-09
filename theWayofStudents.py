global inventory
global location
global warning_lvl
global rest_lvl
global look_count
rest_lvl = 0
warning_lvl = 0
knowledge_lvl = 0
location = 0
look_count = 0
inventory = []

#defines acceptable responses to prevent other responses
acc_yes = ["yes", "yeah", "y", "yeh", "yah", "sure"]
acc_no = ["no", "nah", "nay", "n", "fight me bitch"]
acc_look = ["look", "look around", "have a gander", "see", "try to look"]
acc_doors = ["go through doors", "doors", "door", "look at doors", "through doors", "open doors", "open", "open door", "go through door"]
acc_rest = ["rest", "relax"]
acc_inv = ["inventory"]

acc_res = [acc_yes, acc_no, acc_look, acc_doors, acc_rest]
acc_responses = []
for a in acc_res:
    for b in a:
        acc_responses.append(b)

#defining the room
class Room(object):
    """Room object defines a room"""

    def __init__(self, style, number, description, door1, door2, door3, item1, item2, item3):
        """defines what the rooms are like
        style is the type of room and description. number is a number that indicates the position of the room.
        there can be up to three doors and up to three items in a room."""

        self.style = style
        self.number = number
        self.description = description
        self.door1 = door1
        self.door2 = door2
        self.door3 = door3
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3

    def doors_list(self):
        doors = [self.door1, self.door2, self.door3]
        n = 0
        for x in doors:
            if type(x) == str:
                n += 1
                print(f"{n}. {x}")
            else:
                print("Which one would you like to go through?")
        print("Please type the number of the door you would like to go through.")

    def items_list(self):
        items = [self.item1, self.item2, self.item3]
        clean_items = []
        n = 0
        for item in items:
            if type(item) == str:
                clean_items.append(item)
        if clean_items[0] in inventory:
            print("\nYou have already taken all available items in the room. A small, facetious voice in your brain tells you 'Good job!'")
        else:
            if len(inventory) <= 6:
                print(f"\nNow that you have taken a good look around, you catch sight of many items around you. \nAlmost as though they were conveniently placed for you to find (isn't that bizarre?), you see a:")
            elif len(inventory) > 6 and len(inventory) <= 12:
                print(f"\nNow that you have taken a good look around, you catch si -- weird. \nIt's almost as though you've just thought that before, and multiple times at that. \nNevermind. Regardless, you see a:")
            elif len(inventory) > 12 and len(inventory) <= 18:
                print(f"\nNow that you have -- this is really strange. I know that I'm narrating to you, but this is really strange. \nYou seem awfully regimented. Anyway, just take these items, yeah?")
            elif len(inventory) > 18:
                print(f"\nYou feel tempted to comment on taking a good look around. \nInstead, you just see the items. You take them. \nNow, you have just added these items to your inventory:")
            for item in clean_items:
                print("     ", item)
                inventory.append(item)
            print("\nYou add these items into a bag you are holding. For sure, you know that the items cannot fit, yet they do.")
        eep = input("""\nWould you like to see your inventory? \n::: """).lower()
        if eep in acc_yes:
            print("These are the items you currently have in your inventory.")
            for item in inventory:
                n += 1
                print(f"{n}. {item}")
        elif eep in acc_no:
            print("Very well. If you wish to see your inventory at any time, type in 'inventory'.""")
        print("What would you like to do?")
        clean_items = []
        action()

    def inventory():
        n = 0
        print("These are the items you currently have in your inventory.")
        for item in inventory:
                n += 1
                print(f"{n}. {item}")

def action():
    lol = False
    while lol == False:
        lol = True
        hehe = input("""::: """).lower()
        if look_count == 0:
        #THIS DOESN'T WORK PLS FIX
            if hehe not in acc_look:
                print("""I am sorry, that is unacceptable. Please try again.""")
                lol = False
            else:
                look()
        else:
            if hehe in acc_look:
                look()
            elif hehe in acc_doors:
                doors()
            elif hehe in acc_rest:
                rest()
            elif hehe in acc_inv:
                inventory()
            else:
                print("""I am sorry, that is unacceptable. Please try again.""")
                lol = False

def look():
    lookcount += 1
    if location == 0:
        print(entrance.description)
        entrance.items_list()
    elif location == 1:
        print(hall_1.description)
        hall_1.items_list()
    elif location == 2:
        print(hall_2.description)
        hall_2.items_list()
    elif location == 3:
        print(room_1.description)
        room_1.items_list()
    elif location == 4:
        print(room_2.description)
        room_2.items_list()
    elif location == 5:
        print(room_3.description)
        room_3.items_list()
    elif location == 6:
        print(room_4.description)
        room_4.items_list()
    elif location == 7:
        print(room_5.description)
        room_5.items_list()
    elif location == 8:
        print(hall_3.description)
        hall_3.items_list()

#def warning():

#def rest():

def startgame():
    print("""You are currently in the entrance of what appears to be an old castle. \nUnfortunately, you do not appear to remember anything of your past. \nSomething very cold and wet drips upon your head, and you feel a headache incoming. \nWhat would you like to do? \n \n(TIP: try to make your commands as short as possible. \nFor example, instead of typing 'open door', simply type 'door'.)""")
    action()

#def hall1():

#def hall2():

#def room1():

#def room2():

#def room3():

#def room4():

#def room5():

#def hall3():

X = 1
#defining rooms
entrance = Room("room", "0", "There are three doors: one to your left, one to the front, and one to your right. A torch dimly lights the entrance. \nFrom somewhere above, you think that you hear a scream.", "Left Door", "Center Door", "Right Door", "torch", "silver key", X)
hall_1 = Room("hallway", "1", X, "Door to the Entrance", "Door Marked 3", X, X, X, X)
hall_2 = Room("hallway", "2", X, "Door to the Entrance", "Door Marked 2", X, X, X, X)
room_1 = Room("room", "3", X, "Door to the Entrance", "Door Marked 4", "Door Marked 5", X, X, X)
room_2 = Room("room", "4", X, "Door Marked Hall-2", "Door Marked 5", X, X, X, X)
room_3 = Room("room", "5", X, "Door Marked Hall-1", "Door Marked 4", "Door Marked Hall-3", X, X, X)
room_4 = Room("room", "6", X, "Door Marked 1", "Door Marked 3", X, X, X, X)
room_5 = Room("room", "7", X, "Door Marked 1", "Door Marked 2", "Door Marked Hall-3", X, X, X)
hall_3 = Room("hallway", "8", X, "Door Marked 3", "Door Marked 5", "Stairwell", X, X, X)