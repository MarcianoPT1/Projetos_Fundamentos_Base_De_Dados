#Nome: Márcio Canuto
#Data: 21/11/2024

from tkinter import * #Importa a biblioteca para criar uma interface
import sqlite3 # Importa a biblioteca para puder fazer a base de dados

janela = Tk() #criação da janela que vai usado como interface

# Conexão e criação da base de dados
conn = sqlite3.connect('ImcDosAlunos.db')
cursor = conn.cursor() #criar um cursor para a base de dades

# Criação da tabela de utilizadores, ou seja, "users"
cursor.execute('''Create TABLE IF NOT EXISTS users (
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                altura REAL NOT NULL,
                peso REAL NOT NULL)
                ''')
conn.commit()

def Entrar():
    while True:
        print("\n ---Menu---")
        print("1. Registrar um usuario.")
        print("2. Consultar dados de um usario.")
        print("3. Sair")

        escolha = input("Oque deseja fazer: ")
        if escolha == "1":
            Registrar_Usuario()
        elif escolha == "2":
            CalcularIMC()
        elif escolha == "3":
            break
        else:
            print("Opção invalida! tente novamente")



#Criação de um afunção que registrar o usario
def Registrar_Usuario():
    nome = input("Insere o nome do Usuario: ") #
    idade = int(input("Insere a idade do Usuario: "))
    altura = float(input("Insere a altura do Usuario: "))
    peso = float(input("Insere a peso do Usario: "))

    #Comando para
    cursor.execute(
        'INSERT INTO users (nome, idade, altura, peso) VALUES (?, ?, ?, ?)',
                                      (nome, idade, altura, peso))
    conn.commit() #comando para guardar o registro do user
    print(f"O utilizador '{nome}' foi inserido com sucesso.")

# Criação de uma função para calcular o IMC
def CalcularIMC():
    # Listar os usuários cadastrados
    print("\n--- Usuários Registrados ---")
    cursor.execute('SELECT nome FROM users')  # Obtém apenas os nomes dos usuários
    users = cursor.fetchall()

    if not users:
        print("Nenhum usuário encontrado!")
        return

    for user in users:
        print(f"- {user[0]}")

    # Solicitar o nome do usuário para cálculo do IMC
    nome = input("\nDigite o nome do usuário para calcular o IMC: ")

    # Buscar o usuário no banco de dados
    cursor.execute('SELECT altura, peso FROM users WHERE nome = ?', (nome,))
    dados = cursor.fetchone()

    if dados:
        altura, peso = dados
        imc = peso / (altura ** 2)  # Fórmula do IMC
        print(f"\nO IMC de {nome} é: {imc:.2f}")

# Executar o menu de entrada
Entrar()

#Fechar a conexão
conn.close()