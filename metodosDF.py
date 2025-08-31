# %%

"""Data Frame com amostras Exemplo"""
import pandas as pd
import numpy as np

np.random.seed(42)
n = 500  # Quantidade de registros

df = pd.DataFrame({
    'ID_Transacao': range(1, n+1),
    'Valor': np.random.uniform(10, 10000, n),
    'Tipo_Transacao': np.random.choice(['Compra', 'Transferencia', 'Pagamento'], n),
    'Localizacao': np.random.choice(['SP', 'RJ', 'MG', 'RS', 'BA', 'PR'], n),
    'Horario': np.random.choice(['Manha', 'Tarde', 'Noite', 'Madrugada'], n),
    'Fraude': np.random.choice([0, 1], n, p=[0.7, 0.3]),
    'Extra' : np.random.choice(['sim', "não"], n) 
})


"""Métodos"""
df.head()       # Usado para ver as 5 primeiras linhas

# %%
df.head(10)     #Ver os 10 primeiros paramêtros

# %%
df.iloc[10:21]  # Mostra as linhas entre 10 e 21

# %%
df.tail(10)     # Mostra as 10 últimas linhas

# %%
df.sample(8)    # Mostra 5 linhas aleatórias
