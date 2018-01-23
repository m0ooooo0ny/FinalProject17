#defines variables + globalizes some of them if they need to be referenced multiple times
import random
global inventory
global location
global warning_lvl
global rest_lvl
global rest_decrease
global look_count
global knowledge_lvl
global norestcount
rest_lvl = 30                                   #if this level reaches zero, the player dies
rest_decrease = 1                               #defines how quickly rest_lvl changes
warning_lvl = 0                                 #if this level reaches above three, the player dies
knowledge_lvl = 0                               #depending on how high the value is, the player gains more and more info
look_count = 0
location = 0
norestcount = 0
inventory = []                                  #where all of the items go
noninventory = []                               #where all of the used items go (helps to check if items were already picked up)

#smaller lists for encounter functions; initially part of the function but reset each time, so here we are
global ingredients
global wools
global platter
global bookmaker
global offerings
ingredients = []
wools = []
platter = []
bookmaker = []
offerings = []

#defines acceptable responses to filter responses and also accept various other ones as opposed to only one specific one
acc_yes = ["yes", "yeah", "y", "yeh", "yah", "sure", "yup", "yep", "ye", "yee"]
acc_no = ["no", "nah", "nay", "n", "fight me b----", "nope", "nah fam"]
acc_look = ["look", "look around", "have a gander", "see", "try to look"]
acc_doors = ["go through doors", "doors", "door", "look at doors", "through doors", "open doors", "open", "open door", "go through door", "go to doors", "leave"]
acc_chest = ["look at chest", "open chest", "see chest", "inspect chest", "chest"]
acc_loom = ["look at loom", "see loom", "use loom", "loom", "inspect loom"]
acc_boiler = ["look at boiler", "see boiler", "use boiler", "feed boiler", "boiler"]
acc_stove = ["look at stove", "use stove", "see stove", "inspect stove", "stove"]
acc_bookmaker = ["look at bookmaker", "use bookmaker", "see bookmaker", "inspect bookmaker", "bookmaker", "look at book-maker", "use book-maker", "see book-maker", "inspect book-maker", "book-maker", "make book", "book maker", "inspect book maker", "look at book maker", "use book maker"]
acc_platter = ["look at platter", "inspect platter", "use platter", "platter"]
acc_stairwell = ["take stairwell", "stairwell", "inspect stairwell", "use stairwell", "look at stairwell"]
acc_trash = ["use trash can", "use trash", "trash can", "trash", "inspect trash can", "look at trash can", "look at trash"]
acc_rest = ["rest", "relax"]
acc_inv = ["inventory"]
acc_int = ["1", "2", "3", "4", "5"]
#makes a total list of acceptable responses for the action function
acc_res = [acc_yes, acc_no, acc_look, acc_doors, acc_rest, acc_inv, acc_int, acc_chest, acc_loom, acc_boiler, acc_stove, acc_platter, acc_stairwell, acc_trash]
#had to do this separate list because it acc_res didn't work
acc_responses = []
for a in acc_res:
    for b in a:
        acc_responses.append(b)

