import numpy  as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express  as px 

#Geração de gráficos:
base_credit = pd.read_csv(r'C:\Users\jvict\OneDrive\Documentos\Machine Learning e Data Science com Python de A à Z\Bases de dados\credit_data.csv')
sns.countplot(x = base_credit['default'])
plt.show()
plt.hist(x  = base_credit['age'])
plt.show()
plt.hist(x = base_credit['income'])
plt.show()
plt.hist(x = base_credit['loan'])
plt.show()

grafico = px.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'], color= 'default')
grafico.show()
