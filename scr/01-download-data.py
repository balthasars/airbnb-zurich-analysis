# libraries
import pandas as pd

# get data from Inside Airbnb and save as CSV
url_1 = "http://data.insideairbnb.com/switzerland/z%C3%BCrich/zurich/2022-03-29/visualisations/listings.csv"

# read data from url and save as CSV
pd.read_csv(url_1).to_csv("data/listings.csv", index=False)

# add additional info

url_2 = "http://data.insideairbnb.com/switzerland/z%C3%BCrich/zurich/2022-03-29/data/listings.csv.gz"
pd.read_csv(url_2, compression='gzip').to_csv("data/listings_detailed.csv", index=False)
