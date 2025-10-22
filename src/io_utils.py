import pandas as pd
import os

df = pd.read_csv("data/ecommerce_sales.csv") 

"""Fick inte pathway att fungera externt, googlade och tog hjälp av:
https://saturncloud.io/blog/how-to-open-files-in-a-data-folder-with-pandas-using-relative-path/ """

print(df.head())