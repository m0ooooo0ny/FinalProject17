#things to do:
#actually have uses for all of the items that you find
#movement is pretty much good at this point. write in the storyline and stuff
#sort out warnings + rest
#finish up the thingy thing for the knowledge + revelations
#fix hehe/basicactions bug

#defines variables + globalizes some of them if they need to be referenced multiple times
global inventory
global location
global warning_lvl
global rest_lvl
global rest_decrease
global look_count
global knowledge_lvl
rest_lvl = 16
rest_decrease = 1
warning_lvl = 0
knowledge_lvl = 0
look_count = 0
location = 0
inventory = []
noninventory = []

#defines acceptable responses to prevent other responses
acc_yes = ["yes", "yeah", "y", "yeh", "yah", "sure", "yup"]
acc_no = ["no", "nah", "nay", "n", "fight me bitch", "nope"]
acc_look = ["look", "look around", "have a gander", "see", "try to look"]
acc_doors = ["go through doors", "doors", "door", "look at doors", "through doors", "open doors", "open", "open door", "go through door"]
acc_chest = ["look at chest", "open chest", "see chest", "inspect chest", "chest"]
acc_loom = ["look at loom", "see loom", "use loom", "loom", "inspect loom"]
acc_boiler = ["look at boiler", "see boiler", "use boiler", "feed boiler", "boiler"]
acc_stove = ["look at stove", "use stove", "see stove", "inspect stove", "stove"]
acc_bookmaker = ["look at bookmaker", "use bookmaker", "see bookmaker", "inspect bookmaker", "bookmaker", "look at book-maker", "use book-maker", "see book-maker", "inspect book-maker", "book-maker"]
acc_platter = ["look at platter", "inspect platter", "use platter", "platter"]
acc_stairwell = ["take stairwell", "stairwell", "inspect stairwell", "use stairwell", "look at stairwell"]
acc_trash = ["use trash can", "use trash", "trash can", "trash", "inspect trash can"]
acc_rest = ["rest", "relax"]
acc_inv = ["inventory"]
acc_int = ["1", "2", "3", "4", "5"]

acc_res = [acc_yes, acc_no, acc_look, acc_doors, acc_rest, acc_inv, acc_int, acc_chest, acc_loom, acc_boiler, acc_stove, acc_platter, acc_stairwell, acc_trash]
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
        global noninventory
        items = [self.item1, self.item2, self.item3]
        clean_items = []
        n = 0
        lol = True
        for item in items:
            if type(item) == str:
                clean_items.append(item)
        if self.item1 in inventory or self.item1 in noninventory or self.item2 in noninventory or self.item3 in noninventory:
            print("\nYou have already taken all available items in the room. A small, facetious voice in your brain tells you 'Good job!'")
        else:
            knowledge_lvl += 1
            if len(inventory) <= 4:
                print(f"\nNow that you have taken a good look around, you catch sight of many items around you. \nAlmost as though they were conveniently placed for you to find (isn't that bizarre?), you see a:")
            elif len(inventory) > 6 and len(inventory) <= 8:
                print(f"\nNow that you have taken a good look around, you catch si -- weird. \nIt's almost as though you've just thought that before, and multiple times at that. \nNevermind. Regardless, you see a:")
            elif len(inventory) > 8 and len(inventory) <= 12:
                print(f"\nNow that you have -- this is really strange. I know that I'm narrating to you, but this is really strange. \nYou seem awfully regimented. Anyway, just take these items, yeah?")
            elif len(inventory) > 12:
                print(f"\nYou feel tempted to comment on taking a good look around. \nInstead, you just see the items. You take them. \nNow, you have just added these items to your inventory:")
            for item in clean_items:
                print("     ", item)
                inventory.append(item)
            print("\nYou add these items into a bag you are holding. You know that the items cannot fit for sure, yet they do.")
        while lol == True:
            eep = input("""\nWould you like to see your inventory? \n::: """).lower()
            if eep in acc_yes:
                lol = False
                print("\nThese are the items you currently have in your inventory.")
                for item in inventory:
                    n += 1
                    print(f"{n}. {item}")
            elif eep in acc_no:
                lol = False
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
    global hehe
    global look_count
    global knowledge_lvl
    lol = False
    while lol == False:
        lol = True
        if look_count == 0:
            hehe = input("""::: """).lower()
            if hehe not in acc_look:
                print("""\nYou cannot see anything in the room, so you cannot do anything.""")
                lol = False
            else:
                knowledge_lvl += 1
                look()
        else:
            if location == 0:
                basicactions()
            elif location == 1:
                if hehe in acc_chest:
                    encounter()
                else:
                    basicactions()
            elif location == 2:
                if hehe in acc_chest:
                    encounter()
                else:
                    basicactions()
            elif location == 3:
                if hehe in acc_stove:
                    encounter()
                else:
                    basicactions()
            elif location == 4:
                if hehe in acc_trash:
                    encounter()
                else:
                    basicactions()
            elif location == 5:
                if hehe in acc_boiler:
                    encounter()
                else:
                    basicactions()
            elif location == 6:
                if hehe in acc_loom:
                    encounter()
                else:
                    basicactions()
            elif location == 7:
                if hehe in acc_platter:
                    encounter()
                else:
                    basicactions()
            elif location == 8:
                if hehe in acc_bookmaker or hehe in acc_stairwell:
                    encounter()
                else:
                    basicactions()

