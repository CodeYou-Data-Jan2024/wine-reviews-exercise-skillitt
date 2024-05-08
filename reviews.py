# add your code here.

import pandas as pd

# Path to CSV file
input_csv_path = "data/winemag-data-130k-v2.csv"

# Read the CSV file 
df = pd.read_csv(input_csv_path)

# Group the data by country and calculate the points
summary_df = df.groupby('country').agg({'country': 'count', 'points': 'mean'})

# Rename columns 
summary_df.rename(columns={'country': 'number_of_reviews', 'points': 'average_points'}, inplace=True)

# Reset index 
summary_df.reset_index(inplace=True)

# Round up the output CSV
summary_df['number_of_reviews'] = summary_df['number_of_reviews'].apply(lambda x: int(x) if x % 1 == 0 else int(x) + 1)
summary_df['average_points'] = summary_df['average_points'].apply(lambda x: round(x))

# output CSV file
output_csv_path = "data/reviews-per-country.csv"

# Write the summary data to a new CSV file
summary_df.to_csv(output_csv_path, index=False)


print("Summary data saved to reviews-per-country.csv")
