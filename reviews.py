# add your code here.

import pandas as pd

# Path to the input CSV file
input_csv_path = "data/winemag-data-130k-v2.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(input_csv_path)

# Group the data by country and calculate the count of reviews and average points
summary_df = df.groupby('country').agg({'country': 'count', 'points': 'mean'})

# Rename the columns for clarity
summary_df.rename(columns={'country': 'number_of_reviews', 'points': 'average_points'}, inplace=True)

# Reset index to make 'country' a column instead of an index
summary_df.reset_index(inplace=True)

# Path to the output CSV file
output_csv_path = "data/reviews-per-country.csv"

# Write the summary data to a new CSV file
summary_df.to_csv(output_csv_path, index=False)

print("Summary data saved to reviews-per-country.csv")
