# Passo 1: Importar a base de dados
import pandas as pd
import plotly.express as px

tabela = pd.read_csv('csv_tables/telecom_users.csv')

# Passo 2: Visualizar a base de dados
tabela = tabela.drop('Unnamed: 0', axis=1)
tabela = tabela.drop('IDCliente', axis=1)
print(tabela)

# - Entender quais as informações tão disponíveis, print(tabela.info())
# - Descobrir aos erros da base de dados

# Passo 3: Tratamento de dados
# - Valores que estão reconhecidos de forma errada
#correção total gasto
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

# - Valores vazios
# # axis = 0 _> linha ou axis = 1 _> coluna
# deletando as colunas vazias
tabela = tabela.dropna(how='all', axis=1)

# deletando as linhas vazias
tabela = tabela.dropna() #-> default any e 0

# Passo 4: Análise Inicial
# Como estão os nossos cancelamentos?
print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

# Passo 5: Análise Mais completa
# comparar cada coluna da minha tabela com a coluna de cancelamento

for coluna in tabela.columns:
    # etapa 1: criar o gráfico
    grafico = px.histogram(tabela, x=coluna, color='Churn', text_auto=True)
    # para edições nos gráficos: https://plotly.com/python/histograms/
    # para mudar a cor do gráfico , color_discrete_sequence=["blue", "green"]
    # etapa 2: exibir o gráfico
    grafico.show()
    
#conclusões

#- Clientes com contrato mensal tem MUITO mais chance de cancelar:
#    - Podemos fazer promoções para o cliente ir para o contrato anual
    
#- Familias maiores tendem a cancelar menos do que famílias menores
#    - Podemos fazer promoções pra pessoa pegar uma linha adicional de telefone
    
#- MesesComoCliente baixos tem MUITO cancelamento. Clientes com pouco tempo como cliente tendem a cancelar muito
#    - A primeira experiência do cliente na operadora pode ser ruim
#    - Talvez a captação de clientes tá trazendo clientes desqualificados
#    - Ideia: a gente pode criar incentivo pro cara ficar mais tempo como cliente
    
#- QUanto mais serviços o cara tem, menos chance dele cancelar
#    - podemos fazer promoções com mais serviços pro cliente
    
#- Tem alguma coisa no nosso serviço de Fibra que tá fazendo os clientes cancelarem
#    - Agir sobre a fibra
    
#- Clientes no boleto tem MUITO mais chance de cancelar, então temos que fazer alguma ação para eles irem para as outras formas de pagamento