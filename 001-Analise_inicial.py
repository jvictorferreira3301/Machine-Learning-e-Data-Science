import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Criação da Variável com o dataset lido atraves da função read_csv do  pandas com o path onde o dataset está contida.
base_credit = pd.read_csv(
    r"C:\Users\jvict\OneDrive\Documentos\Machine Learning e Data Science com Python de A à Z\Bases de dados\credit_data.csv"
)  # dataset com os atributos: clientid, income, age, loan e default.
# Análise inicial:
print(base_credit.head(10))  # Visualizar os primeiros (n) registros.
print(base_credit.tail(10))  # Visualizar os últimos (n) registros.
print(
    base_credit.describe()
)  # Conta a quantidade de itens em cada atributo e outros aspectos como média, desvio etc.

# Exploração do dataset com filtros:
print(
    base_credit[base_credit["income"] >= 69995.685578]
)  # Busca o cliente com maior income (Renda). Valor obtido na análise inicial.
print(
    base_credit[base_credit["loan"] >= 1.377630]
)  # Busca o cliente com  menor loan (Dívida). Valor obtido na análise inicial.

print(
    np.unique(base_credit["default"], return_counts=True)
)  # Valores de cada coluna/atributo.
