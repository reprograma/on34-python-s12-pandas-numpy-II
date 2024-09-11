import pandas as pd

df = pd.read_csv('./data_sample_RJ.csv', sep=';', encoding='latin-1', on_bad_lines='skip')

df = df.drop_duplicates()

minha_regiao = df.query("ESTACAO in ('MACAE')")

colunas_selecionadas = [
    'TEMPERATURA DO AR - BULBO SECO. HORARIA (C)',
    'TEMPERATURA DO PONTO DE ORVALHO (C)',
    'PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO. HORARIA (mB)'
]

for coluna in colunas_selecionadas:
    minha_regiao[coluna] = pd.to_numeric(minha_regiao[coluna])

df_sem_nulos = minha_regiao[colunas_selecionadas].dropna()

amostra = df_sem_nulos.sample(n=100, random_state=1)

print(amostra)