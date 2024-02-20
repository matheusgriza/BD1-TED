import os
import mysql.connector
conexao = mysql.connector.connect(
    
)

class Aluno:
    def __init__(self, nome, cpf, email, fone):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.fone = fone


#Escopo Global
requisicao = conexao.cursor()

#Functions

def criarAluno():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("Email: ")
    fone = input("Telefone: ")

    aluno = Aluno(nome,cpf,email,fone)
    return aluno


def inserirAluno():
    aluno = criarAluno()
    sql = "insert into tb_aluno(nome, cpf, e_mail, telefone) values (%s, %s, %s, %s)"
    valores = (aluno.nome, aluno.cpf, aluno.email, aluno.fone)
    requisicao.execute(sql,valores)
    #Confirmando Requisição
    conexao.commit()
    #Obtendo a chave inserida
    return print("Novo registro inserido. ID:", requisicao.lastrowid)


def listarAluno():
    sql = f"select * from tb_aluno"
    requisicao.execute(sql)
    resultado = requisicao.fetchall()
    for aluno in resultado:
        print('-----------------------')
        print(f"ID: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"CPF: {aluno[2]}")
        print(f"E-mail: {aluno[3]}")
        print(f"Telefone: {aluno[4]}")

def deletar():
    aluno = input("Digite o ID: ")
    sql = f"delete from tb_aluno where aluno_id = {aluno}"
    requisicao.execute(sql)
    conexao.commit()
    print("Aluno deletado com sucesso!")

def listaAtributos():
    print('1 - Nome')
    print('2 - CPF ')
    print('3 - E-mail ')
    print('4 - Telefone')
    print('5 - Tudo')

def selecionarAtributo():
    lista = ['nome', 'cpf','E_mail', 'telefone', '*']
    listaAtributos()
    atributo = int(input("Selecione um atributo para alterar: "))
    return lista[atributo-1]

def apresentaAluno(id):
    sql = f"select * from tb_aluno where aluno_id = {id}"
    requisicao.execute(sql)
    resultado = requisicao.fetchall()
    for aluno in resultado:
        print('-----------------------')
        print(f"ID: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"CPF: {aluno[2]}")
        print(f"E-mail: {aluno[3]}")
        print(f"Telefone: {aluno[4]}")


def alterarAluno():
    id = input("Digite o ID do aluno que deseja: ")
    apresentaAluno(id)
    atributo = selecionarAtributo()
    if (atributo == '*'):
        dadosAtualizados = criarAluno()
        sql = f"update tb_aluno set nome = '{dadosAtualizados.nome}', cpf = '{dadosAtualizados.cpf}', E_mail = '{dadosAtualizados.email}', telefone = '{dadosAtualizados.fone}' where aluno_id = {id}"
    else:
        novoValor=input(f"Digite o novo {atributo}: ")
        sql = f"update tb_aluno set {atributo} = '{novoValor}' where aluno_id = {id}"
    
    
    requisicao.execute(sql)
    conexao.commit()
    print('**** DADOS ALTERADOS COM SUCESSO ****')
    apresentaAluno(id)

def menu():
    print('1 - Incluir')
    print('2 - Alterar')
    print('3 - Deletar')
    print('4 - Listar todos alunos')
    print('5 - Sair')

opc = 0
while (opc != 5):
    menu()
    opc = int(input('Selecione um das opcoes acima: '))
    match opc:
        case 1:
            os.system('cls')
            print('INSERIR ALUNO')
            inserirAluno()
        case 2:
            os.system('cls')
            print('ALTERAR ALUNO')
            listarAluno()
            print('-----------------')
            alterarAluno()
            print()
        case 3:
            os.system('cls')
            print('DELETAR ALUNO')
            listarAluno()
            print('-----------------')
            deletar()
            os.system('cls')
            listarAluno()

        case 4:
            os.system('cls')
            print('LISTAR TODOS ALUNOS')
            listarAluno()
            input()

