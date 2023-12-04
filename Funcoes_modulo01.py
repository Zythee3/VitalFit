import pandas as pd
from Classes import *
import csv
def cadastramento_cliente():
    print("\n------------ CADASTRAMENTO DE CLIENTES ------------")
    try:
        nome = input("nome do cliente: ")
        idade = int(input("Idade: "))
        historico_medica = input("Histórico médico: ")
        peso = float(input("Peso: "))
        altura = float(input("Altura: "))
        condicao = input("condição do cliente: ")
        metas = input("metas do cliente: ")
    except ValueError:
        print("Dado inválido. Tente novamente.")
        cadastramento_cliente()
    
    novo_cliente = clientes(nome, idade)
    novo_perfil_cliente = perfil_cliente(nome, idade, historico_medica, peso, altura, condicao, metas, "0")
    lista_clientes_cadastrados = []
    lista_perfil_clientes_cadastrados = []
    
    lista_clientes_cadastrados.append(novo_cliente)
    lista_perfil_clientes_cadastrados.append(novo_perfil_cliente)

    df = pd.DataFrame({
        'Nome': [nome],
        'Idade': [idade],
        'Historico Medico': [historico_medica],
        'Peso': [peso],
        'Altura': [altura],
        'Condicao': [condicao],
        'Metas': [metas],
        'Desempenho': ['0']
    })
#escreve no arquivo csv as informações do cliente
    df.to_csv('clientes_cadastrados.csv', index=False, sep=';')
    df.to_csv(f'{nome}.csv', index=False, sep=';')
    print("Cliente cadastrado com sucesso!")
    lista_clientes_cadastrados.clear()
    lista_perfil_clientes_cadastrados.clear()

def menu_cliente():
    print("\n------------ MENU CLIENTE ------------")
    print("1 - Cadastrar novo cliente")
    print("2 - Acessar pefil de cliente")

    escolha_menu = int(input("Escolha uma opção: "))
    match escolha_menu:
        case 1:
            cadastramento_cliente()
        case 2:
            escolha_nome_cliente = input("Digite o nome do cliente: ")
            sub_menu_cliente(escolha_nome_cliente)

def sub_menu_cliente(nome_cliente):
    print("\n------------ MENU CLIENTE ------------")
    print("1 - visualizar perfil de cliente")
    print("2 - Criar avaliação física do cliente")
    print("3 - Criar treino")
    print("4 - Acessar treino")
    print("5 - visualizar dieta do cliente")
    print("6 - Registrar falta")
    print("7 - Voltar ao menu principal\n")

    escolha_sub_menu = int(input("Escolha uma opção: \n"))
    match escolha_sub_menu:
        case 1:
            imprimi_perfil_cliente(nome_cliente)
            sub_menu_cliente(nome_cliente)
        case 2:
            cria_avaliacao(nome_cliente)
            sub_menu_cliente(nome_cliente)
        case 3:
            cria_treino(nome_cliente)
            sub_menu_cliente(nome_cliente)
        case 4:
            imprimi_treino(nome_cliente)
            sub_menu_cliente(nome_cliente)
        case 5:
            print("Dieta do cliente")
        case 6:
            menu_cliente()

        

def cria_avaliacao(nome_cliente):
    desempenho_cliente = input("Desempenho do cliente: ")
    novo_peso = float(input("Peso: "))
    
    with open(f"{nome_cliente}.csv", newline = '') as arquivo:
        leitor = csv.DictReader(arquivo, delimiter = ';')
        linhas = []
        for linha in leitor:
            linha['Desempenho'] = desempenho_cliente
            linha['Peso'] = novo_peso
            linhas.append(linha)

    with open(f"{nome_cliente}.csv", "w", newline = '') as arquivo:
        escritor = csv.DictWriter(arquivo, delimiter= ';', fieldnames= leitor.fieldnames)
        escritor.writeheader()
        escritor.writerows(linhas)

def imprimi_perfil_cliente(nome_cliente):
    print("\n------------ PERFIL DE CLIENTE ------------")
    with open(f"{nome_cliente}.csv", "r") as arquivo:
        leitor_dados = csv.DictReader(arquivo, delimiter=";")
        for dados in leitor_dados: 
            print(f"Nome: {dados['Nome']}\nIdade: {dados['Idade']}\nHistorico Medico: {dados['Historico Medico']}\nPeso: {dados['Peso']}\nAltura: {dados['Altura']}\nCondição: {dados['Condicao']}\nMetas: {dados['Metas']}\nDesempenho: {dados['Desempenho']}\n")
def cria_treino(nome_cliente):
    print("\n------------ CRIAÇÃO DE AVALIAÇÃO FÍSICA ------------")
    exercicio = input("Exercicio: ")
    data = input("Data: ")
    carga = input("Carga: ")
    repeticoes = input("Repetições: ")
    series = input("Series: ")
    novo_treino = treino(exercicio, data, carga, repeticoes, series)
    lista_treinos_cadastrados = []
    lista_treinos_cadastrados.append(novo_treino)

    treinos = pd.DataFrame({
        'Exercicio': [exercicio],
        'Data': [data],
        'Carga': [carga],
        'Repeticoes': [repeticoes],
        'Series': [series]
    })
    treinos.to_csv(f'{nome_cliente}_treinos.csv', index=False, sep=';')

def imprimi_treino(nome_cliente):
    print("\n------------ TREINO ------------")
    with open(f"{nome_cliente}_treinos.csv", "r") as arquivo:
        leitor_dados = csv.DictReader(arquivo, delimiter=";")
        for dados in leitor_dados: 
            print(f"Exercicio: {dados['Exercicio']}\nData: {dados['Data']}\nCarga: {dados['Carga']}\nRepetições: {dados['Repeticoes']}\nSeries: {dados['Series']}\n")
menu_cliente()

