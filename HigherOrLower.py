import random

def get_username():
    """Input name, quit for 'no', greet player, then return username"""
    username = input('Type your name if you want to play the game, else type "no":\n').title()
    if username.lower() == 'no':
        quit()
    else:
        print(f'Welcome to the Higher/Lower game {username}!\n')
        return username

def get_lower_upper_bounds():
    """Input lower/upper bound, loop if lower >= upper, display error if input is not an integer, return lower/upper"""
    while True:
        try:
            lower_bound = int(input('What is the lower range/bound of the numbers you want to guess between: '))
            upper_bound = int(input('What is the upper range/bound of the numbers you want to guess between: '))

            if lower_bound >= upper_bound:
                print('The lower bound must be less than the upper bound number. Please select a new range.')
            else:
                return lower_bound, upper_bound
        except ValueError:
            print('Please pick a valid number, not a letter!')

def get_user_guess(lower_bound, upper_bound):
    """Get user guess, if they guess outside of bounds reinput guess, if input is not integer provide error message"""
    while True:
        try:
            user_guess = int(input(f'Guess a number between {lower_bound} and {upper_bound}: '))
            #Provide user feedback if they are higher or lower than random_num
            if user_guess > upper_bound or user_guess < lower_bound:
                print(f'Please guess between {lower_bound} and {upper_bound}.')
            else:
                return user_guess
        except ValueError:
            print('Please type a number.')
            

def play_game():
    """Main gameplay loop"""

    #Call functions for username/greeting, and establishing bounds, then establish variables
    username = get_username()
    lower_bound, upper_bound = get_lower_upper_bounds()
    random_num = random.randint(lower_bound, upper_bound)
    num_guess = 0
    guess = 0


    #Loop while guess is not the correct number, acquire user guess by calling user_guess funct, increment num_guesses, display appropiate message
    while guess != random_num:
        guess = get_user_guess(lower_bound, upper_bound)
        num_guess += 1
        #Provide user feedback if they are higher or lower than random_num
        if guess == random_num:
            print(f'\nGood job, you guessed {random_num}, the right number... you win!')
            print(f'It took you {num_guess} tries.')
        elif guess > random_num:
            print(f'\nYou guessed {guess}, but you are a bit too high!')
            print(f'Attempts: {num_guess}\n')
        elif guess < random_num:
            print(f'\nYou guessed {guess}, but you are a bit too low!')
            print(f'Attempts: {num_guess}\n')       


if __name__ == '__main__':
    """If this script is run independently then call play_game function and initiate game"""
    play_game()
