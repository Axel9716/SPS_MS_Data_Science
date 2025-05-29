# Q1 Fix all the syntax and logical errors in the given source code
# add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the
# average is a high score. The high score variable holds the value that is considered a high score.

high_score = 95

# Get the test scores.
# Add input for test3 score
# Add the parentheses around additives in `average` function so the order of operations is correct
# change `high_score` to lower snake case to fix naming convention
# Convert test score variables to floats to allow for division
test1 = float(input("Enter the score for test 1: "))
test2 = float(input("Enter the score for test 2: "))
test3 = float(input("Enter the score for test 3: "))
# Calculate the average test score.
average = (test1 + test2 + test3) / 3
# Print the average.
print("The average score is", average)
# If the average is a high score,
# congratulate the user.
if average >= high_score:
    print("Congratulations!")
print("That is a great average!")

# Q2
# The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles.

# Measurements for rectangle 1
length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))

# Measurements for rectangle 2
length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))

# Print the area of both rectangles
print("The area of the first rectangle is: ", length1 * width1)
print("The area of the second rectangle is: ", length2 * width2)

