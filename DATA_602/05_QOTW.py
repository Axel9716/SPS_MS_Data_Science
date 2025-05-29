# 1. Write a Python class to reverse a string word by word.
# Example:
# Input string : 'hello .py'
# Expected Output : '.py hello'

import string as pystring

class ReverseWord:

    def reverse_word(self, string):

# Found this neat attribute `punctuation` from module `string` which contains a string of
# punctuation characters. The .translate and .maketrans methods of python's built-in string class 
# work together to read a string (in this case, pystring.punctuation) and remove those characters
# from our variable string. In this case, it also removes the period from ".py", which was not the
# desired effect, but is more versatile, in my opinion.
        self.string = string.translate(str.maketrans("", "", pystring.punctuation))

        self.string_list = self.string.split()    #splits strings by whitespace

# The slicing argument for a list has 3 parameters: start, stop, step. By omitting start and 
# stop (simply putting ::), the slicing argument will read the whole list by default. Lastly, 
# putting -1 as the step parameter reads the list in reverse (the default for step is 1).
        self.reverse_string_list = self.string_list[::-1]

        return " ".join(self.reverse_string_list) #rejoin reversed list into single string


rw = ReverseWord()

print(rw.reverse_word("hello .py"))
#Output: "py hello"

print(rw.reverse_word("test a is this!"))
#Output: "this is a test"

print(pystring.punctuation)
#Output: "!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


# 2. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

import math

class Circle:

# Initialize the radius attribute with a default value of 0
    def __init__(self, radius=0):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius**2, 2)
    
    def perimeter(self):
        return round(2*math.pi*self.radius, 2)
    

test_circ = Circle(3.5)

print(test_circ.area())
#Output: 38.48

print(test_circ.perimeter())
#Output: 21.99