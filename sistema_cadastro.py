""" 
Atualizações:

1 - Verificar se existe aluno cadastrado antes de editar para evitar erro (utilizar try catch).
2 - Verificar se existem notas cadastradas antes de editar para evitar erro (utilizar try catch).
3 - Em vez de editar Nome, Telefone e Endereço dos alunos de uma única vez, apresentar um menu para o usuário escolher a informação que deseja editar.
4 - Em vez de editar Nota 1, Nota 2 e Trabalho de uma única vez, apresentar um menu para o usuário escolher a informação que deseja editar.
5 - Limpar a tela toda vez que uma operação for realizada.
"""
import json

# função para cadastrar novo aluno

def cadastrarAluno():
    nome = input("Nome do aluno: ")
    cpf = input("CPF do aluno: ")
    telefone = input("Telefone do aluno: ")
    endereco = input("Endereço do aluno: ")

# gera matrícula de forma automática
    matricula = str(abs(hash(cpf)))[:5]

# dicionário escrito em Python (pares de chaves, ordenados)
    aluno = {
        "Nome" : nome,
        "CPF" : cpf,
        "Telefone" : telefone,
        "Endereço" : endereco,
        "Notas": {}
    }

# abre o arquivo pra ser editado em "json" e o "a" é de anexo. depois write escreve o arquivo
    with open("alunos.json", "a") as file:
        file.write(json.dumps({matricula : aluno}) + "\n")
    print(f"Aluno cadastrado com matrícula: {matricula}.")


# função para listar todos os alunos cadastrados
def listarAlunos():

# abre o arquivo pra ser editado em "json" e o "r" é de ler ou mudar coisas dentro do arquivo aberto
#for dentro do for é pra percorrer linha por linha até carregar (load), e ao carregar a linha, percorre item por item
#o for de dentro é pra percorrer matrizes (um vetor de vetores)
    with open("alunos.json", "r") as file:
        for linha in file:
            dado = json.loads(linha)
            for matricula, aluno in dado.items():
                if "Nome" in aluno:
                    print(f"Matricula: {matricula}. Nome: {aluno['Nome']}.")

# função para editar um aluno cadastrado
def editarAluno():
    matricula = input("Digite a matrícula do aluno a ser editado: ")

    with open("alunos.json", "r") as file:
        linhas = file.readlines()

    for i, linha in enumerate(linhas):
        dado = json.loads(linha)
        if matricula in dado:
            novo_nome = input("Novo nome: ")
            novo_telefone = input("Novo telefone: ")
            novo_endereco = input("Novo endereço: ")

            # Atualiza as informações do aluno
            dado[matricula]["Nome"] = novo_nome
            dado[matricula]["Telefone"] = novo_telefone
            dado[matricula]["Endereco"] = novo_endereco

            linhas[i] = json.dumps(dado) + "\n"
            with open("alunos.json", "w") as file:
                file.writelines(linhas)

            print("Informações do aluno atualizadas.")
            return

    print("Matrícula não encontrada.")

# função para lançar as notas de um aluno
def lancarNotas():
    matricula = input("Digite a matrícula do aluno a ser editado: ")
    
    with open("alunos.json", "r") as file:
        linhas = file.readlines()

    for i, linha in enumerate(linhas):
        dado = json.loads(linha)
        if matricula in dado:
            prova1 = input("Nota da prova 1: ")
            prova2 = input("Nota da prova 2: ")
            trabalho = input("Nota do trabalho: ")

            dado[matricula]["Notas"] = {
                "Prova 1": prova1,
                "Prova 2": prova2,
                "Trabalho": trabalho
            }

            linhas[i] = json.dumps(dado) + "\n"
            with open("alunos.json", "w") as file:
                file.writelines(linhas)

            print("Notas do aluno atualizadas.")
            return

    print("Matrícula não encontrada.")

# Função para exibir as notas de um aluno
def exibirNotas():
    matricula = input("Digite a matrícula do aluno a ser editado: ")

    with open("alunos.json", "r") as file:
        for linha in file:
            dado = json.loads(linha)
            if matricula in dado:
                if "Notas" in dado[matricula]:
                    notas = dado[matricula]["Notas"]
                    print(f"Notas do aluno {dado[matricula]['Nome']} : {notas}")
                    return

    print("Matrícula não encontrada.")

# função para exibir notas de um aluno
def exibirNota():
    matricula = input("Digite a matrícula do aluno cujas notas serão exibidas: ")

    with open("alunos.json", "r") as file:
        for linha in file:
            dado = json.loads(linha)
            if matricula in dado:
                print(f"Notas do aluno: (Matrícula: {matricula}) : {dado[matricula]}")
                return
    print("Matrícula não encontrada.")

# função para editar notas de um aluno
def editarNota():
    matricula = input("Digite a matrícula do aluno a ser editado: ")

    with open("alunos.json", "r") as file:
        linhas = file.readlines()
    
    for i, linha in enumerate(linhas):
        dado = json.loads(linha)
        if matricula in dado:
            if "Notas" in dado[matricula]:
                notas = dado[matricula]["Notas"]
                print(f"Notas atuais do aluno: {dado[matricula]['Nome']} : {notas}")
            novaProva1 = input("Digite a nova nota da Prova 1: ")
            novaProva2 = input("Digite a nova nota da Prova 2: ")
            novaTrabalho = input("Digite a nova nota do Trabalho: ")

            #atualiza as informações do aluno
            dado[matricula]["Notas"]["Prova 1"] = novaProva1
            dado[matricula]["Notas"]["Prova 2"] = novaProva2
            dado[matricula]["Notas"]["Trabalho"] = novaTrabalho

            linhas[i] = json.dumps(dado) + "\n"
            with open("alunos.json", "w") as file:
                file.writelines(linhas)
            
            print("Notas do aluno atualizadas.")
            return

    print("Matrícula não encontrada. ")

# Menu principal
while True:
    print("1- Cadastrar aluno")
    print("2- Listar alunos")
    print("3- Editar aluno")
    print("4- Lançar notas")
    print("5- Exibir notas")
    print("6- Editar nota")
    print("0- SAIR")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cadastrarAluno()
    elif escolha == "2":
        listarAlunos()
    elif escolha == "3":
        editarAluno()
    elif escolha == "4":
        lancarNotas()
    elif escolha == "5":
        exibirNotas()
    elif escolha == "6":
        editarNota()
    elif escolha == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")
