# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

def main():
    # Faz a leitura do arquivo
    input_file = 'bridges.data.version2'
    output_file = 'bridges.data.version2clean'
    df = pd.read_csv(input_file, # Nome do arquivo com dados
                     names =['IDENTIF','RIVER','LOCATION','ERECTED','PURPOSE','LENGTH', 'LANES', 'CLEAR-G', 'T-OR-D', 'MATERIAL', 'SPAN', 'REL-L','TYPE'], # Nome das colunas 
                     usecols = ['LOCATION'], # LOCATION Define as colunas que serão  utilizadas
                     na_values='?') # Define que ? será considerado valores ausentes
    
    df_original = df.copy()
    
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
        mean = df['LOCATION'].mean()
        df['LOCATION'].fillna(mean, inplace=True)    
      
    elif method == 'mode':
        # Substituindo valores ausentes pela moda
        mode = df['LOCATION'].mode()[0]
        print(mode)
        df['LOCATION'].fillna(mode, inplace=True)    
    
    
    columns_missing_value = df.columns[df.isnull().any()]
    print(columns_missing_value)
    method = 'mode' # number or median or mean or mode
    
    for c in columns_missing_value:
        UptateMissingvalue(df, c)
    
    print('Total valores ausentes: ' + str(df['LOCATION'].isnull().sum()))
    print(df.describe())
    print("\n")
    print(df.head(15))
    print(df_original.head(15))
    print("\n")
    
    # Salva arquivo com o tratamento para dados faltantes
    df.to_csv(output_file, header=False, index=False)  
    

def UptateMissingvalue(df, column, method="mode", number=0):
    if method == 'number':
        # Substituindo valores ausentes por um número
        df[column].fillna(number, inplace=True)
    elif method == 'median':
        # Substituindo valores ausentes pela mediana 
        median = df['LOCATION'].median()
        df[column].fillna(median, inplace=True)
    elif method == 'mean':
        # Substituindo valores ausentes pela média
        mean = df[column].mean()
        df[column].fillna(mean, inplace=True)
    elif method == 'mode':
        # Substituindo valores ausentes pela moda
        mode = df[column].mode()[0]
        df[column].fillna(mode, inplace=True)
    
    #print('Total valores ausentes: ' + str(df['LOCATION'].isnull().sum()))
    #print(df.describe())
    #print("\n")

    #print("\n")
    
    
    

if __name__ == "__main__":
    main()