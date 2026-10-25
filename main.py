import time
import textwrap

#a slow text print, for dramaticness
def print_slow(text):
    #Takes each line from the text block and prints them slowly
    for line in text.split('\n'):
        print(line)
        time.sleep(1)


def play_game():
    # Game State
    inventory = []
    current_room = "living room"
    runs = 0
    action = ""
    game_on = True
    first_action = True
    #print_slow(f"""{num_kills} Way(s) to Kill a Girl Scout
#-----""")
    #list of all the rooms
    rooms = {
        "living room":{
            "description":textwrap.fill("""You are in your living room, with a well loved couch and a small TV in the corner.
The news on, but you're not paying attention to what seems to be the 12th vampire attack this month.""", 90),
            "exits":"""You can go to the DOOR, the KITCHEN, the PLANT ROOM, or BATHROOM."""
            },
        "door":{
            "description":"""You are at your front door. It is dark outside, and the streetlamps are on.""",
            "exits":"""You can go to the LIVING ROOM."""
        },
        "kitchen":{
            "description":textwrap.fill("""You are in your kitchen. Your famous garlic chicken parm lies on the counter,
along with the leftover cloves of garlic.""", 90),
            "exits":"""You can go to the LIVING ROOM."""
        },
        "plant":{
            "description":textwrap.fill("""You are in your greenhouse. Well, it's technically a repurposed office space.
It doesn't get a lot of sunlight in the winter, so you have some battery powered UV lamps around.""",90),
            "exits":"""You can go to the LIVING ROOM."""
        },
        "bathroom":{
            "description":textwrap.fill("""You are in your bathroom. It's pretty small, but it has all the necesities. 
You notice your old plunger by the toilet.""", 90),
            "exits":"""You can go to the LIVING ROOM."""
        }
    }

    #method that checks if you want to go to the living room
    def go_living():
        nonlocal action
        nonlocal current_room
        if action in ["living room", "living"]:
            current_room = "living room"
    #ending unlock numbers
    def unlocked_endings(runs_num):
        runs_num += 1
        print(f"""You have completed {runs_num} run(s).
-----""")
        restart = input("Would you like to play again? (y/n) ")
        if restart == "y":
            print("-----")
            play_game()
        else:
            print("Thank you for playing!") 
        
    while game_on:
        room = rooms[current_room]
        print(f"\n{room["description"]}")
        print(f"{room["exits"]}")

        if first_action:
            first_action = False
            print("\nSuddenly, you hear your doorbell ring.")
            choice = input("Do you want to answer the door? (y/n) ")
            if choice == "y":
                action = "door"
            elif choice == "n":
                print_slow("""Whoever it is, they'll leave eventually. 
As time slips by, the news starts covering yet another vampire attack.\n""")
                unlocked_endings(runs)
                break
        
        #prompt for actions
        else:
            action = input("\nWhat would you like to do? ").lower().strip()
        
        #end game
        if action in ["quit", "exit"]:
            print_slow("Thanks for playing!")
            break
        #check inventory
        if action in ["inventory", "i"]:
            print(f"[Inventory: {', '.join(inventory)}]")
    #logic for each room
        #living room movement
        if current_room == "living room":
            if "door" in action:
                current_room = "door"
            elif action in ["plant room", "plant"]:
                current_room = "plant"
            elif "kitchen" in action:
                current_room = "kitchen"
            elif "bathroom" in action:
                current_room = "bathroom"
            else:
                print("I don't understand that action.")
        if current_room == "door":
            go_living()
            #things you can do in this room: greet girl scout, look in mirror

        elif current_room == "plant":
            go_living()
            #things you can do in this room: get uv plant lights
            if action in ["UV", "light", "UV light", "lights"]:
                inventory.append("UV lights")
                print("You pick up your UV lights. It's basically sunlight, right?")
                rooms["plant"]["description"] = """You are in your greenhouse. Well, it's technically a repurposed office space."""
            else:
                print("I don't understand that action.")
        elif current_room == "kitchen":
            go_living()
            #things you can do in this room: get garlic
            if "garlic" in action:
                inventory.append("garlic")
                print("In the stories, vampires are weak to garlic. Good thinking.")
                rooms["kitchen"]["description"] = """You are in your kitchen. Your famous garlic chicken parm lies on the counter."""
            elif "chicken parm" in action:
                print("I don't think vampires can eat human food. Besides, why would you waste your food like that?")
            else:
                print("I don't understand that action.")
        elif current_room == "bathroom":
            go_living()
            #things you can do in this room: get plunger
            if "plunger" in action:
                inventory.append("stake")
                print("You take the plunger handle and snap it surprisingly easily. This should work as a stake.\nStake Taken.")
                #update the dictionary of room description
                rooms["bathroom"]["description"] = """You are in your bathroom. It's pretty small, but it has all the necesities."""
            else:
                print("I don't understand that action.")

play_game()
