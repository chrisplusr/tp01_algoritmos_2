import pandas as pd

file = pd.read_csv('titanic.dat', sep=',')
file.to_csv('titanic.csv', index=None)
