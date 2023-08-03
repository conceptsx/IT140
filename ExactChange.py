#define a function to calculate and return maximum change between each form of currency i.e(dollars thru pennies)
#this function should return a tuple, which each value representing the final amount of that specific form of currency
def exact_change(total_cents):
    num_dollars = total_cents // 100
    remaining_cents = total_cents % 100

    num_quarters = remaining_cents // 25
    remaining_cents %= 25

    num_dimes = remaining_cents // 10
    remaining_cents %= 10

    num_nickels = remaining_cents // 5
    remaining_cents %= 5

    num_pennies = remaining_cents

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies



#define a main function with main loop
#main loop consists of:
#ask user for input on amount of cents/pennies they want to exchange
#input validation for an input of 0 or below
#input validation for an input that is not an integer
#call a function and return values associated with each currency type
#output to user
if __name__ == '__main__':
    user_change = -1
    while user_change <= 0:
        try:
            user_change = int(input('Enter how much money you have in cents, ex.(1032).   :'))
            if user_change <= 0:
                print('Please enter a postive number.')
        except ValueError:
            print('Please enter a number.')
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(user_change)

    currency_dict = {
        'Dollar' : num_dollars,
        'Quarter' : num_quarters,
        'Dime' : num_dimes,
        'Nickel' : num_nickels,
        'Penny' : num_pennies
    }

    for currency_type, amount in currency_dict.items():
        if amount > 1 and currency_type != 'Penny':
            print(f'{amount} {currency_type}s')
        elif amount > 1 and currency_type == 'Penny':
            print(f'{amount} Pennies')
        elif amount > 0:
            print(f'{amount} {currency_type}')
        else:
            continue
        