#defining the rooms
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
        """provides a list of doors based on the doors there when the class was created"""
        global peep
        global warning_lvl
        lol = False
        doors = [self.door1, self.door2, self.door3]
        n = 0
        print(" ")
        for x in doors:                         #not every room has three doors; this cleans out nonexistant doors
            if type(x) == str:
                n += 1
                print(f"{n}. {x}")
            else:
                print("\nWhich one would you like to go through?")
        print("Please type the number of the door you would like to go through.")
        while lol == False:                     #keeps cycling through the input (subpeep) until an acceptable answer is given
            subpeep = input("::: ")             #checks to make sure the input is an integer, just in string form
            if subpeep not in acc_int:
                warning()
                print("\nThat is an unacceptable value, please try again.")
            else:
                peep = int(subpeep)             #turns an acceptable input into an integer
                if peep <= n:
                    lol = True
                else:
                    warning()
                    print("\nThat is an unacceptable value, please try again.")

    def items_list(self):
        """provides a list of items in the room, and automatically adds those items to the inventory"""
        global knowledge_lvl
        global inventory
        global noninventory
        items = [self.item1, self.item2, self.item3]
        clean_items = []
        for item in items:                      #not every room has three items; this cleans out nonexistent items
            if type(item) == str:
                clean_items.append(item)
        if self.item1 in inventory or self.item1 in noninventory or self.item2 in noninventory or self.item3 in noninventory:
            #prevents items from being added to the inventory twice
            print("\nYou have already taken all available items in the room. A small, facetious voice in your brain tells you 'Good job!'")
        else:
            if len(inventory) <= 4:             #changes text display and information depending on how many items you have already gotten
                print(f"\nNow that you have taken a good look around, you catch sight of many items around you. \nAlmost as though they were conveniently placed for you to find (isn't that bizarre?), you see a:")
            elif len(inventory) > 4 and len(inventory) <= 8:
                print(f"\nNow that you have taken a good look around, you catch si -- weird. \nIt's almost as though you've just thought that before, and multiple times at that. \nNevermind. Regardless, you see a:")
            elif len(inventory) > 8 and len(inventory) <= 12:
                print(f"\nNow that you have -- this is really strange. I know that I'm narrating to you, but this is really strange. \nYou seem awfully regimented. Anyway, just take these items, yeah?")
            elif len(inventory) > 12:
                print(f"\nYou feel tempted to comment on taking a good look around. \nInstead, you just see the items. You take them. \nNow, you have just added these items to your inventory:")
            for item in clean_items:
                print("     ", item)
                inventory.append(item)
            #I used to have an automatic prompter to reveal inventory here, but my sister said that it was annoying, so I removed it
            print("\nYou add these items into a bag you are holding. You know that the items cannot fit for sure, yet they do.\n(If you wish to see your inventory at any time, type in 'inventory.')")
        print("\nWhat would you like to do?")
        action()

    def entered(self):
        """tells the player which room they just entered"""
        global location
        location = int(self.number)             #changes the location value of the room automatically
        norest()                                #each time a room is changed, sees if they need a norest prompt
        print(f"You have entered the {self.name}.")
        action()

def revelation():
    """provides additional storyline information, specifically about the narrator, depending on the amount of knowledge they have"""
    print("   ")
    global knowledge_lvl
    if knowledge_lvl == 10:
        print("""Hello? You do realize that there's actually a person talking to you here, right? \nDon't try and talk to me though -- we'll both die if you end up doing that. \nTrust me, I was once like you. I wish I could tell you it gets better, but it doesn't really. \nAnyway --""")
    elif knowledge_lvl == 20:
        print("""Look, I'm a little lonely here so I'm just going to talk to you, if that's alright with you. \nI was once like you: stressed out of my mind and trying to find any way to escape. \nAnd you are correct, this is your best method of trying to escape. \nIf you can make it to the end, that is. \nAnyway --""")
        knowledge_lvl += 1
    elif knowledge_lvl == 30:
        print("""Do you want to know who I am? I am a prisoner, a result of Magnet. \nI am meant to take students here on a chase and lure them into a sense of escape before snatching it away from them. \nAs you can see, I'm not necessarily the best at it. \nI like giving chances. Anyway --""")
        knowledge_lvl += 2
    elif knowledge_lvl == 40:
        print("""Why am I a prisoner? I am a prisoner because I failed this task. I failed this task spectacularly. \nDon't worry too much about me, this isn't my day job or anything. \nJust -- try not to fail, yeah? So let's get our heads back into the game --""")
    else:
        return None

