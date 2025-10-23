import pandas as pd 
import ecommerce as ec #Ta bort vid renskrivning
data = ec.df_clean #Ta bort vid renskrivning











# Skapar en funktion för att räkna ut revenue/kategori 
def revenue_per_category(data):
    return (data.groupby("category", dropna=False, observed = True)
               .agg( 
                   total_intäkt= ("revenue", "sum"), #viktigast att räkna ut 
                   antal_köp = ("revenue", "count"), #med i dok
                   medel_intäkt_per_köp = ("revenue", "mean"), #med i dok 
                   median_intäkt_per_köp = ("revenue", "median"), 
                   lägsta_köp = ("revenue", "min"), 
                   högsta_köp = ("revenue", "max")                                
               ).reset_index()
               )

rpd = revenue_per_category(data)  #Ta bort vid renskrivning

#rpd.to_csv("data/revenue_per_category.csv", index=False) # Gör data till en  filen, Ta bort vid renskrivning