import time

#a slow text print, for dramaticness
def print_slow(text):
    #Takes each line from the text block and prints them slowly
    for line in text.split('\n'):
        print(line)
        time.sleep(0.5)

def play_game():
    # Game State
    inventory = []
    current_room = "living room"
    game_on = True

    #list of all the rooms
    rooms = {
        "living room":{
            "description":"""A simple room, with a well loved couch and a small TV in the corner.\n 
The news on, but you're not paying attention to what seems to be the 12th vampire attack this month.
            """,
            "exits":"""You can go to the DOOR, the KITCHEN, or the PLANT ROOM."""
            },
        "door":{
            "description":"""""",
            "exits":"""this"""
        }       
    }

    while game_on:
        room = rooms[current_room]
        print(f"\n{room["description"]}")
        print(f"\n{room["exits"]}")

        #shuts off the game
        exit()

play_game()