def warning():
    """a system to punish those that put in ridiculous answers for simple questions (such as typing in a number or yes/no questions)"""
    global warning_lvl
    global knowledge_lvl
    warning_lvl += 1
    if warning_lvl == 1:
        print("""It is absolutely ridiculous that you can manage to do such a thing as mess up something that easy. Quite frankly, I am ashamed. \nI tried rebelling like that before too, you know. Didn't really work out well for me or anyone else involved. \nDare to do that again, and trust me, there will be many consequences.""")
        knowledge_lvl += 1
    elif warning_lvl == 2:
        print("""Let's not try to push it anymore, yeah? Trust me, it's takng all of my strength not to do so. \nYou do realize that you won't just get yourself in trouble, you'll get me in trouble too, right? \nIt's like hell in here, and you're seriously only making things worse for my life. I can't stand it.""")
        knowledge_lvl +=1
    elif warning_lvl == 3:
        print("""Are you really trying to take advantage of my generosity like that? Seriously? \nNext time, for sure, I will not be so kind. Anything more than 3 strikes is too much.""")
        knowledge_lvl += 1
    elif warning_lvl == 4:
        print("That is it, I can't take this anymore. It's over for you.\n")
        endgame()

def norest():
    """decreases a player's rest level each time they move from room to room
    if the rest level hits zero, they die; this also provides warnings throughout the game"""
    global rest_decrease
    global rest_lvl
    global norestcount                          #prevents continuous prompting every single time rest is below a certain value
    rest_lvl -= rest_decrease                   #because rest_decrease changes, rest_lvl changes by rest_decrease and not a static value
    print(" ")
    if rest_lvl <= 0:
        print("You grow so exhausted that you cannot move anymore. You fall to the ground and die.")
        endgame()
    elif rest_lvl <= 5 and norestcount == 3:
        print("You are barely able to push on and keep moving. I'm telling you that I'm worried. \nI would highly recommend resting, yeah?\n")
        norestcount += 1
    elif rest_lvl <= 10 and norestcount == 2:
        print("Something in your back stings a lot, and it is almost as though the world around you is going to dissolve. \nPerhaps this is a product of standing around too much and not resting, or maybe it's just your imagination.\n")
        norestcount += 1
    elif rest_lvl <= 15 and norestcount == 1:
        print("You actually collapse onto the ground for a few seconds before you are able to stand up again. \nYou wonder if you should stop and rest a little bit before continuing on.\n")
        norestcount += 1
    elif rest_lvl <= 20 and norestcount == 0:
        print("The headache that you had been feeling before is coming back even stronger. \nFor a second, your knees buckle and you worry that you won't be strong enough to carry on.\n")
        norestcount += 1
    else:
        return None

def action():
    """this is the basic action function that takes input from the user and decides what to do"""
    global hehe
    global look_count
    global knowledge_lvl
    lol = False             #I probably should've chosen a better variable name than lol, but I grew accustomed to seeing it
    while lol == False:     #because I'm generous (and don't want to get points off for academic dishonesty), credit to Damon for the loop idea that I abuse throughout this code
        lol = True
        hehe = input("""::: """).lower()        #main input receiver
        revelation()                            #runs revelation each action to see if knowledge_lvl has reached a point where new information is provided; does nothing if it does not
        if look_count == 0:                     #for the very first room, the first action must be look
            if hehe not in acc_look:
                print("""\nYou cannot see anything in the room, so you cannot do anything.""")
                lol = False
            else:
                knowledge_lvl += 1
                look()
        else:                                   #for all other rooms, no first action is necessary
            knowledge_lvl += 1
            if hehe in acc_chest and location == 1:
                encounter()
            elif hehe in acc_chest and location == 2:
                encounter()
            elif hehe in acc_stove and location == 3:
                encounter()
            elif hehe in acc_trash and location == 4:
                encounter()
            elif hehe in acc_boiler and location == 5:
                encounter()
            elif hehe in acc_loom and location == 6:
                encounter()
            elif hehe in acc_platter and location == 7:
                encounter()
            elif hehe in acc_bookmaker and location == 8:
                encounter()
            elif hehe in acc_stairwell and location == 8:
                stairwell()
            elif hehe in acc_look:
                look()
            elif hehe in acc_doors:
                doors()
            elif hehe in acc_rest:
                rest()
            elif hehe in acc_inv:
                inventoryf()
            else:
                knowledge_lvl -= 1              #prevents knowledge level from going up with invalid inputs
                print("""\nI am sorry, that is unacceptable. Please try again.""")
                lol = False

