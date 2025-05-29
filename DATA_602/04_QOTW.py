# QOTW #4 - Alex Ptacek
# To reader: all my code has been tested, but I have opted against including the output.
# I encourage you to try any argument that would break it or return something unintended
# and please let me know. Thank you!

# 1. Write a function to calculate the area and perimeter of a rectangle.
def rectangle_area_and_perim(length, width):
    area = length * width
    perimeter = 2*length + 2*width

    print("The rectangle's area is: ", area)
    print("The rectangle's perimeter is: ", perimeter)

rectangle_area_and_perim(5, 3)


# 2. Write a function to check if a number is even or not.  The function should indicate to the user even or odd.
def is_even(number):

    # Verify we are only accepting integers. Bool has to be specified
    # as well because Python will read it as a 1 or 0
    if not isinstance(number, int) or isinstance(number, bool):
        print("This funtion only accepts integers")
    elif number % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")


# 3. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample string: “CUNY sps”
# # of upper case characters: 4
# # of lower case characters: 3

# NOTE TO FUTURE SELF: THIS FUNCTION DOESN'T GET RID OF PUNCTUATION.
# HERE IS A VERSION FROM A CLASSMATE THAT WORKS:

# def count_upper_lower(s):
#     upper_count = sum(1 for c in s if c.isupper())
#     lower_count = sum(1 for c in s if c.islower())
#     return upper_count, lower_count

def count_case(string):
    upper_counter = 0   # initialize upper and lower case counters
    lower_counter = 0
    string = string.replace(" ", "") # UPDATE: added these 2 lines
    string = string.strip()          # to remove non-letters

    # If argument is string, counts upper and lower case characters
    # and prints at end of function 
    if isinstance(string, str):
        for letter in string:
            if letter == letter.upper():
                upper_counter += 1
            elif letter == letter.lower():
                lower_counter += 1

    # If argument not string, informs user that function only accepts strings,
    # not [whatever type of object they entered] and exits function immediately
    else:
        print(f'This function only accepts strings, not {type(string)}')
        return
    
    # Since this expression is outside of the if statement, only prints
    # if argement input by user is a string.
    print(f'# of upper case characters: {upper_counter}')
    print(f'# of lower case characters: {lower_counter}')


# 4. Write a Python function to sum all the numbers in a list

# After lots and lots of testing, here is my function. It only accepts lists
# that are all numbers. If there is any non-number, the function will stop,
# return no value, and state that it only accepts numbers.
def sum_nums_in_list(list_of_numbers):
    total_sum = 0   # initialize variable to hold sum of numbers

    # Loop through list. Only add value if it's a number. Excluding bool
    # because Python recognizes True as 1 and False as 0 if not specified.
    for num in list_of_numbers:    
        if isinstance(num, (int, float)) and not isinstance(num, bool):
            total_sum += num
        else:    # If not a number, stops function and only prints the below.
            print("This function only accepts integers and floats")
            return ""    # needs blank string so it doesn't print "None"

    return total_sum
        

random_nums = [1,2,3,4,5]
result = sum_nums_in_list(random_nums)
print(result)


# 5. Create a function that shows an example of global vs local variables.

x = 5    # Global variable

def test_function():
    x = 2    # Local variable
    print(x)

test_function()    # Ouput: 2
                   # Calling the function utilizes the local variable.

print(x)    # Output: 5
            # Calling x outside of the function uses the global variable.


# 6. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

# The "unknown given number" will be truly unknown with this function
# because it uses the random package to pick a random float multiplier
# for our input.
import random

def random_multiplier(num):
    random_number = random.uniform(-100, 100)    # picks a random float between
                                                 # -100 and 100
                                                 
    return round(num * random_number, 2)    # rounds to 2 decimals
