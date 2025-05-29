# QOTW #3 - Alex Ptacek

# 1. Create a list called animals that contain the following: cat, dog, manta ray, horse, crouching tiger

animals = ['cat', 'dog', 'manta ray', 'horse', 'crouching tiger']


# 2. Repeat question 1 and loop through and print each item in the animal list by iterating through an index number and using range().
# Set a variable len_animals to the length of the animal list.

animals = ['cat', 'dog', 'manta ray', 'horse', 'crouching tiger']
len_animals = len(animals)

# use len_animals as index, loop through to print each index number and corresponding animal
for index in range(len_animals):
    print(index, animals[index])


# 3. Programmatically reorganize the countdown list below in descending order and return the value of the 5th element in the sorted countdown list.
#     The 5th element will be stored in the variable the_fifth_element, which currently below has a dummy value of -999.
#     Remember, the index number of the 5th element is not 5

countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
the_fifth_element = -999

# create function to sort countdown and return the 5th element, so that it can be stored in a new variable
def sort_and_pull_fifth(countdown):
    sorted_countdown = sorted(countdown, reverse=True)
    return sorted_countdown[4]

the_fifth_element = sort_and_pull_fifth(countdown)
print(the_fifth_element)


# 4. Write a program to add item 7000 after 6000 in the following Python List

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# access the 3rd item of the 3rd item of list1 and use append to add 7000 at the end
list1[2][2].append(7000)

print(list1)


# 5. Write a program to remove all occurrences of item 20 in the following list.

list2 = [5, 20, 30, 15, 20, 30, 20]

# checks if any values are equal to 20, and removes them
for i in list2:
    if i == 20:
        list2.remove(i)

print(list2)


# 6. Using the following dictionary .. (Use python to solve for the answer.)

dict = {"Course": "DATA 606", "Program": "MSDS", "School": "CUNYSPS"}

# a. What is the name of the course?

print(dict["Course"])

# b. Change the course to DATA602

dict["Course"] = "DATA602"

# c. Add new information to the dictionary - "Professor" with "Schettini"

dict["Professor"] = "Schettini"

# d. Using the len function, find how many keys there are in the dictionary. 

print(len(dict))


# 7.  Write a Python program to change Brad’s salary to 7500 in the following dictionary.

# access salary key inside emp3 key to change value
sample_dict = {
    'emp1': {'name': 'Amanda', 'salary': 8200},
    'emp2': {'name': 'John', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 700}
}

sample_dict['emp3']['salary'] = 7500