def rest():
    """increases rest_lvl by a random amount if the player chooses to rest"""
    global rest_lvl
    rest_lvl += random.randint(1,5)
    print("\nYou feel better rested than before and find it easier to continue.")
    if "chicken" in inventory or "mist" in inventory:           #provides prompt to suggest removing certain items from the inventory
        print("\nYou wonder if some of the exhaustion that you felt was due to an item that you are currently carrying. \nIt would certainly explain why you started tiring far more easily.")
    action()

def inventoryf():
    """prints the player's inventory"""
    global inventory
    n = 0
    print("\nThese are the items you currently have in your inventory.")
    for item in inventory:
        n += 1
        print(f"{n}. {item}")
    action()

def look():
    """provides a description of the room + adds items to inventory automatically"""
    global look_count
    global location
    global rest_decrease
    look_count += 1
    if location == 0:                           #I tried using a more involved class system to do this, but I couldn't figure it out
        print(entrance.description)
        entrance.items_list()
    elif location == 1:
        print(hall_1.description)
        hall_1.items_list()
    elif location == 2:
        print(hall_2.description)
        hall_2.items_list()
    elif location == 3:
        rest_decrease += 2                      #the mist and chicken are in this room, and so rest_decrease increases because they are damaging items and automatically added
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

def doors():
    """provides a list of doors in order to help with movement"""
    if location == 0:
        entrance.doors_list()
        if peep == 1:                           #peep here is referencing the doors_list() function in the class
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
        elif peep == 3:
            hall_3.entered()
    elif location == 6:
        room_4.doors_list()
        if peep == 1:
            room_1.entered()
        elif peep == 2:
            room_3.entered()
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

