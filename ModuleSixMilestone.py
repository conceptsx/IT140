# Cameron J. Freed
# IT 140
# Southern New Hampshire University
# Module 6 - Milestone
# Simplified Version of Game



import os #import os for clear screen function


def clear_screen():
    """Clears screen to improve readability, had to google this one because I could not stand game testing with a clogged terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')
          

def greeting():
    """Greet player and introduce game plot"""
    print('\n\n\tWelcome to the dragon-game, where you must search a castle for 6 items\n'
          '\tand confront the dragon. Make sure you have all items before the fight')
    print('\t\t', '*' * 48) #my attempt at formatting the introduction message to make it nicer


def show_instructions():
    """Display instructions on how to move between rooms and get items."""
    print('\tValid movement commands are {go North, South, East or West}\n'
          '\tValid item commands are {get item} to add nearby item to inventory.\n'
          '\t\t\tType "exit" at anytime to quit.')
    print('\t\t', '*' * 48, '') #my attempt at formatting the introduction message to make it nicer
    input('\t\t\tPress enter to continue.') #allow user to read instructions and enter when done before screen clears


def player_status(current_room, inventory):
    """
    Display inventory, current location, and current rooms description
    
    This function takes the current room and inventory list as input and
    outputs the player's current room, that rooms customized description, and their inventory.
    """
    print(f'You are in the {current_room}.')
    print(room_intro_msg[current_room])
    print(f'Inventory: {inventory}')


def player_move(current_room, direction):
    """
    Move the player to a new room based on the provided direction.

    This function takes the current room and a direction as input and checks if the specified
    direction is valid for the current room by accessing rooms dictionary. If the direction is valid, the player is moved
    to the new room, and the name of the new room is returned.

    Parameters:
        current_room: The name of the current room.
        direction: The direction in which the player wants to move (e.g., 'North', 'South', 'East', 'West').

    Returns:
        string: The name of the new room if the movement is successful, otherwise the current room name.
    """
    direction = direction.strip() #strip whitespace from lead and trail of direction to standardize user input

    if direction in rooms[current_room].keys():
        print(f'You move {direction}...')
        new_room = rooms[current_room][direction]
        return new_room
    else:
        input(f'You cannot go {direction.lower()} from the {current_room}. Press enter to continue.')
        return current_room

 
def get_item(current_room, item, inventory):
    """
    Get_item function to be completed in Project 2
    Obtain an item and add it to the player's inventory if it exists in the current room.

    This function takes the current room, the item name, and the player's inventory as input.
    It checks if the item exists in the current room and if it does, adds it to the player's inventory.
    If the item is already in the inventory, it displays a message that the room has already been searched.
    If there is no item in the room, it displays that the room is empty.

    Parameters:
        current_room: The name of the current room.
        item: The name of the item to obtain and add to the inventory.
        inventory: The player's inventory as a list of items.

    Returns:
        list: The updated player's inventory after obtaining the item.
    """
    input('FIXME: finish get_item function -- enter to continue')
    return -1



#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = { 
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

#Dictionary to link a introduction message for each room.
room_intro_msg = {
    'Great Hall' : 'A fantastic hall surrounds you, but its emptiness overwhelms you.',
    'Bedroom' : 'A lively quarters lays before you, a bed still warm... who was here?',
    'Cellar' : 'A dimly lit cellar blocks most of your vision, laced with cobwebs and chilly air.'
}

#Pending dictionary to link an item pick up message for each item.
#item_pickup_msg = { 
#
#}



def main():
    """
    This function initializes the Dragon Game, displaying the game's greeting and instructions. It manages the game loop,
    where the player can interact with the game by entering commands to move between rooms and obtain items.
    The loop continues until the player decides to exit the game by typing 'exit'.
    """

    inventory = [] #create empty list for inventory
    current_room = 'Great Hall' #tracks current room
    command = 'null' #initialize command to 'null' prior to gameplay loop

    greeting() #call greeting() for initial display
    show_instructions() #call show_instructions for initial display

    while current_room != 'Exit': 
        clear_screen() #call clear screen function at beginning of each turn
        player_status(current_room, inventory) #call player_status() with current_room as argument to display customized status page
        
        command = input('What is your next move?\n').title().split() #titalizes the user command and splits it into a list called command to mesh with dict room name format
        if not command: #if no command (user presses enter) repeat loop. this ensures no list index error arrises
            continue
        if command[0] == 'Get' and len(command) == 2: 
            get_item(current_room, command[1], inventory) #call get item function with current room, second word of user command, and inventory as arguments
        elif command[0] == 'Go' and len(command) == 2:
            new_room = player_move(current_room, command[1]) #call player_move function with current room and second word of user command as arguments, assigns return value to new room
            current_room = new_room #current room is new room
        elif command[0] == 'Exit':
            print('\nWhy did you abandon the castle!? :(')
            current_room = 'Exit' #set current room to exit 
        else:
            print('That is not a valid command!') #if no authorized commands entered, output message and offer to repeat instructions, then repeat loop.
            repeat_instruct = input('Type {yes} to view instructions, or enter to continue.')
            if repeat_instruct == 'yes':
                    show_instructions()
    if current_room == 'Exit':
        exit()
        


if __name__ == '__main__':
    """
    This if statement only operates if the file is run as the main program
    When True, calls main() function to begin the game.
    """
    main()
