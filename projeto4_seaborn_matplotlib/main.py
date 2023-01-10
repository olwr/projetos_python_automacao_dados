import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import numpy as np

#importar tabela
anuncios = pd.read_csv('advertising.csv')
print(anuncios)

#ajuste de dados (correção e limpeza de dados)
#print(anuncios.info())

#análise exploratória
#16 gráficos comparando cada correlação
#sns.pairplot(anuncios)
#plt.show()

#mesmos gráficos, porém em forma de heatmap
sns.heatmap(anuncios.corr(), annot=True, cmap='Wistia')
plt.show()

#modelagem + algoritmos
#separação de dados de treino e teste

# inputs do modelo (eixo x):
x = anuncios.drop('Vendas', axis=1)

# outputs do modelo (eixo y):
y = anuncios['Vendas']

#treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

#criação e treino ai
modelo_regressaolinear= LinearRegression()
modelo_regressaolinear.fit(x_treino, y_treino)

modelo_arvoredecisao = RandomForestRegressor()
modelo_arvoredecisao.fit(x_treino, y_treino)

#teste ai -> previsores e comparação
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

r2_lin = metrics.r2_score(y_teste, previsao_regressaolinear)
rsme_lin = np.sqrt(metrics.mean_squared_error(y_teste, previsao_regressaolinear))
print(f'R² da Regressão Linear: {r2_lin}')
print(f'RSME do Random Forest: {rsme_lin}')

r2_rf = metrics.r2_score(y_teste, previsao_arvoredecisao)
rsme_rf = np.sqrt(metrics.mean_squared_error(y_teste, previsao_arvoredecisao))
print(f'R² da Regressão Linear: {r2_rf}')
print(f'RSME do Random Forest: {rsme_rf}')

#visualização gráfica das previsões
previsao_teste = pd.DataFrame()
previsao_teste['y_teste'] = y_teste
previsao_teste['previsao_regressaolinear'] = previsao_regressaolinear
previsao_teste['previsao_arvoredecisao'] = previsao_arvoredecisao

plt.figure(figsize=(15,6))
sns.lineplot(data=previsao_teste)
plt.show()

# Como fazer uma nova previsao
# importar a nova_tabela com o pandas (a nova tabela tem que ter os dados de TV, Radio e Jornal)
# previsao = modelo_randomforest.predict(nova_tabela)
# print(previsao)

nova_tabela = pd.read_csv('novos.csv')
previsao = modelo_arvoredecisao.predict(nova_tabela)
print(previsao)