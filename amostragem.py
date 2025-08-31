#%%  Amostragem aleatória com 10mil linhas
import pandas as pd
import numpy as np

# Criando um dataframe ficticio
np.random.seed(42) # garante a reprodução do experimento
n = 10000 # Quantidade de clientes que queremos gerar dados ficticios

df1 = pd.DataFrame({
    "ID": range(1, n+1),
    "Idade": np.random.randint(18, 65, n),
    "Renda": np.random.randint(2000, 30000, n),
    "Regiao": np.random.choice(["Norte", "Sul", "Leste", "Oeste"], n)
})

df1.sample(5)
###############################################################################################################################################################################################################

#%%
## **Amostragem Aleatória Simples**

amostra_simples = df1.sample(n=1000, random_state=42) # Random State tem o mesmo papel do seed.
amostra_simples.head()

###############################################################################################################################################################################################################
#%%
## **Amostragem Aleatória Sistematica**

intervalo = np.random.randint(1, 50) # Gera intervalo com base na quantidade de registros arrendondando para baixo
amostra_sistematica = df1.iloc[::intervalo, :]
amostra_sistematica.head()

###############################################################################################################################################################################################################
#%%
## **Amostragem Estratificada**

from sklearn.model_selection import train_test_split

amostra_estratificada, _ = train_test_split(df1, test_size=0.5, stratify=df1["Regiao"])
amostra_estratificada.head()
#Vou usar amostra estratificada de acordo com o exato parâmetro você deseja
###############################################################################################################################################################################################################

#%%
## **Amostragem por Conglomerados**

# regra de clusterizacao pega todos daquele parâmetro e usa exatamente todos os dados do parâmetro selecionado

clusters = df1.groupby('Regiao')
amostra_conglomerados = clusters.get_group('Sul')
amostra_conglomerados.head()
###############################################################################################################################################################################################################

#%%
## **Amostragem Por Conveniência**
"""Amostragem em ordem"""

amostra_conveniencia = df1.head(1000) #Pega apenas as primeiras linhas
amostra_conveniencia.head()
###############################################################################################################################################################################################################

#%%
## **Amostragem por Julgamento**

amostra_julgamento = df1[(df1['Idade'] > 30) &
                        (df1['Idade'] <=55) &
                        (df1['Renda'] > 1500) |
                        (df1['Regiao'] != 'Oeste')].sample(n=1000, random_state=42) #Amostra de mil linhas # a | aqui serve como complementro/segunda parte, a gente vai começar apartir do ponto do oeste

amostra_julgamento.head()

###############################################################################################################################################################################################################
#%% Amostra por cotas
"""Amostra por cotas"""
amostra_cotas = df1.groupby("Regiao").apply(lambda x: x.sample(n =25)).reset_index(drop=True)
amostra_cotas.head()
# troque isso por verdadeiro e quando.a linha quando tiver a Região leste da primeira amostra aparto do n=25 e pegará todas as linhas que tem a Região Leste
# Caso drop=False ele pegará todas as amostras que não contém  a Região "Leste"


###############################################################################################################################################################################################################
## **Exercícios**

"""Comece executando a criação do conjunto de dados na célula abaixo e depois façam os exercícios abaixo:

1. Realizar uma amostragem aleatória simples com 500 registros.

2. Criar uma amostragem sistemática escolhendo cada 10º registro.

3. Dividir a base em estratos por localização e selecionar amostras proporcionais.

4. Selecionar aleatoriamente transações fraudulentas e comparar com transações não fraudulentas.

5. Criar um subconjunto de dados com base em amostragem por julgamento para transações acima de R$5000.

6. Aplicar amostragem por conglomerados dividindo os dados por tipo de transação e sorteando um grupo.

7. Executar uma amostragem por conveniência pegando os 300 primeiros registros.

8. Criar uma amostragem por cotas considerando o tipo de transação e localização.

9. Comparar os resultados das amostras aleatória e estratificada e explicar as diferenças.
"""