#upon further thought, I may have split up encounter into separate functions because I use way too many loops
#and those loops need a different variable name every single time, so that's food for thought
def encounter():
    """defines all functions revolving around more complex scenarios, such as opening a chest or feeding a boiler"""
    global inventory
    print(" ")
    if location == 1:
        print("Upon inspection, you can see that the lock is a silver one.")
        if "silver key" in inventory:               #checks to make sure that the silver key is in the inventory
            inventory.remove("silver key")
            noninventory.append("silver key")
            print("\nWith the silver key, you open up the chest. \nInside the chest lies a golden egg. \nYou pick it up and add it to the bag.")
            inventory.append("golden egg")
            action()
        elif "silver key" in noninventory:          #checks to see if chest was already opened before
            print("\nYou have already opened the chest.")
            action()
        else:
            print("\nYou cannot open the chest.")
            action()
    elif location == 2:                             #works the exact same way as above chest function
        print("Upon inspection, you can see that the lock is made of diamond.")
        if "diamond key" in inventory:
            inventory.remove("diamond key")
            noninventory.append("diamond key")
            print("\nWith the diamond key, you open up the chest. \nInside the chest lies a pepper. \nYou pick it up and add it to the bag.")
            inventory.append("pepper")
            action()
        elif "silver key" in noninventory:
            print("\nYou have already opened the chest.")
            action()
        else:
            print("\nYou cannot open the chest.")
            action()
    elif location == 3:
        global ingredients                          #ingredients have to be outside of the function because otherwise it resets each time it is called and that can't happen
        print("The first thing that you notice is that the stove is locked with a heavy gold padlock.")
        if "good egg dish" in inventory or "good egg dish" in noninventory:         #checks to make sure stove wasn't already used to full capacity
            print("\nYou have already used the stove to the full extent necessary.")
            action()
        else:
            if "golden key" in inventory:           #works same as the chest functions
                inventory.remove("golden key")
                noninventory.append("golden key")
                print("\nWith the golden key, you undo the padlock. \nBefore you lies a stove, ready for use, with a pan on top of it.")
            if "golden key" in noninventory:
                if "spinach" in inventory:          #all of these are separate if functions; adds items from inventory even if not all of them are complete
                    ingredients.append("spinach")
                    noninventory.append("spinach")
                    inventory.remove("spinach")
                if "egg" in inventory:
                    ingredients.append("egg")
                    noninventory.append("egg")
                    inventory.remove("egg")
                if "pepper" in inventory:
                    ingredients.append("pepper")
                    noninventory.append("pepper")
                    inventory.remove("pepper")
                if len(ingredients) != 0:           #if some ingredients were used
                    print("\nYou place:")
                    for item in ingredients:
                        print("     ", item)
                    print("in the pan.")
                    if len(ingredients) < 3:        #if not all ingredients were used, prints how many ingredients are still needed
                        print("\nYou still need", str(3-len(ingredients)), "ingredients")
                    else:                           #if all ingredients were used, provides the good egg dish
                        print("\nYou have created the superior dish, commonly eaten by a legend that went by the name of Cat or something. \nA dish of eggs, peppers (the spicy kind), and spinach. \nThe good egg dish is added to your inventory.")
                        inventory.append("good egg dish")
                    action()
                elif len(ingredients) == 0:         #if there are no ingredients
                    print("\nYou are lacking all of the ingredients necessary to cook a dish.\nYou still need 3 ingredients.")
                    action()
            else:
                print("\nYou cannot open the padlock.")
                action()
    elif location == 4:
        global rest_decrease
        x = True                                    #again, far too many loops
        loop = True
        while loop == True:                         #this loop is to make sure the input from "throwaway" is acceptable
            throwaway = input("You go over to the trash can and inspect it. It seems that you can throw things away. Would you like to throw something away?\n::: ")
            loop = False
            if throwaway in acc_yes:
                while x == True:                    #this loop is to make sure the input from "items" is acceptable
                    x = False
                    n = 0
                    print("\nThese are the items you currently have in your inventory.")
                    for item in inventory:          #provides list of items in their current inventory
                        n += 1
                        print(f"{n}. {item}")
                    items = input("\nWhat item would you like to throw away? \n(Please type in the item, not the number the item is associated with. \ntype 1 if you would not like to throw an item away) \n::: ")
                    if items == "1":                #allows for people to back out of throwing things away
                        print("\nVery well. You are no longer at the trashcan. What would you like to do?")
                        action()
                    elif items not in inventory:
                        print("I am sorry, but you do not possess that item, or you spelled it incorrectly. Please try again. \n::: ")
                        x = True
                    else:                           #assuming items are in the inventory
                        if items == "mist" or items == "chicken":
                            rest_decrease -= 1      #decreases the amount the rest decreases when mist or chicken (damaging items) are thrown away
                        elif items == "torch":      #one of my favorite ways that you can die
                            print("\nYou are pretty sure that you don't need the torch at this point, and you throw it away. \nHowever, immediately after you throw it away, everywhere around you is plunged into complete darkness. \nWhen you try to run to a door to find a light switch, you slip. \nYour head hits the gilded trash can and you promptly die.")
                            endgame()
                        elif items != "mist" and items != "chicken":
                            print("\nYou fool! You need to hold onto that, or else you'll never get out of here!")
                            endgame()
                        inventory.remove(items)
                        noninventory.append(items)
                        print(f"\nYou take the {items} out and throw it into the trash can.")
                        subx = True
                        while subx == True:         #this loop is to ensure that the input for "cont" is acceptable
                            subx = False
                            cont = input("Would you like to remove any more items?\n::: ")
                            if cont in acc_yes:
                                x = True
                            elif cont in acc_no:
                                print("\nVery well.")
                                action()
                            else:
                                subx = True
                                if warning_lvl == 3:
                                    subx = False
                                warning()
            if throwaway in acc_no:
                print("\nVery well.")
                action()
            else:
                loop = True
                if warning_lvl == 3:
                    loop = False
                warning()
    elif location == 5:
        if "good egg dish" in noninventory:         #prevents interacting with the boiler twice
            print("You have already dealt with the boiler, which is sitting there happily.")
            action()
        else:
            print("When you come closer to the boiler, you notice that the boiler is  hungry. \nIn fact, you're rather worried that the boiler would go and try to kill you if you crawl too close. \nWould you like to go closer?")
            ahh = False
            while ahh == False:                     #loop for when "boop" is not an acceptable input
                ahh = True
                boop = input("::: ")                #gives the choice to back away from the boiler
                if boop in acc_yes:
                    if "good egg dish" in inventory:
                        inventory.remove("good egg dish")
                        noninventory.append("good egg dish")
                        print("\nYou throw the good egg dish from your inventory into the boiler's open grid and wait anxiously. \nAfter a few tense seconds, the boiler closes and bounces up and down a few times. \nThen, the boiler quietens, burping out a pigeon feather. \nYou successfully calmed the boiler without dying.")
                        inventory.append("feather of a pigeon")
                        action()
                    elif "good egg dish" not in inventory:      #also one of my favorite ways someone can die
                        print("\nAs you are not possessing an offering the boiler desires, it launches at you. \nYou are eaten by the boiler.")
                        endgame()
                elif boop in acc_no:
                    print("\nYou make a well-timed and expeditious retreat away from the boiler.")
                    action()
                else:
                    ahh = False
                    if warning_lvl == 3:
                        ahh = True
                    warning()
    elif location == 6:
        global wools
        print("The loom reaches the ceiling, and you cannot insert the wool without help.")
        if "binding" in inventory or "binding" in noninventory: #ensures that you can't use the loom twice
            print("\nYou have already used the loom to the full extent necessary.")
            action()
        else:
            if "spider" in inventory:               #works the same way as the stove, except with more items
                inventory.remove("spider")
                noninventory.append("spider")
                print("\nThe spider deftly crawls up and down the loom, moving exactly where you want it. \nIt eagerly awaits instruction.")
            if "spider" in noninventory:
                if "spider thread" in inventory:
                    wools.append("spider thread")
                    noninventory.append("spider thread")
                    inventory.remove("spider thread")
                if "golden wool" in inventory:
                    wools.append("golden wool")
                    noninventory.append("golden wool")
                    inventory.remove("golden wool")
                if "blue wool" in inventory:
                    wools.append("blue wool")
                    noninventory.append("blue wool")
                    inventory.remove("blue wool")
                if "purple wool" in inventory:
                    wools.append("purple wool")
                    noninventory.append("purple wool")
                    inventory.remove("purple wool")
                if len(wools) != 0:
                    print("\nThe spider takes from you:")
                    for item in wools:
                        print("     ", item)
                    print("and immediately jumps on the loom in order to start weaving.")
                    if len(wools) < 4:
                        print("\nYou still need", str(4-len(wools)), "different materials in order to fully make something.")
                    else:
                        print("\nThe spider finishes its work atop the loom and drops into your hands an amount of binding. \nThe binding is that typically used on books.")
                        inventory.append("binding")
                    action()
                elif len(wools) == 0:
                    print("\nYou are lacking all of the necessary materials to fully make what you are supposed to.\nYou still need 4 different materials.")
                    action()
            else:
                print("\nYou cannot reach the loom in order to do any work. \nPerhaps if you had something that could crawl up there to help...")
                action()
    elif location == 7:                         #works the same way as the stove
        global platter
        print("The platter is very decorative and has three round spaces where you think objects are supposed to go.")
        if "paper" in inventory or "paper" in noninventory:
            print("You have already received the paper from the platter.")
            action()
        else:
            if "silver orb" in inventory:
                inventory.remove("silver orb")
                noninventory.append("silver orb")
                platter.append("silver orb")
            if "golden orb" in inventory:
                inventory.remove("golden orb")
                noninventory.append("golden orb")
                platter.append("golden orb")
            if "bronze orb" in inventory:
                inventory.remove("bronze orb")
                noninventory.append("bronze orb")
                platter.append("bronze orb")
            if len(platter) != 0:
                print("\nYou place:")
                for item in platter:
                    print("     ", item)
                print("inside the indentation within the platter. It fits perfectly.")
                if len(platter) < 3:
                    print("\nYou still need", str(3-len(platter)), "different round objects in order to fill up the platter.")
                else:
                    print("\nAll of your shiny, shiny orbs that you probably could have sold for a million dollars slide into the platter. \nThere is a spinning sound, and the platter spins around. \nFrom the resulting crevice in the wall, you see something shining. \nFor a second, you think that it's a diamond that you can sell and make tons of money off of. \nInstead, you see a ton of paper. \nDisappointment fills you, but you take the sheafs of paper regardless.")
                    inventory.append("paper")
                action()
            elif len(platter) == 0:
                print("\nYou are lacking all of the necessary orbs to fill the platter.\nYou still need 3 different orbs.")
                action()
    elif location == 8:                         #works the same way as the stove, except with less items
        global bookmaker
        print("The bookmaker seems to be built for just the purpose that it looks to be for.")
        if "Tome of Secrets" in inventory or "Tome of Secrets" in noninventory:
            print("You have used already used the bookmaker enough.")
            action()
        else:
            if "binding" in inventory:
                bookmaker.append("binding")
                inventory.remove("binding")
                noninventory.append("binding")
            if "paper" in inventory:
                bookmaker.append("paper")
                inventory.remove("paper")
            if len(bookmaker) != 0:
                print("\nYou place:")
                for item in bookmaker:
                    print("     ", item)
                print("inside the bookmaker.")
                if len(bookmaker) == 2:
                    print("\nYou wait excitedly as the bookmaker accepts the binding and paper you put inside it. \nThe bookmaker chugs away for a surprisingly short amount of time before spewing out a book. \nWhen you pick up the book, you feel complete and utter knowledge flow through you. \n/This is the Tome of Secrets/ something whispers at you.")
                    inventory.append("Tome of Secrets")
                    action()
                elif len(bookmaker) == 1:
                    print("\nAlthough you place one necessary material into the bookmaker, it still requires another one as well.")
                    action()
            if len(bookmaker) == 0:
                print("\nUnfortunately, you don't seem to have anything that you can put inside the bookmaker.")
                action()

