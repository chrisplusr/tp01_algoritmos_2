import pandas as pd

file = pd.read_csv('banana.dat', sep=',')
file.to_csv('banana.csv', index=None)
