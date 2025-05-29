# Q1. What will the following code display?

# The following code with display an empty list because the two arguments to the numbers
# list (1, -5) tell the program to start at index 1 and end at -5 (equivalent to index 0, in this case).
# Since the step is not specified, the program automatically reads the list from left to right.
# Combined, this means that this code is supposed to start at index 1 and end at index 0, but since it 
# only reads left to right, it ends up not reading any values and returns an empty list.
numbers = [1, 2, 3, 4, 5]
print(numbers[1:-5])

# Can you debug and fix the output?  The code should return the entire list

# To display the entire list you can either access the range of the list or simply print the list.

numbers = [1, 2, 3, 4, 5]
print(numbers[0:5])
print(numbers)


# Q2.Design a program that asks the user to enter a store’s sales for each day of the
# week. The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.

# Request sales for each day of the week
Sunday = float(input("Enter Sunday's sales: "))
Monday = float(input("Enter Monday's sales: "))
Tuesday = float(input("Enter Tuesday's sales: "))
Wednesday = float(input("Enter Wednesday's sales: "))
Thursday = float(input("Enter Thursday's sales: "))
Friday = float(input("Enter Friday's sales: "))
Saturday = float(input("Enter Saturday's sales: "))

# Store daily sales in a list
sales = [Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]

# Initialize total sales
total_sales = 0

# Loop through sales list and add each day's sales to total
for daily_sales in sales:
    total_sales += daily_sales

print(f'Total sales for the week: ${total_sales:.2f}')


# Q3.Create a list with at least 5 places you’d like to travel to.   Make sure the list isn’t in
# alphabetical order

travel_wishlist = ['Norway', 'Utah', 'Germany', 'China', 'Japan']

# ● Print your list in its original order.

print(travel_wishlist)

# ● Use the sort() function to arrange your list in order and reprint your list.

travel_wishlist.sort()
print(travel_wishlist)

# ● Use the sort(reverse=True) and reprint your list.

travel_wishlist.sort(reverse=True)
print(travel_wishlist)


# Q4.Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time.

# Create dictionaries for course numbers with nested dictionaries for course details.
# The course details dictionaries are nested so that calling the course number will return all details.

course_details = {
    '602': {
        'room': 'Room 1',
        'instructor': 'Harry George',
        'meeting_time': '9:00 AM'
    },
    '624': {
        'room': 'Room 2',
        'instructor': 'Mary Johnson',
        'meeting_time': '10:00 AM'
    }
}

# Prompt user for course number and display course details if available.
def get_course_details():
    available_courses = ', '.join(course_details.keys())   
    print(f'Courses available: {available_courses}')   # Display available courses
    course_number = input('Enter course number to see course details: ')

# Access the nested dictionaries based on course number input
    if course_number in course_details:
        print(f"Course Number: {course_number}")
        print(f"Room Number: {course_details[course_number]['room']}")
        print(f"Instructor: {course_details[course_number]['instructor']}")
        print(f"Meeting Time: {course_details[course_number]['meeting_time']}")
    else:
        print('Course not found')
        get_course_details()   # Restart function if course not found


get_course_details()


# Q5. Write a program that keeps names and email addresses in a dictionary as
# key-value pairs. The program should then demonstrate the four options:
#   ● look up a person’s email address,
#   ● add a new name and email address,
#   ● change an existing email address, and
#   ● delete an existing name and email address.

contacts = {'Alex Ptacek': 'alexptacek@gmail.com',
            'Harry George': 'harrybarry@gmail.com',
            'Mary Johnson': 'maryhadalittlelamb@gmail.com'}

# Create multiple menus for user to navigate, select desired action, and engage
# with contacts dictionary
def contacts_menu():
    print('Please select from the following options:')
    print('1. Look up a person\'s email address')
    print('2. Add a new name and email address')
    print('3. Change an existing email address')
    print('4. Delete an existing name and email address')
    print('5. Quit')

# If statements in each function in case user inputs invalid name
def get_email():
    print('Enter full name of contact')
    name = input()
    if name not in contacts:
        print('Contact not found')
    else:
        print (f'{name}\'s email address is {contacts[name]}')

def add_contact():
    print('Enter full name of new contact')
    name = input()
    if name in contacts:
        print('Contact already exists')
    else:
        print('Enter email address')
        email = input()
        contacts[name] = email
        print(f'{name} has been added to contacts')

def change_contact():
    print('Enter full name of contact')
    name = input()
    if name not in contacts:
        print('Contact not found')
    else:
        print('Enter new email address')
        email = input()
        contacts[name] = email
        print(f'{name}\'s email address has been updated')

def delete_contact():
    print('Enter full name of contract')
    name = input()
    if name not in contacts:
        print('Contact not found')
    else:
        del contacts[name]
        print(f'{name} has been deleted from contacts')


# while loop connects all the menus and keeps program running until user wants to quit
done = False
while not done:
    contacts_menu()

    selected = input()

    if selected == '1':
        get_email()

    elif selected == '2':
        add_contact()
    
    elif selected == '3':
        change_contact()

    elif selected == '4':
        delete_contact()

    elif selected == '5':
        done = True

    else:
        print('Invalid selection. Please try again.')

print('End of program')