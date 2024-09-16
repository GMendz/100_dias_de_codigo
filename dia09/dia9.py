import pandas as pd
import numpy as np

media = df['vendas'].mean()
mediana = df['vendas'].median()
desvio_padrao = df['vendas'].std()
maximo = df['vendas'].max()
minimo = df['vendas'].min()

print(f"Média das vendas: {media:.2f}")
print(f"Mediana das vendas: {mediana:.2f}")
print(f"Desvio padrão das vendas: {desvio_padrao:.2f}")
print(f"Valor máximo das vendas: {maximo:.2f}")
print(f"Valor mínimo das vendas: {minimo:.2f}")

descricao = df['vendas'].describe()
print("\nEstatísticas descritivas completas:")
print(descricao)