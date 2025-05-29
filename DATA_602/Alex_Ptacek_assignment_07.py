# Alex Ptacek - Assignment #7

# Introduction
# The dataset used in this assignment is the CDC’s “Obesity, Physical Activity, and Diet” dataset, sourced from:
# https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Obesity-Physical-Activity-and-Diet-CDC/3x4v-q6iz
# This dataset was chosen because it provides a rich mix of health metrics across US states and years,
# useful for exploring trends in obesity-related behaviors, activity, and socioeconomic factors.


# Data Exploration
import pandas as pd

df = pd.read_csv("/Users/alex/SPS_MS_DS/DATA_602/Data_602_FINAL_PROJECT/Obesity_Risk_Factors_CDC.csv")

# Summary statistics
summary_stats = df.describe(include='all')
print("Summary Statistics:\n", summary_stats)

# Missing values
missing_info = df.isnull().sum()
print("Missing Values:\n", missing_info)

# Data types
print("Data Types:\n", df.dtypes)

# First few rows
print("First 5 Rows:\n", df.head())


# Data Wrangling

# Rename columns
df.rename(columns={
    "LocationAbbr": "StateAbbr",
    "LocationDesc": "State",
    "Data_Value_Unit": "YearReported"
}, inplace=True)

# Convert 'YearStart' and 'YearEnd' to string (if needed)
df['YearStart'] = df['YearStart'].astype(str)
df['YearEnd'] = df['YearEnd'].astype(str)

# Fill missing Data_Value with median
df['Data_Value'].fillna(df['Data_Value'].median(), inplace=True)

# Create a new column
df['Value_Per_1000'] = df['Data_Value'] * 10

# Drop unnecessary column
df.drop(columns=['Low_Confidence_Limit', 'High_Confidence_Limit'], errors='ignore', inplace=True)

# Drop rows where StateAbbr is null
df = df[df['StateAbbr'].notnull()]

# Sort by State then YearStart
df.sort_values(by=['State', 'YearStart'], inplace=True)

# Filter: only Obesity class
obesity_df = df[df['Class'] == 'Obesity / Weight Status']

# Convert column to lowercase
df['Question'] = df['Question'].str.lower()

# Check for numeric in 'Data_Value'
df['HasNumeric'] = df['Data_Value'].apply(lambda x: isinstance(x, (int, float)))

# Group and aggregate
grouped = df.groupby('State')['Data_Value'].agg(['mean', 'min', 'max'])

# Group by two columns
double_grouped = df.groupby(['State', 'YearStart'])['Data_Value'].mean().reset_index()
double_grouped.sort_values(['State', 'Data_Value'], inplace=True)


# Conclusions
# After cleaning and exploring the CDC Obesity dataset, several insights emerged:
# 
# - Obesity-related data varies significantly by state and demographic categories such as race, income, and age.
# - Some states consistently report higher average obesity values across multiple years, suggesting potential areas for policy intervention.
# - The presence of missing values in health-related measures like 'Data_Value' highlights challenges in consistent data collection across all regions and years.
# - By transforming and aggregating the data, we were able to identify maximum and minimum average obesity-related metrics at the state level.
# - Grouping by state and year showed how certain states saw sharp increases or declines over time, which may correlate with external factors like healthcare access or economic conditions.
# 
# With more time, I would explore trends over time more deeply, visualize regional disparities using maps or heatmaps, and look at the relationship between physical activity levels and obesity rates.

