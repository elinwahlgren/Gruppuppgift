import matplotlib.pyplot as plt 
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
  
  def line (ax, x, y, title, xlabel, ylabel, grid: bool = True):
    ax.plot(x, y, marker = "o")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid)
    plt.tight_layout()
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

def revenue_by_city(df, ax=None):
    summary = (df.groupby("city", dropna=False)
            .agg(
                    medel=("revenue", "mean"),
                    std=("revenue", "std"),
                    n=("revenue", "count")
                ).reset_index())

    se = summary["std"] / np.sqrt(summary["n"])

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(summary["city"], summary["medel"], yerr=se, capsize=4)
    ax.set_title("Medelintäkt per stad")
    ax.set_xlabel("Stad")
    ax.set_ylabel("Medelintäkt")
    ax.grid(True, axis="y")
    return ax

def boxplot_revenue_by_city(df, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8,5))
    df.boxplot(column="revenue", by="city", ax=ax)
    ax.set_title("Fördelning av intäkt per stad")
    plt.suptitle("")
    ax.set_xlabel("Stad")
    ax.set_ylabel("Intäkt")
    return ax
