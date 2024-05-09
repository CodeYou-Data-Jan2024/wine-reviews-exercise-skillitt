# add your code here.

# import pandas 
import pandas as pd

# Read wine mag data
wine_reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

# Group country, count and points
reviews_country = wine_reviews.groupby(['country']).points.agg([len, "mean"]).round(decimals=1)
reviews_country = reviews_country.rename(columns={"county": 'country', 'len': "count", 'mean': "points"})

# create a file to the data folder
reviews_country.to_csv("data/reviews-per-country.csv")
