# Você trabalha em uma empresa de varejo e precisa analisar os dados de
# vendas do último ano para identificar padrões e insights para melhorar o desempenho. Os dados
# estão armazenados em um banco de dados SQLite, e você utilizará a biblioteca Pandas para
# manipular e analisar esses dados, além de gerar visualizações utilizando Matplotlib e Seaborn.

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Conectar ao banco de dados SQLite
conexao = sqlite3.connect("dados_vendas.db")

# Criar um cursor 
cursor = conexao.cursor()

# Criar a tabela caso ela ainda nao exista
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')

# Verificar se a tabela esta vazia
cursor.execute("SELECT COUNT(*) FROM vendas1")

quantidade_vendas = cursor.fetchone()[0]

# Se a tabela estiver vazia, inserir os dados
if quantidade_vendas == 0:

    cursor.execute('''
    INSERT INTO vendas1
    (data_venda, produto, categoria, valor_venda)
    VALUES
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00)
    ''')

    # Confirmar as mudancas
    conexao.commit()

    print("Dados inseridos com sucesso!")

else:

    print("Os dados ja existem no banco de dados.")

# Pegar os dados da tabela e colocar em um DataFrame
df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)

# Mostrar os dados
print("\nDados de vendas:")
print(df_vendas)

# Mostrar informacoes sobre os dados
print("\nInformacoes dos dados:")
df_vendas.info()

# Verificar se existem valores vazios
print("\nValores vazios:")
print(df_vendas.isnull().sum())

# Transformar a coluna de data em formato de data
df_vendas["data_venda"] = pd.to_datetime(df_vendas["data_venda"])

# Calcular o total de vendas
total_vendas = df_vendas["valor_venda"].sum()

# Calcular a media das vendas
media_vendas = df_vendas["valor_venda"].mean()

# Encontrar a maior venda
maior_venda = df_vendas["valor_venda"].max()

# Encontrar a menor venda
menor_venda = df_vendas["valor_venda"].min()

# Calcular o total de vendas por categoria
vendas_categoria = df_vendas.groupby("categoria")["valor_venda"].sum()

# Calcular a quantidade de vendas por categoria
quantidade_categoria = df_vendas.groupby("categoria")["id_venda"].count()

# Calcular o total de vendas por mes
df_vendas["mes"] = df_vendas["data_venda"].dt.month

vendas_mes = df_vendas.groupby("mes")["valor_venda"].sum()

#Exibe Relatorios
print("\n======================================")
print("RELATORIO FINAL DE VENDAS")
print("======================================")
print(f"Total de vendas: R$ {total_vendas:.2f}")
print(f"Media das vendas: R$ {media_vendas:.2f}")
print(f"Maior venda: R$ {maior_venda:.2f}")
print(f"Menor venda: R$ {menor_venda:.2f}")


print("\nTotal de vendas por categoria:")
print(vendas_categoria)


print("\nQuantidade de vendas por categoria:")
print(quantidade_categoria)


print("\nTotal de vendas por mes:")
print(vendas_mes)


# Configuracao do Seaborn
sns.set_theme()

# Tabela total de vendas
plt.figure(figsize=(8, 5))

sns.barplot(
    x=vendas_categoria.index,
    y=vendas_categoria.values
)

plt.xlabel("Categoria")
plt.ylabel("Valor das Vendas")

plt.title("Total de Vendas por Categoria")

plt.show()

#Tabela de quantidade de vendas
plt.figure(figsize=(8, 5))

sns.barplot(
    x=quantidade_categoria.index,
    y=quantidade_categoria.values
)

plt.xlabel("Categoria")
plt.ylabel("Quantidade de Vendas")

plt.title("Quantidade de Vendas por Categoria")

plt.show()

#Tabela vendas ao ano
plt.figure(figsize=(10, 5))

sns.lineplot(
    x=vendas_mes.index,
    y=vendas_mes.values,
    marker="o"
)

plt.xlabel("Mes")
plt.ylabel("Valor das Vendas")

plt.title("Vendas ao Longo do Ano")

plt.show()

# Encontrar a categoria com maior valor de vendas
categoria_maior_venda = vendas_categoria.idxmax()

valor_categoria_maior = vendas_categoria.max()


# Encontrar o mes com maior valor de vendas
mes_maior_venda = vendas_mes.idxmax()

valor_mes_maior = vendas_mes.max()


print("\n======================================")
print("INSIGHTS DA ANALISE")
print("======================================")
print(f"A categoria com maior valor de vendas foi {categoria_maior_venda}, com R$ {valor_categoria_maior:.2f}.")
print(f"O mes com maior valor de vendas foi {mes_maior_venda}, com R$ {valor_mes_maior:.2f}.")
print("\nCom base nos dados analisados, a empresa pode dar maior atencao as categorias e aos periodos que apresentam maiores valores de vendas.")


conexao.close()

print("\nAnalise finalizada com sucesso!")
