from feature import *
import pandas as pd
import numpy as np

# Read and merge multiple CSV files ---
# List of CSV filenames
csv_files = [f"data.2025100{i}.csv" for i in range(5, 10)]

# Read each CSV into a DataFrame and collect them
df_list = []
for file in csv_files:
    print(f"Reading {file} ...")
    df_temp = pd.read_csv(file)
    df_list.append(df_temp)

# Concatenate all data into one DataFrame
df_data = pd.concat(df_list, ignore_index=True)
print(f"Combined dataset shape: {df_data.shape}")

# Compute the feature for each row using a loop ---
feature_values = []
for i, row in df_data.iterrows():
    feature_values.append(get_feature_value(row))

# Store feature values in the DataFrame ---
df_data["OBI"] = feature_values

# Compute correlation with target Y ---
correlation = df_data["OBI"].corr(df_data["Y"])
print(f"Correlation between OBI and Y: {correlation:.4f}")
