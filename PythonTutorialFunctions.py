#Function is a machine that takes input and produces a return value
#DRY - Dont repeat yourself

def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)

"""print(hello_func('Hi', name = 'Cam'))"""

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

#accept arbitrary number of positional or keyword arguments
#positional arguments as classes the student is taking
#keyword arguments that are random info about student
#doesnt have to be *args or **kwargs
# this outputs a tuple with the positional arguments,
# and a dictionary with keys and values for student info

# () tuple -- [] list -- {} dict

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)
# this instead of passing the info in individually
# it passes in the complete list and dictionary
# you need to * and ** the parameters to unpack individually

#---------------------------------------------------------------#

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017,2))






