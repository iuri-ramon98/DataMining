import matplotlib.pyplot as plt
import pandas as pd
##from pandasUteis.pandas_utils import frequency_by_natural_order, frequency_by_buckets

input_file = '../1-DataSets/regiao1_limpo_mean.data'
names = ['Dia','Mes','Ano','Temperatura','RH','WS','Chuva','FFMC','DMC','DC','ISI','BUI','FWI','Classes']

df = pd.read_csv(input_file,    # Nome do arquivo com dados
                 names = names) # Nome das colunas  


"""
Criando um histograma para com os pesos dos alunos
"""
ws = df['FWI']

plt.figure(figsize=(10, 8))
plt.hist(ws, bins=range(0, 35, 2))
plt.title('Distribuição de FWI')
plt.xlabel('Fire Weather Index  indice FWI')
plt.ylabel('Dias')
plt.show()
##plt.savefig('imagens/peso-histograma.png')
##plt.close()