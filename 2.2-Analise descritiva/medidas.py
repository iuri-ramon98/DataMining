import pandas as pd
import numpy as np
input_file = '../1-DataSets/regiao1_limpo_mean.data'
names = ['Dia','Mes','Ano','Temperatura','RH','WS','Chuva','FFMC','DMC','DC','ISI','BUI','FWI','Classes'] 
features = ['Temperatura','RH','WS','Chuva','FFMC','DMC','DC','ISI','BUI','FWI', 'Classes']

df = pd.read_csv(input_file,    # Nome do arquivo com dados
                 names = names) # Nome das colunas  
    
print("Medidas de tendência central")

print("\n")
print("Média")
print("\n")    

print("Media Temperatura: ",df['Temperatura'].mean())
print("Media RH: ",df['RH'].mean())
print("Media WS: ",df['WS'].mean())
print("Media Chuva: ",df['Chuva'].mean())
print("Media FFMC: ",df['FFMC'].mean())
print("Media DMC: ",df['DMC'].mean())
print("Media DC: ",df['DC'].mean())
print("Media ISI: ",df['ISI'].mean())
print("Media BUI: ",df['BUI'].mean())
print("Media FWI: ",df['FWI'].mean())

print("\n")
print("Moda")
print("\n")    

print("Moda Temperatura: ",df['Temperatura'].mode())
print("Moda RH: ",df['RH'].mode())
print("Moda WS: ",df['WS'].mode())
print("Moda Chuva: ",df['Chuva'].mode())
print("Moda FFMC: ",df['FFMC'].mode())
print("Moda DMC: ",df['DMC'].mode())
print("Moda DC: ",df['DC'].mode())
print("Moda ISI: ",df['ISI'].mode())
print("Moda BUI: ",df['BUI'].mode())
print("Moda FWI: ",df['FWI'].mode())

print("\n")
print("Medidas de dispersão")
print("\n")
print("Amplitude")
print("\n")

print("Amplitude Temperatura: ",df['Temperatura'].min(), " - ", df['Temperatura'].max())
print("Amplitude RH: ",df['RH'].min(), " - ", df['RH'].max())
print("Amplitude WS: ",df['WS'].min(), " - ", df['WS'].max())
print("Amplitude Chuva: ",df['Chuva'].min(), " - ", df['Chuva'].max())
print("Amplitude FFMC: ",df['FFMC'].min(), " - ", df['FFMC'].max())
print("Amplitude DMC: ",df['DMC'].min(), " - ", df['DMC'].max())
print("Amplitude DC: ",df['DC'].min(), " - ", df['DC'].max())
print("Amplitude ISI: ",df['ISI'].min(), " - ", df['ISI'].max())
print("Amplitude BUI: ",df['BUI'].min(), " - ", df['BUI'].max())
print("Amplitude FWI: ",df['FWI'].min(), " - ", df['FWI'].max())

print("\n")
print("Variância")
print("\n")

print("Variância Temperatura: ",df['Temperatura'].var())
print("Variância RH: ",df['RH'].var())
print("Variância WS: ",df['WS'].var())
print("Variância Chuva: ",df['Chuva'].var())
print("Variância FFMC: ",df['FFMC'].var())
print("Variância DMC: ",df['DMC'].var())
print("Variância DC: ",df['DC'].var())
print("Variância ISI: ",df['ISI'].var())
print("Variância BUI: ",df['BUI'].var())
print("Variância FWI: ",df['FWI'].var())

print("\n")
print("Desvio Padrão")
print("\n")

print("Desvio padrão Temperatura: ",df['Temperatura'].std())
print("Desvio padrão RH: ",df['RH'].std())
print("Desvio padrão WS: ",df['WS'].std())
print("Desvio padrão Chuva: ",df['Chuva'].std())
print("Desvio padrão FFMC: ",df['FFMC'].std())
print("Desvio padrão DMC: ",df['DMC'].std())
print("Desvio padrão DC: ",df['DC'].std())
print("Desvio padrão ISI: ",df['ISI'].std())
print("Desvio padrão BUI: ",df['BUI'].std())
print("Desvio padrão FWI: ",df['FWI'].std())

print("\n")
print("Covariância")
print("\n")

print(df[features].cov())

print("\n")
print("Correlação")
print("\n")

print(df[features].corr())

dataFrame = pd.DataFrame(data=df[features])

kurt = dataFrame.kurt(axis=1)

print("Data:")

print(dataFrame)

print("Kurtosis:")

print(kurt) ##posteriormete jogar em um doc para visualização completa