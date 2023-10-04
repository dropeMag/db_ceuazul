import random

# Função para gerar dados fictícios para as tabelas
def gerar_dados_classificacao(num_inserts):
    dados = []
    for i in range(1, num_inserts + 1):
        descricao = f'Descrição {i}'
        dados.append((descricao,))
    return dados

def gerar_dados_entrada_saida(num_inserts):
    dados = []
    for i in range(1, num_inserts + 1):
        classificacao_id = random.randint(1, 10)  # IDs de classificação de 1 a 10
        descricao = f'Descrição {i}'
        valor = round(random.uniform(1, 1000), 2)
        data = '2023-10-03 12:00:00'  # Data fictícia
        anexo = f'Anexo_{i}.pdf'
        observacao = f'Observação {i}'
        dados.append((classificacao_id, descricao, valor, data, anexo, observacao))
    return dados

# Gerar inserts para a tabela Classificacao
inserts_classificacao = []
dados_classificacao = gerar_dados_classificacao(10)
for dado in dados_classificacao:
    insert = f"INSERT INTO [scFinanceiro].[Classificacao] (descricao) VALUES ('{dado[0]}');"
    inserts_classificacao.append(insert)

# Gerar inserts para a tabela Entrada
inserts_entrada = []
dados_entrada = gerar_dados_entrada_saida(800)
for dado in dados_entrada:
    insert = f"INSERT INTO [scFinanceiro].[Entrada] (classificacao_id, descricao, valor, data, anexo, observacao) VALUES ({dado[0]}, '{dado[1]}', {dado[2]}, '{dado[3]}', '{dado[4]}', '{dado[5]}');"
    inserts_entrada.append(insert)

# Gerar inserts para a tabela Saida
inserts_saida = []
dados_saida = gerar_dados_entrada_saida(800)
for dado in dados_saida:
    insert = f"INSERT INTO [scFinanceiro].[Saida] (classificacao_id, descricao, valor, data, anexo, observacao) VALUES ({dado[0]}, '{dado[1]}', {dado[2]}, '{dado[3]}', '{dado[4]}', '{dado[5]}');"
    inserts_saida.append(insert)

# Imprimir os comandos INSERT INTO no terminal
print("-- Inserts para a tabela Classificacao --")
for insert in inserts_classificacao:
    print(insert)

print("\n-- Inserts para a tabela Entrada --")
for insert in inserts_entrada:
    print(insert)

print("\n-- Inserts para a tabela Saida --")
for insert in inserts_saida:
    print(insert)
