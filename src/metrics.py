import pandas as pd 


def revenue_per_category(df):
    """
    Räknar ut intäkt per kategori
    """
    return (df.groupby("category", dropna=False, observed = True)
               .agg( 
                   total_intäkt= ("revenue", "sum"),                              
               ).reset_index()
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

def aov(df):
    return df["revenue"].mean()

def aov_varians(df):
    return df["revenue"].std()




def revenue_per_city(df):
    """
    Tar fram intäkt per stad 
    """
    return (df.groupby("city", dropna=False, observed = True)
               .agg( 
                   total_intäkt= ("revenue", "sum"),                                
               ).reset_index()
               )


def change_over_time(df):
    """
    Förändringar i intäkt över tid
    """
    return (df.groupby("month", dropna=False, observed=True)
            .agg(
                revenue = ("revenue", "sum"),
            ).reset_index()
            )
def find_outliers(df, kolumn='revenue', grupp=None, tröskel=2, observed=True):
    """
    Hittar avvikelser i ett dataset.
    """
    if grupp is None:
        medel = df[kolumn].mean()
        std = df[kolumn].std()
        avvikelser = df[(df[kolumn] > medel + tröskel * std) |
                        (df[kolumn] < medel - tröskel * std)]
        return avvikelser
    else:
        grupper = df.groupby(grupp)[kolumn].sum()
        medel = grupper.mean()
        std = grupper.std()
        avvikande_grupper = grupper[(grupper > medel + tröskel * std) |
                                    (grupper < medel - tröskel * std) ]
        return avvikande_grupper


def summarize_outliers(df, observed = True):
    """
    Ger en sammanfattning av eventuella avvikelser:
    """
    revenue_avvikelser = find_outliers(df, 'revenue')
    hög_intäkt_kategorier = find_outliers(df, 'revenue', grupp='category')
    hög_intäkt_stader = find_outliers(df, 'revenue', grupp='city')

    return revenue_avvikelser, hög_intäkt_kategorier, hög_intäkt_stader