def stairwell():
    """created a separate function for the stairwell and did not add in encounter because there were two location == 8's"""
    global offerings                        #works very similarly to the stove
    print("\nA bright pink post-it note is stuck on the wall, contrasting the more medieval settings surrounding you. \nOn it reads: \n'BRING ME THREE OBJECTS: A GOLDEN EGG, THE TOME OF SECRETS, AND THE FEATHER OF A PIGEON. \nTHEN YOU MAY LEAVE THIS PLACE.'")
    if "golden egg" in inventory:
        inventory.remove("golden egg")
        noninventory.append("golden egg")
        offerings.append("golden egg")
    if "feather of a pigeon" in inventory:
        inventory.remove("feather of a pigeon")
        noninventory.append("feather of a pigeon")
        offerings.append("feather of a pigeon")
    if "Tome of Secrets" in inventory:
        inventory.remove("Tome of Secrets")
        noninventory.append("Tome of Secrets")
        offerings.append("Tome of Secrets")
    if len(offerings) != 0:
        print("\nYou place:")
        for item in offerings:
            print("     ", item)
        print("before the stairwell as an offering.")
        if len(offerings) < 3:
            print("\nYou still need more offerings in order to leave this place.")
            action()
        elif len(offerings) == 3:
            print("\nThe stairwell accepts your offerings.")
            ending()
    elif len(offerings) == 0:
        print("\nYou possess no offerings to give the stairwell.")
        action()