def basicactions():
    global hehe
    global knowledge_lvl
    lol = False
    while lol == False:
        hehe = input("""::: """).lower()
        lol = True
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
        action()

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
        print("""It is absolutely ridiculous that you can manage to do such a thing as mess up something that easy. Quite frankly, I am ashamed. \nI tried rebelling like that before too, you know. Didn't really work out well for me or anyone else involved. \nDare to do that again, and trust me, there will be many consequences.""")
        knowledge_lvl += 1
    elif warning_lvl == 2:
        print("""Let's not try to push it anymore, yeah? Trust me, it's takng all of my strength not to do so. \nYou do realize that you won't just get yourself in trouble, you'll get me in trouble too, right? \nIt's like hell in here, and you're seriously only making things worse for my life. I can't stand it.""")
        knowledge_lvl +=1

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

def encounter():
    global inventory
    print(" ")
    if location == 1:
        print("Upon inspection, you can see that the lock is a silver one.")
        if "silver key" in inventory:
            inventory.remove("silver key")
            noninventory.append("silver key")
            print("\nWith the silver key, you open up the chest. \nInside the chest lies a golden egg. \nYou pick it up and add it to the bag.")
        else:
            print("\nYou cannot open the chest.")
    elif location == 2:
        print("Upon inspection, you can see that the lock is made of diamond.")
        if "diamond key" in inventory:
            inventory.remove("diamond key")
            noninventory.append("diamond key")
            print("\nWith the diamond key, you open up the chest. \nInside the chest lies a pepper. \nYou pick it up and add it to the bag.")
        else:
            print("\nYou cannot open the chest.")
    elif location == 3:
        print("The first thing that you notice is that the stove is locked with a heavy gold padlock.")
        if "golden key" in inventory:
            inventory.remove("golden key")
            noninventory.append("golden key")
            print("\nWith the golden key, you undo the padlock. \nBefore you lies a stove, ready for use, with a pan on top of it.")
        else:
            print("\nYou cannot open the padlock.")
        if "golden key" in noninventory:
            ingredients = []
            if "spinach" in inventory:
                ingredients.append("spinach")
                noninventory.append("spinach")
                inventory.remove("spinach")
            if "eggs" in inventory:
                ingredients.append("eggs")
                noninventory.append("eggs")
                inventory.remove("eggs")
            if "pepper" in inventory:
                ingredients.append("pepper")
                noninventory.append("pepper")
                inventory.remove("pepper")
            print("\nYou place:")
            for item in ingredients:
                print("     ", item)
            print("in the pan.")
            if len(ingredients) < 3:
                print("\nYou still need", str(3-len(ingredients)), "ingredients")
            else:
                print("\nYou have created the superior dish, commonly eaten by a legend that went by the name of Cat or something. \nA dish of eggs, peppers (the spicy kind), and spinach. \nThe good egg dish is added to your inventory.")
                inventory.append("good egg dish")
    elif location == 4:
        x = True
        throwaway = input("You go over to the trash can and inspect it. It seems that you can throw things away. Would you like to throw something away?\n::: ")
        if throwaway in acc_yes:
            while x == True:
                x = False
                items = input("What item would you like to throw away? (type 10 if you would not like to throw an item away) \n::: ")
                if items == "10":
                    print("Very well. You are no longer at the trashcan. What would you like to do?")
                elif items not in inventory:
                    print("I am sorry, but you do not possess that item, or you spelled it incorrectly. Please try again. \n::: ")
                    x = True
                else:
                    inventory.remove(items)
                    noninventory.append(items)
                    print(f"\nYou take the {items} out and throw it into the trash can.")
                    cont = input("Would you like to remove any more items?")
                    if cont in acc_yes:
                        x = True
                    elif cont in acc_no:
                        print("\nVery well.")
                    else:
                        warning()
        if throwaway in acc_no:
            print("\nVery well.")
        else:
            warning()
    """elif location == 5:

    elif location == 6:

    elif location == 7:

    elif location == 8:"""

