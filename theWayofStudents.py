#things to do:
#actually have uses for all of the items that you find
#movement is pretty much good at this point. write in the storyline and stuff
#sort out warnings + rest
#finish up the thingy thing for the knowledge + revelations

#defines variables + globalizes some of them if they need to be referenced multiple times
global inventory
global location
global warning_lvl
global rest_lvl
global look_count
global knowledge_lvl
silver_key = False
rest_lvl = 0
warning_lvl = 0
knowledge_lvl = 0
look_count = 0
location = 0
inventory = []

#defines acceptable responses to prevent other responses
acc_yes = ["yes", "yeah", "y", "yeh", "yah", "sure", "yup"]
acc_no = ["no", "nah", "nay", "n", "fight me bitch", "nope"]
acc_look = ["look", "look around", "have a gander", "see", "try to look"]
acc_doors = ["go through doors", "doors", "door", "look at doors", "through doors", "open doors", "open", "open door", "go through door"]
acc_rest = ["rest", "relax"]
acc_inv = ["inventory"]
acc_int = ["1", "2", "3", "4", "5"]

acc_res = [acc_yes, acc_no, acc_look, acc_doors, acc_rest]
acc_responses = []
for a in acc_res:
    for b in a:
        acc_responses.append(b)

#defining the room
class Room(object):
    """Room object defines a room"""

    def __init__(self, name, number, description, door1, door2, door3, item1, item2, item3):
        """defines what the rooms are like
        name is the basic description of the room. number is a number that indicates the location of the room.
        there can be up to three doors and up to three items in a room."""

        self.name = name
        self.number = number
        self.description = description
        self.door1 = door1
        self.door2 = door2
        self.door3 = door3
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3

    def doors_list(self):
        global peep
        global warning_lvl
        lol = False
        doors = [self.door1, self.door2, self.door3]
        n = 0
        print(" ")
        for x in doors:
            if type(x) == str:
                n += 1
                print(f"{n}. {x}")
            else:
                print("\nWhich one would you like to go through?")
        print("Please type the number of the door you would like to go through.")
        while lol == False:
            subpeep = input("::: ")
            if subpeep not in acc_int:
                warning()
                subpeep = input("\nThat is an unacceptable value. Please try again. \n::: ")
            else:
                peep = int(subpeep)
                if peep <= n:
                    lol = True
                else:
                    peep = input("\nThat is an unacceptable value. Please try again. \n::: ")
                    warning()

    def items_list(self):
        global knowledge_lvl
        global inventory
        items = [self.item1, self.item2, self.item3]
        clean_items = []
        n = 0
        for item in items:
            if type(item) == str:
                clean_items.append(item)
        if self.item1 in inventory:
            print("\nYou have already taken all available items in the room. A small, facetious voice in your brain tells you 'Good job!'")
        else:
            knowledge_lvl += 1
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
            print("\nYou add these items into a bag you are holding. You know that the items cannot fit for sure, yet they do.")
        eep = input("""\nWould you like to see your inventory? \n::: """).lower()
        if eep in acc_yes:
            print("\nThese are the items you currently have in your inventory.")
            for item in inventory:
                n += 1
                print(f"{n}. {item}")
        elif eep in acc_no:
            print("\nVery well. If you wish to see your inventory at any time, type in 'inventory'.""")
        else:
            warning()
        print("\nWhat would you like to do?")
        clean_items = []
        action()

    def entered(self):
        global location
        location = int(self.number)
        print(f"\nYou have entered the {self.name}")
        action()


def inventoryf():
    global inventory
    n = 0
    print("\nThese are the items you currently have in your inventory.")
    for item in inventory:
        n += 1
        print(f"{n}. {item}")
    action()


def action():
    global look_count
    global knowledge_lvl
    lol = False
    while lol == False:
        lol = True
        hehe = input("""::: """).lower()
        if look_count == 0:
            if hehe not in acc_look:
                print("""\nI am sorry, that is unacceptable. Please try again.""")
                lol = False
            else:
                knowledge_lvl += 1
                look()
        else:
            knowledge_lvl += 1
            if hehe in acc_look:
                look()
            elif hehe in acc_doors:
                doors()
            elif hehe in acc_rest:
                rest()
            elif hehe in acc_inv:
                inventoryf()
            else:
                knowledge_lvl -= 1
                print("""\nI am sorry, that is unacceptable. Please try again.""")
                lol = False

def look():
    global look_count
    global location
    look_count += 1
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

