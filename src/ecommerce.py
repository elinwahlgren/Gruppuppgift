import pandas as pd
import io_utils as io

df =io.df

print(df.info())
print()
print(df.isna().sum())
print()
print(df.dtypes)
print()
print("Dubblettrader:", df.duplicated().sum())
print()
print("Dubblettordernummer:", df["order_id"].duplicated().sum())
print()
print(df["city"].nunique())
print()
print(df["category"].nunique())

class EcommerceAnalyzer:
    def __init__(self, df):
        self.df = df

    def clean_df(self):
        self.df.columns = (self.df.columns.str.strip().str.replace(" ", "_").str.lower())
        self.df["category"] = self.df["category"].astype("category")
        self.df["city"] = self.df["city"].astype("category")
        self.df["date"] = pd.to_datetime(self.df["date"], dayfirst=False, errors="coerce")
        return self.df

df_clean = EcommerceAnalyzer(df)   
print(df_clean.clean_df().head())

print(df.dtypes)