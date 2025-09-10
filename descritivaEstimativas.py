# # Descritiva          08/09/2025
#                       
#
# Ordem
# 1. Média      //média ponderada
# 2. Mediana    //mediana ponderada
# 3. Moda
# 4. Variância
# 5. Desvio padrão
# 6. Histograma

# > Dependendo do cenário você vai precisar usar média ponderada ou mediana ponderada, isso só funciona caso você tenha dados heterogenicos.

# > A estatística é pura interpretação de cenário


import numpy as np
import scipy.stats as stats
import pandas as pd

# Dados de exemplo
dados = [10, 20, 30 , 40 ,50 , 100, 150, 200, 300, 500] # População

### Média (mean)
media = np.mean(dados)

###  MÉDIA PONDERADA (weighted mean)
pesos = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3]
media_ponderada = np.average(dados, weights=pesos) # tenho 2 conjutos para interajir para tirar a média ponderada


### Mediana (median)
mediana = np.median(dados)

### MEDIANA PONDERADA
def mediana_ponderada(dados, pesos):
    dados_ordenados, pesos_ordenados = zip(*sorted(zip(dados, pesos)))
    soma_pesos = np.cumsum(pesos_ordenados)     #cumsum = soma acumulativa
    return dados_ordenados[np.searchsorted(soma_pesos, soma_pesos[-1]/2)]

mediana_ponderada = mediana_ponderada(dados, pesos)

### MÉDIA APARADA (trimed mean) - Remove os 10% menores e maiores valores
media_aparada = stats.trim_mean(dados, proportiontocut=0.1)   # Proporção de corte = 10%

### IQR (Interquartile= Range) - intervalo interquartil - Intervalo Interquartilico (quartil)
p25, p75 = np.percentile(dados, [25, 75]) #0,25 e 0.75 é o valor que vai dividir o desenho gráfico, não necessariamente teremos 25% de dados fora
iqr = p75 - p25   # Intervalo Q2 de dados

### DETEÇÃO DE OUTLIERS COM IQR
limite_inferior = p25 - 1.5 * iqr
limite_superior = p75 + 1.5 * iqr
outliers = [x for x in dados if x < limite_inferior or x > limite_superior]

### VARIÂNCIA (variance)
variancia = np.var(dados) # não tenho uma unidade 'boa'; unidade vai ser quadrática

### DEVIO PADRÃO AMOSTRAL - em inglês(sample stardard deviation)
desvio_padrao_amostral = np.std(dados, ddof=0)  # ddof=1 ->  amostral # ddof = grau de liberdade (tem haver com o error que eu posso aceitar na minha amostra)

### DESVIO PADRÃO POPULACIONAl (population stardard deviation)
desvio_padrao_populacional = np.std(dados, ddof=0) # ddof=0 = não adimito erros aqui

### AMPLITUDE (range)
amplitude = np.max(dados) - np.min(dados)

### ESTATISTICA ORDINAILS - Moda (mode)
moda = stats.mode(dados, keepdims=True).mode[0]

### PENCENTIL (ex: Qual amostra está presente em 90%)
percentil_90 = np.percentile(dados, 90)

### QUARTIL (Exemplo: quantil 0.25 = Q1)
quantil_25 = np.percentile(dados, 0.25)   # 0.25 primeiro Quartil, 0.50 segundo quartil

### DESVIO ABSOLUTO MEDIANO DA MEDIANA (MAD) - desvio padrão em relação a mediana
mad = stats.median_abs_deviation(dados)

### VALOR ESPERADO (EV) - Esperança

# Exibir resultados
estatisticas = {
    'Média': media,
    'Média Ponderada': media_ponderada,
    'Mediana': mediana,
    'Mediana Ponderada': mediana_ponderada,
    'Média aparada': media_aparada,
    'IQR': iqr,
    'Outliers (IQR)': outliers,
    'Variância': variancia,
    'Desvio Padrão Amostral': desvio_padrao_amostral,
    'Desvio Padrão Populacional': desvio_padrao_populacional,
    'Amplitude': amplitude,
    'Moda': moda,
    '90° Percentil': percentil_90,
    'Quartil 25%': quantil_25,
    'Desvio Absoluto Mediano (MAD)': mad,
    'Valor Esperado': 'Não aplicável'
}

# Exibir estatistica em formato tabular
df_estatisticas = pd.DataFrame.from_dict(estatisticas, orient='index', columns=['Valor'])
print(df_estatisticas)