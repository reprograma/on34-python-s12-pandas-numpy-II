import pandas as pd

df = pd.read_csv('./data_sample_RJ.csv', sep=';', encoding='latin-1', on_bad_lines='skip')

df = df.drop_duplicates()

minha_regiao = df.query("ESTACAO in ('MACAE')")

colunas_temperatura = [
    'TEMPERATURA DO AR - BULBO SECO. HORARIA (C)',
    'TEMPERATURA DO PONTO DE ORVALHO (C)',
    'TEMPERATURA MAXIMA NA HORA ANT. (AUT) (C)',
    'TEMPERATURA MINIMA NA HORA ANT. (AUT) (C)',
    'TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (C)',
    'TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (C)'
]

for coluna in colunas_temperatura:
    minha_regiao[coluna] = pd.to_numeric(minha_regiao[coluna])

medias_temperaturas = minha_regiao[colunas_temperatura].mean()

print("Média das temperaturas:")
print(medias_temperaturas)
