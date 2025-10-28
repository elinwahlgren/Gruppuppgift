import matplotlib.pyplot as plt 
import pandas as pd


def line (ax, x, y, title, xlabel, ylabel, grid: bool = True):
    ax.plot(x, y, marker = "o")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid)
    plt.tight_layout()
    return ax
