# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

def main():
    # Faz a leitura do arquivo
    input_file = 'bridges.data.version2'
    df = pd.read_csv(input_file, # Nome do arquivo com dados
                     names =['IDENTIF','RIVER','LOCATION','ERECTED','PURPOSE','LENGTH', 'LANES', 'CLEAR-G', 'T-OR-D', 'MATERIAL', 'SPAN', 'REL-L','TYPE'], # Nome das colunas 
                     usecols = ['LOCATION','LANES'], # Define as colunas que serão  utilizadas
                     na_values='?') # Define que ? será considerado valores ausentes
    
    # Imprime as 15 primeiras linhas do arquivo
    print("PRIMEIRAS 15 LINHAS\n")
    print(df.head(15))
    print("\n")

    # Imprime informações sobre dos dados
    print("INFORMAÇÕES GERAIS DOS DADOS\n")
    print(df.info())
    print("\n")

    # Imprime uma analise descritiva sobre dos dados
    print("DESCRIÇÃO DOS DADOS\n")
    print(df.describe())
    print("\n")

    # Imprime a quantidade de valores faltantes por coluna
    print("VALORES FALTANTES\n")
    print(df.isnull().sum())
    print("\n")


    # Tratando valores faltantes da coluna Density
    print("VALORES FALTANTES DA COLUNA Density\n")
    print('Total valores ausentes: ' + str(df['LOCATION'].isnull().sum()))

    method = 'mode' # number or median or mean or mode

    if method == 'number':
        # Substituindo valores ausentes por um número
        df['LOCATION'].fillna(125, inplace=True)

        # Substituindo valores de linhas específicas por um numero
        df.loc[2,'LOCATION'] = 125

    elif method == 'median':
        # Substituindo valores ausentes pela mediana 
        median = df['LOCATION'].median()
        df['LOCATION'].fillna(median, inplace=True)

    elif method == 'mean':
        # Substituindo valores ausentes pela média
        mean = df['Density'].mean()
        df['Density'].fillna(mean, inplace=True)    
      
    elif method == 'mode':
        # Substituindo valores ausentes pela moda
        mode = df['LOCATION'].mode()[0]
        print(mode)
        df['LOCATION'].fillna(mode, inplace=True)    
    
    
    print('Total valores ausentes: ' + str(df['LOCATION'].isnull().sum()))
    print(df.describe())
    print("\n")

    print("\n")
    

if __name__ == "__main__":
    main()