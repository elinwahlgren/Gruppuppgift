import pandas as pd
import io_utils as io

df =io.df

# print(df.info())
# print()
# print(df.isna().sum())
# print()
# print(df.dtypes)
# print()
# print("Dubblettrader:", df.duplicated().sum())
# print()
# print("Dubblettordernummer:", df["order_id"].duplicated().sum())
# print()
# print(df["city"].nunique())
# print()
# print(df["category"].nunique())

class EcommerceAnalyzer:
    def __init__(self, df):
        self.df = df

    def clean_df(self):
        self.df.columns = (self.df.columns.str.strip().str.replace(" ", "_").str.lower())
        self.df["category"] = self.df["category"].astype("category")
        self.df["city"] = self.df["city"].astype("category")
        self.df["date"] = pd.to_datetime(self.df["date"], dayfirst=False, errors="coerce")
        return self.df
    
    def add_month(self):
        self.df["month"] = df["date"].dt.month #Källa https://www.youtube.com/watch?v=vnTWXn9LtHM Python ML Daily
        return self.df

df_clean = EcommerceAnalyzer(df).clean_df() # lägg till i notebook 
df_clean_month = EcommerceAnalyzer(df_clean).add_month()

# print(df_clean.head())
# print(df_clean_month.head())


# print(df.dtypes)