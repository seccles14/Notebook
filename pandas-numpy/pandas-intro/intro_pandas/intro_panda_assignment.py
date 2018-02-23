# Numpy is generally used for making fancier lists called arrays and series.
import numpy as np

# Pandas is super important, it's the foundation data analysis library we're using.
import pandas as pd

# Matplotlib is the python plotting library and folks generally import it as "plt"
import matplotlib.pyplot as plt

# Seaborn is a wrapper for Matplotlib and makes some things easier, generally imported as "sns"
import seaborn as sns


database = 'data/winequality-red.csv'
df = pd.read_csv(database, delimiter=';')


#how many rows and columns are in the DataFrame
df.shape

#what data type is in each column
df.info()

df.describe()

#part2
