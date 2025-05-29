# Alex Ptacek - QOTW #8

import pandas as pd

# 1. How would you delete:

    # An index from your dataframe

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['x', 'y'])
df_reset = df.reset_index(drop=True)
print(df)
print(df_reset)

    # A column from your dataframe

df = df.drop('B', axis=1)
print(df)

    # A row from your dataframe

df = df.drop('x', axis=0)
print(df)


# 2. How do you iterate over a pandas dataframe?

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['x', 'y'])

for index, row in df.iterrows():
    print(f"Index: {index}, A: {row['A']}")


# 3. How would you convert a string to a date?

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4],
                   'Date': ["2025-05-11", "2025-05-12"]}, index=['x', 'y'])

df['Date'] = pd.to_datetime(df['Date'])
print(df['Date'].dtype)


# 4. What is data aggregation?  Give an example in Python. 

# Answer: Data aggregation is the process of combining data from different sources or summarizing/calculating data in a dataset

df = pd.DataFrame({'group': ['A', 'A', 'B'], 'value': [10, 20, 30]})
average_value = df['value'].mean()
print(average_value)

# 5. What is GroupBy in Pandas (groupby()). Give an example in Python.

# Answer: GroupBy is a method of pandas that we can use to group data by a certain variable and summarize a metric for that variable

grouped = df.groupby('group').mean()
print(grouped)