import pandas as pd


class EcommerceAnalyzer:
    def __init__(self, df):
        self.df = df

    def clean_df(self):
        df = self.df.copy()
        df.columns = (df.columns.str.strip().str.replace(" ", "_").str.lower())
        df["category"] = df["category"].astype("category")
        df["city"] = df["city"].astype("category")
        df["date"] = pd.to_datetime(df["date"], dayfirst=False, errors="coerce")
        return df
    
    def add_month(self):
        df = self.df.copy()
        df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()
        return df