#def endgame():

X = 1
#defining rooms
entrance = Room("Entrance", "0", "There are three doors: one to your left, one to the front, and one to your right. A torch dimly lights the entrance. \nFrom somewhere above, you think that you hear a scream.", "Left Door", "Center Door", "Right Door", "torch", "silver key", X)
hall_1 = Room("First Hall", "1", "You see one door down the rest of the hallway. There is also a door back to where you had just come from. \nThis room is just incredibly murky, not unlike a dungeon. \nThere is a chest on the floor, which upon first glance, is locked. Thanks to the torch, you have a general idea of the room.", "Door to the Entrance", "Door Marked 3", X, "spinach", "diamond key", X)
hall_2 = Room("Second Hall", "2", "You see one door down the rest of the hallway. There is also a door back to where you had just come from. \nThis room is far murkier than the last one you were just in. \nThere is a chest on the floor, which is locked by a heavy diamond padlock. \nIt is thanks to the torch that you can see anything at all.", "Door to the Entrance", "Door Marked 2", X, "egg", "silver orb", X)
room_1 = Room("First Room", "3", "You see two doors on opposite ends of each other. There is also a door that leads to the entrance. \nThis room reeks of danger. A low mist crawls across the floor, while a chicken pecks at concrete. \nYou see a flash of movement to your left but when you look, you see nothing but a strand of a web. \nThe spider appears to have abandoned it. \nIn the middle of the floor lies a massive stove.", "Door to the Entrance", "Door Marked 4", "Door Marked 5", "chicken", "spider thread", "mist")
room_2 = Room("Second Room", "4", "This room is a complete contrast to everything that you have seen before. \nIt is just as grand as the fanciest stories you have read, and the ceiling stretches on further than should be possible. \nTwo doors are tucked as far away from each other as possible. \nA golden trash can lies in the corner.", "Door Marked Hall-2", "Door Marked 5", X, "golden key", "golden orb", "golden fabric")
room_3 = Room("Third Room", "5", "This room runs hotter than any other that you have been in thus far. \nThe answer becomes glaringly clear with the heavy boiler that sits in a corner, rattling angrily. \nIf you didn't know better, you would've thought that it was hungry. \nThere are three doors in the room.", "Door Marked Hall-1", "Door Marked 4", "Door Marked Hall-3", "spider", "blue fabric", X)
room_4 = Room("Fourth Room", "6", "The first thing that catches your sight is a gigantic loom that stretches almost all the way to the ceiling. \nA large piece of purple fabric hangs from it already. \nThere is only one door in the room besides the one that you just entered from.", "Door Marked 1", "Door Marked 3", X, "purple fabric", X, X)
room_5 = Room("Fifth Room", "7", "A large decorative platter hangs on a wooden wall. \nThere are three doors in the room, spaced purposefully away from each other.", "Door Marked 1", "Door Marked 2", "Door Marked Hall-3", "bronze orb", X, X)
hall_3 = Room("Third Hall", "8", "This room is strange to see after the brilliance you had seen before. \nIt is a call back to the haunting of the first few rooms you had been in. \nIn the room, there lies a book maker ad a stairwell.", "Door Marked 3", "Door Marked 5", "Stairwell", X, X, X)

startgame()