def startgame():
    """initializes the game"""
    print("""You are currently in the entrance of what appears to be an old castle. \nUnfortunately, you do not appear to remember anything of your past. \nSomething very cold and wet drips upon your head, and you feel a headache incoming. \nWhat would you like to do? \n \n(TIP: try to make your commands as short as possible. \nFor example, instead of typing 'open door', simply type 'door'.)""")
    action()

def endgame():
    """if you do not beat the game, this is the ending"""
    print("\nYou float in an endless night and then jolt awake. \nYou realize that it was a fever dream that you had while asleep in class, dreaming of escape.\nGAME OVER. YOU HAVE LOST.")
    endless1()

def endless1():
    """created a separate function for this endless because it is referenced in two different areas"""
    y = True
    while y == True:
        x = input("\n::: ")
        if type(x) == str:
            print("\nYou have already failed and are stuck in Magnet hell. THere is nothing you can do.")

def ending():
    """if you beat the game, this is the true ending"""
    print("\nWhen you walk up the stairwell, the light slowly grows. \nAs soon as you pop up at the top, you see someone wearing a Magnet ID reaching out for you. \n'Come escape from your place of suffering,' they say, reaching for your hand. \nYou stare for a second before taking their hand and walking along with them on the path away from Magnet.")
    print("GAME COMPLETE")
    y = True
    count = 1
    if count < 100:
        while y == True:
            x = input("\n::: ")
            if type(x) == str:
                print("\nYou have already reached nirvana and are away from Magnet. What else would you like to do?")
                count += 1
    else:                       #if someone keeps on trying to input responses, they end up actually losing the game
        while y == True:
            x = input("\n::: ")
            if type(x) == str:
                print("\nYou could have had it all, but because of your inability to let things go, \nyou have been kicked away from nirvana. \nGAME OVER. YOU HAVE LOST.")
                endless1()

