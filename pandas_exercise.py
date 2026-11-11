import pandas as pd

dados = [10, 20, 30, 40, 100]

series = pd.Series(dados, index = ['a', 'b', 'c', 'd', 'e'])

print("\n", series.describe())