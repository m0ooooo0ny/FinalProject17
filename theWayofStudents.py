#defines acceptable responses to prevent other responses
acc_yes = ["yes", "yeah", "y", "yeh", "yah", "sure"]
acc_no = ["no", "nah", "nay", "n", "fight me bitch"]
acc_look = ["look", "look around", "have a gander", "see", "try to look"]
acc_doors = ["go through doors", "doors", "door", "look at doors", "through doors", "open doors", "open", "open door", "go through door"]
acc_rest = ["rest", "relax"]

acc_res = [acc_yes, acc_no, acc_look, acc_doors, acc_rest]
acc_responses = []
for a in acc_res:
    for b in a:
        acc_responses.append(b)

#defining the room
class Room(object):
    """Room object defines a room"""

    def __init__(self, style, description, position, door1, door2, door3, item1, item2, item3):
        """defines what the rooms are like
        style is the type of room and description. position is a number that indicates the position of the room.
        there can be up to three doors and up to three items in a room."""

        self.style = style
        self.position = position
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
        #START WORKING HERE

rest_lvl = 0
warning_lvl = 0
knowledge_lvl = 0

#entrance descriptor: """You are currently in the entrace of what appears to be an old castle. \nUnfortunately, you do not appear to remember anything of your past. \nSomething very cold and wet drips upon your head, and you feel a headache incoming."""

X = 1
#defining rooms
entrance = Room("room", "0", X, "Left Door", "Center Door", "Right Door", "torch", X, X)
hall_1 = Room("hallway", "1", X, "Door to the Entrance", "Door Marked 3", X, X, X, X)
hall_2 = Room("hallway", "2", X, "Door to the Entrance", "Door Marked 2", X, X, X, X)
room_1 = Room("room", "3", X, "Door to the Entrance", "Door Marked 4", "Door Marked 5", X, X, X)
room_2 = Room("room", "4", X, "Door Marked Hall-2", "Door Marked 5", X, X, X, X)
room_3 = Room("room", "5", X, "Door Marked Hall-1", "Door Marked 4", "Door Marked Hall-3", X, X, X)
room_4 = Room("room", "6", X, "Door Marked 1", "Door Marked 3", X, X, X, X)
room_5 = Room("room", "7", X, "Door Marked 1", "Door Marked 2", "Door Marked Hall-3", X, X, X)
hall_3 = Room("hallway", "8", X, "Door Marked 3", "Door Marked 5", "Stairwell", X, X, X)