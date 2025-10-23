import pandas as pd 


# Skapar en funktion för att räkna ut revenue/kategori 
def revenue_per_category(df):
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


def revenue_per_city(df):
    return (df.groupby("city", dropna=False, observed = True)
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

# funktion för att se förändringar i intäkt över tid 
def change_over_time(df):
    return (df.groupby("month", dropna=False, observed=True)
            .agg(
                intäkt = ("revenue", "sum"),
                antal_köp = ("order_id", "count"),
                medel_intäkt_köp = ("revenue", "mean")
            ).reset_index()
            )
def top_month(df):
    return(df.groupby("month", observed=True)["revenue"]
           .sum()
           .sort_values(ascending=False)
           .round(0)
           .astype(int)
        )


# import ecommerce as ec

# data = ec.df_clean_month
# print(top_month(data))