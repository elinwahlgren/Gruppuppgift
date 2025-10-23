import pandas as pd 


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


def top_categories(df, n=3):
    return(df.groupby("category", observed=True)["revenue"]
           .sum()
           .sort_values(ascending=False)
           .head(n)
           .round(0)
           .astype(int)
        )


def revenue_per_city(data):
    return (data.groupby("city", dropna=False, observed = True)
               .agg( 
                   total_intäkt= ("revenue", "sum"), #viktigast att räkna ut 
                   antal_köp = ("revenue", "count"), 
                   medel_intäkt_per_köp = ("revenue", "mean"), 
                   median_intäkt_per_köp = ("revenue", "median"), 
                   lägsta_köp = ("revenue", "min"), 
                   högsta_köp = ("revenue", "max")                                
               ).reset_index()
               )

def top_city(df):
    return(df.groupby("city", observed=True)["revenue"]
           .sum()
           .sort_values(ascending=False)
           .round(0)
           .astype(int)
        )


