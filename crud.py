import sqlite3

def inserir_aluno():
    banco = sqlite3.connect("banco_alunos.db")

    criar_tabela = '''
        CREATE TABLE IF NOT EXISTS aluno (
            matricula INTEGER PRIMARY KEY,
            nome TEXT,
            CPF TEXT,
            telefone TEXT
        );
    '''
    banco.execute(criar_tabela)

    matricula = int(input("Digite a matricula: "))
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    telefone = input("Digite o telefone: ")

    inserir_dados = f'''
        INSERT INTO aluno (matricula, nome, CPF, telefone) VALUES
        ({matricula}, "{nome}", "{cpf}", "{telefone}");
    '''
    banco.execute(inserir_dados)
    banco.commit()
    print("DADOS INSERIDOS!")

def acessar_conta():
    banco = sqlite3.connect("banco_alunos.db")

    meucursor = banco.cursor()
    pesquisa = "SELECT matricula, nome, CPF, telefone FROM aluno;"
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()

    for linha in resultado:
        print("=====================")
        print("Matricula", linha[0])
        print("Nome:", linha[1])
        print("CPF", linha[2])
        print("Telefone:", linha[3])
        print("=====================")

def sair_banco():
    banco = sqlite3.connect("banco_alunos.db")
    banco.close()

inserir_aluno()
acessar_conta()
