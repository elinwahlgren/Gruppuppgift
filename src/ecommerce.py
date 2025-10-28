import pandas as pd

class EcommerceAnalyzer:
    def __init__(self, df):
        self.df = df

    def clean_df(self):
        df=self.df.copy()
        df.columns = (df.columns.str.strip().str.replace(" ", "_").str.lower())
        df["category"] = df["category"].astype("category")
        df["city"] = df["city"].astype("category")
        df["date"] = pd.to_datetime(df["date"], dayfirst=False, errors="coerce")
        return df
    
    def add_month(self):
        df= self.df.copy()
        df["month"] = df["date"].dt.month #Källa https://www.youtube.com/watch?v=vnTWXn9LtHM Python ML Daily
        return df

#df_clean = EcommerceAnalyzer(df).clean_df() # lägg till i notebook 
#df_clean_month = EcommerceAnalyzer(df_clean).add_month()

# print(df_clean.head())
# print(df_clean_month.head())


# print(df.dtypes)