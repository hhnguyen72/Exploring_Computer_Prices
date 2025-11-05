import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def opening_csv():
    '''Open the CSV as Dataframe'''
    df = pd.read_csv('../data/computer_prices_all.csv')
    df_copy = df.copy
    return df_copy

def df_size(df_copy):
    return f' columns, row: {df.shape}, Elements: {df.size}'
