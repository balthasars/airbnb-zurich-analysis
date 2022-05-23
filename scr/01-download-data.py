# libraries
import pandas as pd

# get data from Inside Airbnb and save as CSV
url = "http://data.insideairbnb.com/switzerland/z%C3%BCrich/zurich/2021-12-28/visualisations/listings.csv"

# read data from url and save as CSV
pd.read_csv(url).to_csv("data/listings.csv", index=False)