import pandas as pd 


def revenue_per_category(df):
    """
    Räknar ut intäkt per kategori
    """
    return (df.groupby("category", dropna=False, observed = True)
               .agg( 
                   total_intäkt= ("revenue", "sum"),                              
               ).reset_index().astype(int)
               )


def total_units(df):
    '''
    Tar fram antal enheter.
    '''
    return df["units"].sum()

def top_categories(df, n=3):
    """
    Tar fram de 3 största kategorierna 
    """
    return(df.groupby("category", observed=True)["revenue"]
           .sum()
           .sort_values(ascending=False)
           .head(n)
           .round(0)
           .astype(int)
        )


def revenue_per_city(df):
    """
    Tar fram intäkt per stad 
    """
    return (df.groupby("city", dropna=False, observed = True)
               .agg( 
                   total_intäkt= ("revenue", "sum"),                                
               ).reset_index().astype(int)
               )


def change_over_time(df):
    """
    Förändringar i inkomst över tid
    """
    return (df.groupby("month", dropna=False, observed=True)
            .agg(
                intäkt = ("revenue", "sum"),
            ).reset_index().astype(int)
            )
