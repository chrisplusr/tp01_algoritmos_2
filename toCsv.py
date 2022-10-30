import pandas as pd

file = pd.read_csv('poker.dat', sep=',')
file.to_csv('poker.csv', index=None)