def revelation():
    global knowledge_lvl
    if knowledge_lvl == 10:
        print("""Hello? You do realize that there's actually a person talking to you here, right? \nDon't try and talk to me though -- we'll both die if you end up doing that. \nTrust me, I was once like you. I wish I could tell you it gets better, but it doesn't really.""")
        knowledge_lvl += 2
    else:
        return None

def warning():
    global warning_lvl
    global knowledge_lvl
    warning_lvl += 1
    if warning_lvl == 1:
        print("""It is absolutely ridiculous that you can manage to do such a thing as mess up a number. Quite frankly, I am ashamed. \nI tried rebelling like that before too, you know. Didn't really work out well for me or anyone else involved. \nDare to do that again, and trust me, there will be many consequences.""")
        knowledge_lvl += 1
    elif warning_lvl == 2:
        print("""Let's not try to push it anymore, yeah? Trust me, it's takng all of my strength not to do so. \nYou do realize that you won't just get yourself in trouble, you'll get me in trouble too, right? \nIt's like hell in here, and you're seriously only making things worse for my life. I can't stand it.""")

#def rest():

def startgame():
    print("""You are currently in the entrance of what appears to be an old castle. \nUnfortunately, you do not appear to remember anything of your past. \nSomething very cold and wet drips upon your head, and you feel a headache incoming. \nWhat would you like to do? \n \n(TIP: try to make your commands as short as possible. \nFor example, instead of typing 'open door', simply type 'door'.)""")
    action()

def doors():
    if location == 0:
        entrance.doors_list()
        if peep == 1:
            hall_2.entered()
        elif peep == 2:
            room_1.entered()
        elif peep == 3:
            hall_1.entered()
    elif location == 1:
        hall_1.doors_list()
        if peep == 1:
            entrance.entered()
        elif peep == 2:
            room_3.entered()
    elif location == 2:
        hall_2.doors_list()
        if peep == 1:
            entrance.entered()
        elif peep == 2:
            room_2.entered()
    elif location == 3:
        room_1.doors_list()
        if peep == 1:
            entrance.entered()
        elif peep == 2:
            room_4.entered()
        elif peep == 3:
            room_5.entered()
    elif location == 4:
        room_2.doors_list()
        if peep == 1:
            hall_2.entered()
        elif peep == 2:
            room_5.entered()
    elif location == 5:
        room_3.doors_list()
        if peep == 1:
            hall_1.entered()
        elif peep == 2:
            room_4.entered()
    elif location == 6:
        room_4.doors_list()
        if peep == 1:
            room_1.entered()
        elif peep == 2:
            room_2.entered()
        elif peep == 3:
            hall_3.entered()
    elif location == 7:
        room_5.doors_list()
        if peep == 1:
            room_1.entered()
        elif peep == 2:
            room_2.entered()
        elif peep == 3:
            hall_3.entered()
    elif location == 8:
        hall_3.doors_list()
        if peep == 1:
            room_3.entered()
        elif peep == 2:
            room_5.entered()
        elif peep == 3:
            endgame()

#def endgame():


X = 1
#defining rooms
entrance = Room("Entrance", "0", "There are three doors: one to your left, one to the front, and one to your right. A torch dimly lights the entrance. \nFrom somewhere above, you think that you hear a scream.", "Left Door", "Center Door", "Right Door", "torch", "silver key", X)
hall_1 = Room("First Hall", "1", "You see one door down the rest of the hallway. There is also a door back to where you had just come from. \nThere is a chest on the floor, which upon first glance, is locked. Thanks to the torch, you have a general idea of the room.", "Door to the Entrance", "Door Marked 3", X, "spinach", "diamond key", X)
hall_2 = Room("Second Hall", "2", X, "Door to the Entrance", "Door Marked 2", X, "egg", "silver orb", X)
room_1 = Room("First Room", "3", X, "Door to the Entrance", "Door Marked 4", "Door Marked 5", "chicken", "pepper", X)
room_2 = Room("Second Room", "4", X, "Door Marked Hall-2", "Door Marked 5", X, "golden key", X, X)
room_3 = Room("Third Room", "5", X, "Door Marked Hall-1", "Door Marked 4", "Door Marked Hall-3", "spider", X, X)
room_4 = Room("Fourth Room", "6", X, "Door Marked 1", "Door Marked 3", X, X, X, X)
room_5 = Room("Fifth Room", "7", X, "Door Marked 1", "Door Marked 2", "Door Marked Hall-3", X, X, X)
hall_3 = Room("Third Hall", "8", X, "Door Marked 3", "Door Marked 5", "Stairwell", X, X, X)