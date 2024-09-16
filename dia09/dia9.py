import pandas as pd
import numpy as np

dados = {'vendas': [100, 150, 200, 120, 90, 180, 250]}
df = pd.DataFrame(dados)

media = df['vendas'].mean()
mediana = df['vendas'].median()
desvio_padrao = df['vendas'].std()
maximo = df['vendas'].max()
minimo = df['vendas'].min()

print("Média das vendas:", media)
print("Mediana das vendas:", mediana)
print("Desvio padrão das vendas:", desvio_padrao)
print("Valor máximo das vendas:", maximo)
print("Valor mínimo das vendas:", minimo)