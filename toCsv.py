import pandas as pd

file = pd.read_csv('iris.dat', sep=',')
file.to_csv('iris.csv', index=None)
