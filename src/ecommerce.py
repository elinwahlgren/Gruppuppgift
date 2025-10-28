import pandas as pd


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
        self.df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()
        return self.df
