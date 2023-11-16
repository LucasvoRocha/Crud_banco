from crud import inserir_aluno, acessar_conta, sair_banco

while True:
    print(" +=========================\n"
           "Bem vindo a Academy turma:\n"
           "==========================\n"
           "1- Criar conta\n"
           "2- Acessar contas existentes\n"
           "3- Sair\n")


    escolha = input("Opçoes: ")
    while escolha not in ["1", "2", "0"]:
        escolha = input("\nOpção invalida, tente novamente: ")

    if escolha == "1":

        print("+========================+\n"
                "| BEM VINDO AO CADASTRO! |\n"
                "+========================+\n"
                "|1- CADASTRO ALUNO       |\n"
                "|2- CADASTRO MODALIDADE  |\n"
                "|3- CADASTRO FUNCIONARIOS|\n"
                "|4- CADASTRO PERSONAL    |\n"
                "|0- VOLTAR               |\n"
                "+========================+\n")

        escolha = input("Opção: ")
        while escolha not in ["1", "2", "3", "4", "0"]:
            escolha = input("****INVALIDO****  : ")

        if escolha == "1":
            inserir_aluno()
            print("\n#######CONTA CRIADA COM SUCESSO!########")

        elif escolha == "2":
            print("\n######CONTA CRIADA COM SUCESSO!#########")

        elif escolha == "3":
            print("\n######CONTA CRIADA COM SUCESSO!#########")

        elif escolha == "4":
            print("\n######CONTA CRIADA COM SUCESSO!#########")

        elif escolha == "0":
            print("###############")
            break



    elif escolha == "2":
        acessar_conta()

    if escolha == "0":
        sair_banco()
        print("\nSaindo.....\n"
              "==========FINALIZADO==========")
        break

    else:
        print("\n#######INVALIDO###TENTE##NOVAMENTE######")
