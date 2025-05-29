#Alex Ptacek - QOTW #7

import pandas as pd

# 1. What is pandas and why use it?

# Pandas is a python module that helps us create and work with tabular data. Pandas contains two important methods for
# this purpose: Series, a labelled 1d numpy array, and DataFrame, a tabular data structure the uses pandas Series as columns.
# Tabular data is a very convenient format for working with data. This structure allows for easy subsetting and mutation of data.


# 2. Give an example of how to import a csv file using pandas

# This is a small practice dataset that I downloaded. The data comes with an index, so I specified this in the index_col parameter.
df = pd.read_csv("/Users/alex/Downloads/people-100.csv", index_col = 0)


# 3. Show how to view the first 10 rows of a dataset using pandas

# Both of these methods achieve the same result, but the iloc method is also good for subsetting columns at the same time.
print(df.iloc[0:10, :])

print(df.head(10))


# 4. Write a Pandas program to compare the elements of the two Pandas Series.
# Sample Series: 

# First, convert sample lists to pandas series
s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 10])

print(s1 == s2)

print(s1.compare(s2))


# 5. Change the first character of each word to upper case in each word of df1

df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])

# .str.capitalize method captializes the first word of every string in a Series
print(df1.str.capitalize())
