import time
import textwrap

#a slow text print, for dramaticness
def print_slow(text):
    #Takes each line from the text block and prints them slowly
    for line in text.split('\n'):
        print(line)
        time.sleep(1)

runs = 0
def play_game():
    # Game State
    inventory = []
    current_room = "living room"
    global runs
    action = ""
    game_on = True
    first_action = True
    past_intro = False
    #decisions made across the game
    has_answered_doorbell = False
    interest_in_cookies = False
    let_her_in = False
    look_at_cookies = False
    #for killing, needs to check inventory

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
            "description":textwrap.fill("""You are at your front door. It is dark outside, and the streetlamps are on. A little
girl stands at your door, wearing a green vest identifying her as a Girl Scout.
"Hello! Would you like to buy some Girl Scout Cookies?" You can say YES or NO.""", 90),
            "exits":"""You can go to the LIVING ROOM."""
        },
        "kitchen":{
            "description":textwrap.fill("""You are in your kitchen. Your famous garlic chicken parm lies on the counter,
along with the leftover cloves of garlic.""", 90),
            "exits":"""You can go to the LIVING ROOM."""
        },
        "plant":{
            "description":textwrap.fill("""You are in your greenhouse. Well, it's technically a repurposed office space.
It doesn't get a lot of sunlight in the winter, so you have some battery powered UV lights around.""",90),
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
    def unlocked_endings():
        global runs 
        runs += 1
        print(f"""You have completed {runs} run(s).
-----""")
        restart = input("Would you like to play again? (y/n) ")
        if restart == "y":
            print("-----")
            play_game()
        else:
            print("Thank you for playing!") 

    def strict_input(current_room, has_answered_doorbell, interest_in_cookies, let_her_in, look_at_cookies):
        nonlocal action 
        nonlocal inventory
        nonlocal past_intro
        action = input("\nWhat would you like to do? ").lower().strip()
        poss_actions = []
        late_game_poss_actions = []
        #set of all approved actions at a moment depending on what choices you've made so far
        #really only matters for intro and murdering options
        if has_answered_doorbell == True:
            poss_actions = ["yes", "no"]
        if interest_in_cookies == True:
            poss_actions = ["let her in", "say no"]
        if let_her_in == True:
            #she is in the house
            #question is asking: would you like to look at the cookies? 
            poss_actions = ["yes", "no"]
        if look_at_cookies == False:
            #you don't lean in, and she doesn't kill you
            #so you get to go on to the next actions
            pass
        if current_room == "living room":
            late_game_poss_actions = ["plant", "plant room", "bathroom", "kitchen"]
        elif current_room == "plant":
            late_game_poss_actions = ["living", "living room", "uv", "light", "uv light", "lights", "take the light", "take the lights"]
        elif current_room == "bathroom":
            late_game_poss_actions = ["living", "living room", "plunger", "take the plunger"]
        elif current_room == "kitchen":
            late_game_poss_actions = ["living", "living room", "garlic", "chicken parm", "take the garlic", "take the chicken parm"]
        #second part of the game actions    
        if current_room == "door" and "garlic" in inventory:
            late_game_poss_actions.append("use garlic")
            late_game_poss_actions.append("use the garlic")
            late_game_poss_actions.append("throw the garlic")
            late_game_poss_actions.append("attack with garlic")
        if current_room == "door" and "stake" in inventory:
            late_game_poss_actions.append("use stake")
            late_game_poss_actions.append("use the stake")
            late_game_poss_actions.append("stab with stake")
            late_game_poss_actions.append("attack with stake")
            late_game_poss_actions.append("impale with stake")
        if current_room == "door" and "UV lights" in inventory:
            late_game_poss_actions.append("shine lights")
            late_game_poss_actions.append("shine the lights")
            late_game_poss_actions.append("shine uv lights")
            late_game_poss_actions.append("shine the uv lights")
            late_game_poss_actions.append("use lights")
            late_game_poss_actions.append("use the lights")

        if action not in poss_actions and not past_intro:
            print("I don't understand that action.")
        elif past_intro and action not in late_game_poss_actions:
            print("What did you want to do?")

    while game_on:
        room = rooms[current_room]
        print(f"\n{room["description"]}")
        if past_intro:
            print(f"{room["exits"]}")

        if first_action:
            first_action = False
            print("\nSuddenly, you hear your doorbell ring.")
            choice = input("Do you want to answer the door? (You must type either y or n) ")
            if choice == "y":
                has_answered_doorbell = True
                action = "door"
            elif choice == "n":
                print_slow("""Whoever it is, they'll leave eventually. 
As time slips by, the news starts covering yet another vampire attack.\n""")
                unlocked_endings()
                break
        
        #prompt for actions
        else:
            strict_input(current_room, has_answered_doorbell, interest_in_cookies, let_her_in, look_at_cookies)
        
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
        elif current_room == "door":
            go_living()
            #things you can do in this room: greet girl scout, look in mirror
            if action == "yes" and has_answered_doorbell:
                interest_in_cookies = True
                rooms["door"]["description"] = """"Great!" she exclaims, "We're donating the proceeds to the local hospital. 
We're also going to be running a blood drive next month!"

A shiver runs down your spine. It's rather chilly outside.
Just as you think that, the Girl Scout echos your sentiments.

"Geez, it sure is cold out here. Could I come in?" 
You could LET HER IN or SAY NO."""
            elif action == "no" and has_answered_doorbell:
                interest_in_cookies = True
                rooms["door"]["description"] = """"Aw man, are you sure? We're donating the proceeds to the local hospital, and we're also
running a blood drive next month!" She looks like a kicked puppy, and now you feel bad. Maybe you'll just buy
a box.
A shiver runs down your spine. It's rather chilly outside.

Just as you think that, the Girl Scout echos your sentiments.
"Geez, it sure is cold out here. Could I come in?" 
You could LET HER IN or SAY NO."""
            if action == "let her in":
                let_her_in = True
                rooms["door"]["description"] = textwrap.fill("""With a bright smile, she steps into your house. For a moment,
her smile seems unnatrually wide, but you brush it off as a trick of the light. What you can't brush off is the fact that
when you shut the front door, the mirror on the back contains ONLY your reflection.
Before you have a chance to confront her, she asks, "Would you like to look at the cookies I have?" You can answer YES or NO.""", 90)
            elif action == "say no":
                let_her_in = False
                rooms["door"]["description"] = textwrap.fill("""Her face falls, but she quickly pivots. "That's fine, stranger danger and all that."
She glances at the watch on her wrist and exclaims, "Oh look at the time, I'm sorry, my parents told me that I should be home by now. Maybe I'll stop
by another day. Have a nice rest of your evening!" """, 90)
                print_slow(f"\n{room["description"]}")
                unlocked_endings()
            if action == "yes" and let_her_in:
                look_at_cookies = True
                # you die
                rooms["door"]["description"] = """As you lean in to look at her cookies, she viciously bites into the side of your neck.
You bleed out within minutes. You don't even like girl scout cookies that much. Oh well."""
                print(f"\n{room["description"]}")
                unlocked_endings()
            elif action == "no" and let_her_in:
                # make an excuse and live
                past_intro = True
                rooms["door"]["description"] = textwrap.fill("""You're pretty sure this is a trap. This "girl" is definitely not a normal person. You mumble out
an excuse, something about needing your reading glasses. Without waiting for a response, you head into your living room, searching for something to defend yourself with. """, 90)
                print(f"\n{room["description"]}")
                rooms["door"]["description"] = """The vampire is still where you last saw her. Do you have a way to get rid of her?"""
                current_room = "living room"
                #main gameplay loop starts
            
            #murders! wooooo! the fun part
            if "garlic" in inventory and action in ["throw garlic", "use garlic"]:
                #death by garlic
                rooms["door"]["description"] = textwrap.fill(""""Hey, what are you doing?" she asks, "I'm just a little guy."
With surprising accuracy, you hurl the cloves of garlic at the vampire. She hisses and flails as multiple of them hit her head on.
"OH THE AGONY! THE STENCH! IT'S DISGUSTING!" While gagging and retching, the vampire flees from your house.
You've driven her off for now. Now you need to pick up all the cloves you've thrown...""", 90)
                print_slow(f"\n{room["description"]}")
                unlocked_endings()
            elif "UV lights" in inventory and action in ["shine lights", "shine uv lights", "use lights"]:
                #death by burning
                rooms["door"]["description"] = textwrap.fill(""""Hey, what are you doing?" she asks, "I'm just a little guy."
Before she can react, you whip out the UV lights and blast them at maximum strength.
She hisses she is set aflame, "AH! THE SUN! ONE OF MY FATAL WEAKNESSES!" Moments later, she is a pile of ash.
You're safe, but you need to clean up this mess you've made... """, 90)
                print_slow(f"\n{room["description"]}")
                unlocked_endings()
            elif "stake" in inventory and action in ["use stake"]:
                #death by stabbing
                rooms["door"]["description"] = textwrap.fill(""""Hey, what are you doing?" she asks, "I'm just a little guy."
Fast as lightning, you drive the stake through her vest, and into her heart.
There was very little resistance, indicating that she was a very old vampire. "ALAS," she screams, "I WAS CARELESS AND NOW I HAVE BEEN BESTED!"
No blood comes from her body, since vampires don't bleed. But now you have a corpse on your floor to dispose of. At least you're safe...""", 90)
                print_slow(f"\n{room["description"]}")
                unlocked_endings()


        elif current_room == "plant":
            go_living()
            #things you can do in this room: get uv plant lights
            if "light" in action or "uv light" in action or "uv lights" in action or "lights" in action:
                inventory.append("UV lights")
                print("You pick up your UV lights. It's basically sunlight, right?")
                rooms["plant"]["description"] = """You are in your greenhouse. Well, it's technically a repurposed office space."""
        elif current_room == "kitchen":
            go_living()
            #things you can do in this room: get garlic
            if "garlic" in action:
                inventory.append("garlic")
                print("In the stories, vampires are weak to garlic. Good thinking.")
                rooms["kitchen"]["description"] = """You are in your kitchen. Your famous garlic chicken parm lies on the counter."""
            elif "chicken parm" in action:
                print("I don't think you have time for that right now.")
        elif current_room == "bathroom":
            go_living()
            #things you can do in this room: get plunger
            if "plunger" in action:
                inventory.append("stake")
                print("You take the plunger handle and snap it surprisingly easily. This should work as a stake.")
                #update the dictionary of room description
                rooms["bathroom"]["description"] = """You are in your bathroom. It's pretty small, but it has all the necesities."""

play_game()
