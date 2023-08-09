# Cameron J. Freed
# IT 140
# Southern New Hampshire University
# Module 7 -- Project Two
# Simplified Version of Game



import os #import os for clear screen function
import time #import time -- was using input(press enter) to slow progress before screen clear, but time.sleep works great


def clear_screen():
    """Clears screen to improve readability, had to google this one because I could not stand game testing with a clogged terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')
          

def greet_player():
    """Greet player and introduce game plot"""
    print('\nWelcome to "Reflections of the Mind". In this text-based journey you\'ll delve into the ethereal\n'
          'realms of your own subconscious. Your mission is to navigate your mind\'s eight corridors to find\n'
          'six important artifacts, each representing a fragment of past experiences. From the innocence of childhood\n'
          'to your trials with sorrow and bravery, each item you collect will unveil a part of your inner self.\n'
          'But beware -- in the Mirror Room a demon of your own skin lies, confront him only when you are mentally prepared.')
    print('-' * 70)


def show_instructions():
    """Display instructions on how to move between rooms and get items."""
    print('\nValid movement commands are {\033[1m\033[4mgo North, South, East or West\033[0m}'
          '\nValid item commands are {\033[1m\033[4mget item name\033[0m} to pick up an item.'
          '\nTo use your map you must first acquire it, then type {\033[1m\033[4mmap\033[0m} to display.\n'
          'Type "exit" at anytime to quit.')
    print('-' * 70)
    input('Press enter to continue.') #allow user to read instructions and enter when done before screen clears


def display_player_status(current_room, inventory):
    """
    Display inventory, current location, and current rooms description
    
    This function takes the current room and inventory list as input and
    outputs the player's current room, that rooms customized description, and their inventory.
    """
    print(f'You are in the {current_room}.')
    print('-' * 27)
    print(room_intro_msg[current_room])
    print('-' * 27)
    print(f'Inventory: {inventory}')
    print('-' * 27)


def move_player(current_room, direction):
    """
    Move the player to a new room based on the provided direction.

    This function takes the current room and a direction as input and checks if the specified
    direction is valid for the current room by accessing rooms dictionary. If the direction is valid, the player is moved
    to the new room, and the name of the new room is returned.

    Returns:
        string: The name of the new room if the movement is successful, otherwise the current room name.
    """
    direction = direction.strip() #strip whitespace from lead and trail of direction to standardize user input

    if direction in rooms[current_room].keys():
        clear_screen()
        print(f'You move {direction.lower()}...')
        time.sleep(1) #used to delay looping so user can see move direction msg for immersion
        new_room = rooms[current_room][direction]
        return new_room
    elif direction in ['North', 'South', 'East', 'West']:
        print(f'You cannot go {direction.lower()} from the {current_room}.')
        time.sleep(1.3) #used to delay looping so user can see move direction msg for immersion
        return current_room
    else:
        print('You want me to go where?! That is not a valid direction.')
        time.sleep(1.3) #used to delay looping so user can see move direction msg for immersion
        return current_room


def obtain_item(current_room, item, inventory):
    """
    Get_item function to be completed in Project 2
    Obtain an item and add it to the player's inventory if it exists in the current room.

    This function takes the current room, the item name, and the player's inventory as input.
    It checks if the item exists in the current room and if it does, adds it to the player's inventory.
    If the item is already in the inventory, it displays a message that the room has already been searched.
    If there is no item in the room, it displays that the room is empty.

    Returns:
        list: The updated player's inventory after obtaining the item.
    """
    if 'Item' in rooms[current_room].keys():
        if item not in inventory and item in rooms[current_room].values(): 
            clear_screen()
            print(f'You acquire the {item.lower()}!')
            print(f'{item_descriptions[item]}')
            time.sleep(2.0)
            inventory.append(item)
            return inventory
        else:
            print('There is nothing here that you require...\n'
                  'Your conciousness moves you forward')
            time.sleep(1.3)
            return inventory    
    else:
        print('It seems this domain doesn\'t have what you are seeking...')
        time.sleep(1.3)
        return inventory
    

def display_map(current_room, inventory):
    if 'Map' in inventory:
        map_text = rooms[current_room].get('Map', 'There is no map for this room.')
        clear_screen()
        print(map_text)
        print('-' * 100)
        input('\n\t\t\t\tYour current location is highlighted.\n\t\t\t\t     Press enter to continue.')
    else:
        print('\nYou have not collected the map yet.')
        time.sleep(1.3)



#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = { 
        'Mental Haze': {
            'South' : 'Gallery of Joy', 
            'North' : 'The Labryinth of Confusion', 
            'East' : 'Ocean of Tears', 
            'West' : 'Childhood Room',
            'Item' : 'Map',
            'Map': '''
            [ Abandoned Park ]---------[ Labryinth of Confusion ]       [ The Mirror Room ]
                                                  |                              |
                                                  |                              |
            [ Childhood Room ]------------[ \033[1m\033[4mMental Haze\033[0m] ]---------------[ Ocean of Tears ]
                                                  |
                                                  |
                                         [ Gallery of Joy ]----------[ Chamber of Courage ]
            ''',
            },
        'Gallery of Joy' : {
            'North' : 'Mental Haze',
            'East' : 'Chamber of Courage',
            'Item' : 'Laughter-Filled Journal',
            'Map': '''
            [ Abandoned Park ]---------[ Labryinth of Confusion ]       [ The Mirror Room ]
                                                  |                              |
                                                  |                              |
            [ Childhood Room ]------------[ Mental Haze ]---------------[ Ocean of Tears ]
                                                  |
                                                  |
                                         [ \033[1m\033[4mGallery of Joy\033[0m ]----------[ Chamber of Courage ]
            ''',
            
            },
        'Chamber of Courage' : {
            'West' : 'Gallery of Joy',
            'Item' : 'Medallion Of Bravery',
            'Map': '''
            [ Abandoned Park ]---------[ Labryinth of Confusion ]       [ The Mirror Room ]
                                                  |                              |
                                                  |                              |
            [ Childhood Room ]------------[ Mental Haze ]---------------[ Ocean of Tears ]
                                                  |
                                                  |
                                         [ Gallery of Joy ]----------[ \033[1m\033[4mChamber of Courage\033[0m ]
            ''',
            },
        'Childhood Room' : {
            'East' : 'Mental Haze',
            'Item' : 'Old Teddy Bear',
            'Map': '''
            [ Abandoned Park ]---------[ Labryinth of Confusion ]       [ The Mirror Room ]
                                                  |                              |
                                                  |                              |
            [ \033[1m\033[4mChildhood Room\033[0m ]------------[ Mental Haze ]---------------[ Ocean of Tears ]
                                                  |
                                                  |
                                         [ Gallery of Joy ]----------[ Chamber of Courage ]
            ''',
            },
        'Ocean of Tears' : {
            'West' : 'Mental Haze',
            'North' : 'The Mirror Room',
            'Item' : 'Tear-Stained Letter',
            'Map': '''
            [ Abandoned Park ]---------[ Labryinth of Confusion ]       [ The Mirror Room ]
                                                  |                              |
                                                  |                              |
            [ Childhood Room ]------------[ Mental Haze ]---------------[ \033[1m\033[4mOcean of Tears\033[0m ]
                                                  |
                                                  |
                                         [ Gallery of Joy ]----------[ Chamber of Courage ]
            ''',
            },
        'Abandoned Park' : {
            'East' : 'The Labryinth of Confusion',
            'Item' : 'Faded Photograph',
            'Map': '''
            [ \033[1m\033[4mAbandoned Park\033[0m ]---------[ Labryinth of Confusion ]       [ The Mirror Room ]
                                                  |                              |
                                                  |                              |
            [ Childhood Room ]------------[ Mental Haze ]---------------[ Ocean of Tears ]
                                                  |
                                                  |
                                         [ Gallery of Joy ]----------[ Chamber of Courage ]
            ''',
            },
        'The Labryinth of Confusion' : {
            'South' : 'Mental Haze',
            'West' : 'Abandoned Park',
            'Item' : 'Enigmatic Puzzle Piece',
            'Map': '''
            [ Abandoned Park ]---------[ \033[1m\033[4mLabryinth of Confusion\033[0m ]       [ The Mirror Room ]
                                                  |                              |
                                                  |                              |
            [ Childhood Room ]------------[ Mental Haze ]---------------[ Ocean of Tears ]
                                                  |
                                                  |
                                         [ Gallery of Joy ]----------[ Chamber of Courage ]
            ''',
            },
        'The Mirror Room' : {
            'South' : 'Ocean of Tears',
             'Villain' : 'The Mirror Demon',
            'Map': '''
            [ Abandoned Park ]---------[ Labryinth of Confusion ]       [ \033[1m\033[4mThe Mirror Room\033[0m ]
                                                  |                              |
                                                  |                              |
            [ Childhood Room ]------------[ Mental Haze ]---------------[ Ocean of Tears ]
                                                  |
                                                  |
                                         [ Gallery of Joy ]----------[ Chamber of Courage ]
            ''',
            }
    }


#Dictionary to link a introduction message for each room.
room_intro_msg = {
    'Mental Haze' : 'You find yourself in a dimly lit chamber, surrounded by an ethereal mist.\n'
                    'A sense of uncertainty lingers in the air as you stand at the threshold of your mind.\n'
                    'A shriveled \033[1m\033[4mmap\033[0m appears out of the mist, shining as if beckoning you to reach out.\n'
                    'Take a deep breath, for the path ahead is laden with memories waiting to be unraveled.',
    'Childhood Room': 'As you step through the door, a rush of nostalgia embraces you.\n'
                      'The room exudes the innocence of your childhood. You can almost hear the laughter\n'
                      'echoing through the walls and feel the warmth of your mother\'s embrace. Among the scattered\n'
                      'toys, an \033[1m\033[4mold teddy bear\033[0m lies, patiently waiting to share its tales of comfort and companionship.',
    'Abandoned Park': 'A haunting stillness surrounds you as you enter the desolate park. The rustling\n'
                      'of leaves and creaking swings evoke memories of carefree days spent here. \n'
                      'Yet, now, the park stands abandoned, mirroring a sense of loss. A \033[1m\033[4mfaded photograph\033[0m rests on a bench, \n'
                      'capturing a moment frozen in time, a bittersweet reminder of those who have left your life.',
    'The Labryinth of Confusion': 'You find yourself in a perplexing maze of twisting corridors, each path leading to a different memory.\n'
                                 'The walls seem to whisper fragments of forgotten conversations, leaving you feeling lost and uncertain.\n'
                                 'In the heart of the labyrinth lies an \033[1m\033[4menigmatic puzzle piece\033[0m, a symbol of the confusion that once clouded your mind.',
    'Chamber of Courage': 'As you enter this room, a warm glow envelops you, and a sense of bravery fills the air.\n'
                          'Here, you confront a defining moment of valor from your past. The flickering candlelight\n'
                          'dances on a \033[1m\033[4mmedallion of bravery\033[0m, a testament to your past courage and determination.',
    'Ocean of Tears': 'The room feels heavy with sorrow as if an ocean of tears has engulfed it.\n'
                      'Waves of emotions crash against the walls, reminding you of moments of grief and heartache.\n'
                      'Among the sea of emotions, a \033[1m\033[4mtear-stained letter\033[0m floats, bearing the weight of unspoken sentiments.',
    'Gallery of Joy': 'Entering this vibrant room is like stepping into a gallery of happiness. The walls adored\n'
                      'with pictures capture the essence of joy in your life. A \033[1m\033[4mlaughter-filled journal\033[0m lies open\n'
                      'on a table, recounting moments of sheer delight, inviting you to relive those memories.',
    'The Mirror Room': 'Dread fills your heart as you approach the final room.\n'
                       'The reflective surfaces distort your image, revealing the shadows that lurk within.\n'
                       'This room houses the Mirror Demon, an embodiment of your innermost fears and regrets.\n'
                       'Confronting this sinister apparition is your last trial before finding inner peace.'
}


#Dictionary to link an item pick up message for each item.
item_descriptions = {
    'Old Teddy Bear': 'A worn and huggable companion from your childhood, filled with memories of comfort and warmth.',
    'Faded Photograph': 'A weathered photograph capturing a moment of joy and togetherness, now tinged with nostalgia.',
    'Enigmatic Puzzle Piece': 'A mysterious puzzle piece representing the confusing and unresolved memories of your past.',
    'Medallion Of Bravery': 'A shining medallion symbolizing the courage and determination you displayed in a challenging moment.',
    'Tear-Stained Letter': 'A heartfelt letter filled with unspoken emotions, revealing the depth of past sorrows.',
    'Laughter-Filled Journal': 'A joyful journal brimming with laughter and delightful memories, inviting you to relive happy moments.',
    'Map' : 'A worn piece of parchment containing directions, you recognize the writing as your own... have you been here before?'
}


def main_game_loop():
    """
    This function initializes the Dragon Game, displaying the game's greeting and instructions. It manages the game loop,
    where the player can interact with the game by entering commands to move between rooms and obtain items.
    The loop continues until the player decides to exit the game by typing 'exit'.
    """
    inventory = [] #create empty list for inventory
    current_room = 'Mental Haze' #tracks current room
    command = 'null' #initialize command to 'null' prior to gameplay loop

    greet_player() #call greeting() for initial display
    show_instructions() #call show_instructions for initial display

    while current_room != 'Exit': 
        clear_screen() #call clear screen function at beginning of each turn
        display_player_status(current_room, inventory) #call player_status() with current_room as argument to display customized status page

        while current_room == 'The Mirror Room':
            rebuttal = input('Do you \033[1m\033[4mconfront\033[0m the mirror demon or \033[1m\033[4mcollect\033[0m your thoughts?: ') #user input if to continue
            if rebuttal.lower() == 'confront':
                clear_screen()
                if len(inventory) >= 7: # if user chooses to continue to final room, and inventory meets win condition, display win statement
                    print('As you stare into the shattered reflections of your past, you gain newfound clarity and strength.\n'
                        'The triumph over your own demons has unlocked the path to inner peace and self-acceptance.\n\n'
                        'You slowly regain \033[1m\033[4mconsciousness\033[0m.\n')
                    exit()
                else: # if user chooses to continue to final room, and inventory doesnt meet win condition, display lose statement
                    print('The weight of your fears and regrets feels insurmountable. The distorted reflections seem to taunt and overwhelm you\n'
                        'plunging you deeper into a state of despair. Despite your efforts, the demon\'s grip on your mind remains unyielding.\n'
                        'You find yourself unable to conquer the shadows that haunt you.\n\n'
                        'You quickly fall into a deeper state of panic...\n\n'
                        'You have lost your \033[1m\033[4mmind\033[0m.\n')
                    exit()
            elif rebuttal.lower() == 'collect': # if user chooses to retreat, move them back south and display current status
                current_room = move_player(current_room, 'South')
                time.sleep(1.3)
                clear_screen()
                display_player_status(current_room, inventory)
            elif rebuttal.lower() == 'map':
                print('\nYou cannot use your map right now!')
                time.sleep(1.3)
                clear_screen()
                display_player_status(current_room, inventory)
            else: # if user input no valid entry repeat until valid entry is provided
                print('\nInvalid choice. Please enter {confront} or {collect} to continue.\n')
                time.sleep(1.5)
                clear_screen()
                display_player_status(current_room, inventory) #call player_status() with current_room as argument to display customized status page


        
        command = input('What is your next move?: ').title().split(' ') #titalizes the user command and splits it into a list called command to mesh with dict room name format
        if not command: #if no command (user presses enter) repeat loop. this ensures no list index error arrises
            continue
        if command[0] == 'Get': 
            item = command[1:]
            item_name = ' '.join(item)
            obtain_item(current_room, item_name, inventory) #call get item function with current room, second word of user command, and inventory as arguments
        elif command[0] == 'Go' and len(command) == 2:
            new_room = move_player(current_room, command[1]) #call player_move function with current room and second word of user command as arguments, assigns return value to new room
            current_room = new_room #current room is new room
        elif command[0] == 'Map':
            display_map(current_room, inventory)
        elif command[0] == 'Exit':
            current_room = 'Exit' #set current room to exit 
        else:
            clear_screen()
            print('\nThat is not a valid command!') #if no authorized commands entered, output message and offer to repeat instructions, then repeat loop.
            repeat_instruct = input('Type {yes} to view instructions, or enter to continue: ')
            if repeat_instruct == 'yes':
                    show_instructions()
    if current_room == 'Exit':
        print('\nYou are your only advocate... (please try to regain consciousness again)')
        exit()


if __name__ == '__main__':
    """
    This if statement only operates if the file is run as the main program
    When True, calls main() function to begin the game.
    """
    main_game_loop()
