#!/usr/bin/env python


# required libraries
import pandas as pd


# initialize dataframe df
path="link to file"
df = pd.read_csv(path)

# Find variables with missing values in dataframe df:
variable_missing = [var for var in df.columns if df[var].isnull().sum() > 0]

# Find numerical variables
num_vars = [var for var in df.columns if df[var].dtypes != 'O']
print(df[num_vars].head())

