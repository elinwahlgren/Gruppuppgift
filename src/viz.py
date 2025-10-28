import matplotlib as plt 
import pandas as pd
import numpy as np

def bar_top_categories(df, ax=None):
    summary = (df.groupby("category", dropna=False)
            .agg(
                    medel=("revenue", "mean"),
                    std=("revenue", "std"),
                    n=("revenue", "count")
                ).reset_index())

    se = summary["std"] / np.sqrt(summary["n"])

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(summary["category"], summary["medel"], yerr=se, capsize=4)
    ax.set_title("Medelintäkt per kategori")
    ax.set_xlabel("Kategori")
    ax.set_ylabel("Medelintäkt")
    ax.grid(True, axis="y")
    return ax

def boxplot_revenue_by_category(df, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8,5))
    df.boxplot(column="revenue", by="category", ax=ax)
    ax.set_title("Fördelning av intäkt per kategori")
    plt.suptitle("")
    ax.set_xlabel("Kategori")
    ax.set_ylabel("Intäkt")
    return ax

