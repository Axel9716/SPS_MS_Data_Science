# Alex Ptacek - QOTW #6

import pandas as pd
import numpy as np

# 1. What are the similarities and differences between pandas and numpy?   Include some type of example with code.

# pandas dataframes are comprised of numpy arrays, but they have to be named
np_array = np.array([[10, 20, 30], [40, 50, 60]])

df = pd.DataFrame(np_array, columns=['A', 'B', 'Cat'])


# Both packages support indexing, but pandas also enables name-based indexing
print(np_array[1, 2])
#Output: 60

print(df.loc[1, 'Cat'])
#Output: 60



# 2. What is the ndarray in numPy?

# Answer: The ndarray in numPy is an n-dimensional array meaning you can stack >1 arrays on top of eachother
array_2d = np.array([[1, 2, 3], [4, 5, 6]])



# 3. Create a 1D array of numbers from 0 to 9 
# Desired Output: 
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

array_1d = np.array(range(10))

print(array_1d)



# 4. Extract all odd numbers from array1 
array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

odd_numbers = array1[array1 % 2 == 1]

print(odd_numbers)



# 5. Get the common items between a and  b  
# #input
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

# #Desired Output:

# array([2, 4])

#subset a and only keep unique values
c = np.unique(a[np.isin(a, b)])
print(c)



# 6. From array a remove all items present in array  b 
# #Input:

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

# #Desired Output:

# array([1,2,3,4])

# subset a using ~ to negate the matching function
c = a[~np.isin(a, b)]

print(c)



# 7. Find out if iris has any missing values. 
# # Input

import requests
import io

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# needed to uses requests to get data because original code wasn't working
response = requests.get(url)

# Load data into NumPy
iris = np.genfromtxt(io.StringIO(response.text), delimiter=',', dtype='float', usecols=[0, 1, 2, 3])

# Check if there are any missing (NaN) values in the dataset
missing_values = np.isnan(iris).any()

print(missing_values)
# No missing values