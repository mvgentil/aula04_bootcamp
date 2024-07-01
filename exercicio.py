import csv

# caminho do arquivo
caminho_arquivo = 'exemplo.csv'

# inicia uma lista vazia para armazenar os dados
dados = []

# usa o gerenciador de contexto 'with' para abrir o arquivo
with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    # cria um leito de csv
    leitor_csv = csv.DictReader(arquivo)

    # itera sobre as linhas do arquivo csv
    for linha in leitor_csv:
        # adicionacada linha (um dicionario) à lista de dados
        dados.append(linha)


# imprime cada linha do arquivo csv
for registro in dados:
    print(registro)