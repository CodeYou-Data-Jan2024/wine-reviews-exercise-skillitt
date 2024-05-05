# add your code here.

import pandas as pd

# Path to the CSV file
csv_file_path = "data/winemag-data-130k-v2.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Display the first few rows of the DataFrame
print(df.head())