#placeholder value
X = 1
#defines rooms for the classes
entrance = Room("Entrance", "0", "There are three doors: one to your left, one to the front, and one to your right. A torch dimly lights the entrance. \nFrom somewhere above, you think that you hear a scream.", "Left Door", "Center Door", "Right Door", "torch", "silver key", X)
hall_1 = Room("First Hall", "1", "You see one door down the rest of the hallway. There is also a door back to where you had just come from. \nThis room is just incredibly murky, not unlike a dungeon. \nThere is a chest on the floor, which upon first glance, is locked. Thanks to the torch, you have a general idea of the room.", "Door to the Entrance", "Door Marked 3", X, "spinach", "diamond key", X)
hall_2 = Room("Second Hall", "2", "You see one door down the rest of the hallway. There is also a door back to where you had just come from. \nThis room is far murkier than the last one you were just in. \nThere is a chest on the floor, which is locked by a heavy diamond padlock. \nIt is thanks to the torch that you can see anything at all.", "Door to the Entrance", "Door Marked 2", X, "egg", "silver orb", X)
room_1 = Room("First Room", "3", "You see two doors on opposite ends of each other. There is also a door that leads to the entrance. \nThis room reeks of danger. A low mist crawls across the floor, while a chicken pecks at concrete. \nYou see a flash of movement to your left but when you look, you see nothing but a strand of a web. \nThe spider appears to have abandoned it. \nIn the middle of the floor lies a massive stove.", "Door to the Entrance", "Door Marked 4", "Door Marked 5", "chicken", "spider thread", "mist")
room_2 = Room("Second Room", "4", "This room is a complete contrast to everything that you have seen before. \nIt is just as grand as the fanciest stories you have read, and the ceiling stretches on further than should be possible. \nTwo doors are tucked as far away from each other as possible. \nA golden trash can lies in the corner.", "Door Marked Hall-2", "Door Marked 5", X, "golden key", "golden orb", "golden wool")
room_3 = Room("Third Room", "5", "This room runs hotter than any other that you have been in thus far. \nThe answer becomes glaringly clear with the heavy boiler that sits in a corner, rattling angrily. \nIf you didn't know better, you would've thought that it was hungry. \nThere are three doors in the room.", "Door Marked Hall-1", "Door Marked 4", "Door Marked Hall-3", "spider", "blue wool", X)
room_4 = Room("Fourth Room", "6", "The first thing that catches your sight is a gigantic loom that stretches almost all the way to the ceiling. \nA large piece of purple wool hangs from it already. \nThere is only one door in the room besides the one that you just entered from.", "Door Marked 1", "Door Marked 3", X, "purple wool", X, X)
room_5 = Room("Fifth Room", "7", "A large decorative platter hangs on a wooden wall. \nThere are three doors in the room, spaced purposefully away from each other.", "Door Marked 1", "Door Marked 2", "Door Marked Hall-3", "bronze orb", X, X)
hall_3 = Room("Third Hall", "8", "This room is strange to see after the brilliance you had seen before. \nIt is a call back to the haunting of the first few rooms you had been in. \nIn the room, there lies a book maker and a stairwell.", "Door Marked 3", "Door Marked 5", X, X, X, X)

startgame()                                     #automatically initializes the game