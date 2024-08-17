import pandas as pd

tabela1 = pd.read_csv('DadosHoras.csv')
print("Tabela Data e Hora: ")
print(tabela1)

print ("Tabela Data Sample")
tabela2 = pd.read_csv('data_sample_.csv', sep = ';')
print(tabela2)