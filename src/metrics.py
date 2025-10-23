import pandas as pd

def top_categories(df, n=3):
    return(df.groupby("category", observed=True)["revenue"]
           .sum()
           .sort_values(ascending=False)
           .head(n)
           .round(0)
           .astype(int)
        )
