# Alex Ptacek - Assignment #3

# Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements
# and else statements print the user a message recommending a meal. For example, if the meal was breakfast, 
# you could say something like, “How about some bacon and eggs?” The user may enter something else in, but you
# only have to respond to breakfast, lunch, or dinner.

# Create a menu that displays meal options
def meal_menu():
    print("Enter number from options below to get meal recommendations!")
    print("1. Breakfast")
    print("2. Lunch")
    print("3. Dinner")
    print("4. Quit")

# Returns meal recommendation based on selected option, and keeps displaying menu until user chooses to quit.
done = False
while not done:
    meal_menu()
    selected = input()

    if selected == "1":
        print("Eggs and bacon")
    elif selected == "2":
        print("Salad with chicken")
    elif selected == "3":
        print("Cheeseburger and fries")
    elif selected == "4":
        done = True
    else:
        print("Invalid selection. Enter a number between 1 and 4")



# Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay,
# including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times
# their regular hourly pay rate for all hours over 20. You should take in the user’s input for the number of hours
# worked, and their rate of pay.

def payroll(hours_worked, rate):
    if hours_worked <= 20 and hours_worked >= 0:
        gross_pay = hours_worked * rate
        return gross_pay
    
# If hours worked is >20, multiplies initial 20 hours by the base rate and multiplies remaining hours by overtime rate,
# then adds together.
    elif hours_worked > 20:
        base_pay = 20 * rate
        overtime_pay = (hours_worked - 20) * (rate * 1.5)
        gross_pay = base_pay + overtime_pay
        return gross_pay
    
    else:
        return "Invalid Entry"


print(payroll(20, 10))
#Output: 200

print(payroll(30, 10))
#Output: 350.0

print(payroll(-5, 10))
#Output: "Invalid Entry"



# Q3: Write a function named times_ten. The function should accept an argument and display the product of its 
# argument multiplied times 10.

def times_ten(n):
    new_n = n*10
    return new_n

print(times_ten(23))
#Output: 230



# SQ4: Find the errors, debug the program, and then execute to show the output.

# This function needs to go before `main()` function
def showCalories(calories1, calories2):    #Add colon and parameters
   #Replaced curly quotes for straight quotes in first object and wrap .2f in quotes in second object
   print("The total calories you ate today", format(calories1 + calories2, ".2f"))

def main():    #Add colon
      #Convert user input to float so it can be used for addition
      calories1 = float(input( "How many calories are in the first food?"))
      calories2 = float(input( "How many calories are in the second food?")) #Change first to second
      showCalories(calories1, calories2)


main()
#Input: (10, 10)
#Output: 20.00



# Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:

# 1/30 + 2/29 + 3/28 ............. + 30/1

# The series provided exhibits a pattern where the dividend starts at 1 and increases by 1 up to 30, while the
# divisor starts at 30 and decreases by 1 until it reaches 1. To first create this series, I created two lists to
# loop through, one from 1 to 30 and the other from 30 to 1. Then, I simply divided those numbers and added to total.
for x, y in zip(list(range(1, 31)), list(range(1, 31))[::-1]):
    total_sum = 0
    total_sum += x/y

print(total_sum)
#Output: 30.0



# Q6: Write a function that computes the area of a triangle given its base and height.
# The formula for an area of a triangle is:
# AREA = 1/2 * BASE * HEIGHT

# For example, if the base was 5 and the height was 4, the area would be 10.
# triangle_area(5, 4)   # should print 10

def triangle_area(base, height):
    area = .5 * base * height
    return area

print(triangle_area(5, 4))
#Output: 10.0

print(triangle_area(6, 3))
#Output: 9.0