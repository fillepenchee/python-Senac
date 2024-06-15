
import math
import os

def ehNumero(numero):
    return numero.isnumeric()

def limpaTela():
    if os.name == 'posix': # sistemas unix/linux/macOS
        os.system('clear')
    elif os.name == 'nt': # sistema windows
        os.system('cls')

def menuFatorial():
    print("Digite...") 
    print("")
    print("1 para fatorial do primeiro número.")
    print("2 para fatorial do segundo número.")
    print("")

def menuPrincipal():
    print("Digite...")
    print("")
    print("1 para ADIÇÃO.")
    print("2 para SUBTRAÇÃO.")
    print("3 para MULTIPLICAÇÃO.")
    print("4 para DIVISÃO.")
    print("5 para DIVISÃO INTEIRA.")
    print("6 para MÓDULO.")
    print("7 para EXPONENCIAÇÃO.")
    print("8 para RAIZ.")
    print("9 para FATORIAL.")
    print("0 para SAIR DO PROGRAMA.")
    print("")

def menuRaiz():
    print("Digite...") 
    print("")
    print("1 para RAIZ QUADRADA.")
    print("2 para RAIZ CÚBICA.")
    print("")

def menuRaizQuad():
    print("Digite...") 
    print("")
    print("1 para RAIZ QUADRADA do primeiro número.")
    print("2 para RAIZ QUADRADA do segundo número.")
    print("")

def menuRaizCub():
    print("Digite...") 
    print("")
    print("1 para RAIZ CÚBICA do primeiro número..")
    print("2 para RAIZ CÚBICA do segundo número..")
    print("")

num1 = input("Digite o valor do primeiro número: ")
while not ehNumero(num1):
    num1 = input("O valor do primeiro número não é um número. Digite um número: ")
    limpaTela()

num2 = input("Digite o valor de segundo número: ")
while not ehNumero(num2):
    num2 = input("O valor do primeiro número não é um número. Digite um número: ")
    limpaTela()

num1 = int(num1)
num2 = int(num2)

menu = 1
menuPrincipal()
while not ehNumero(menu):
    limpaTela()
    print("O valor não é um número. ENTER pra continuar")
    limpaTela()
    menu = input("Digite um número de opção (1 a 9):")
    while menu < 0 or menu > 9:
        limpaTela()
        print("O valor não está entre 1 a 9.  ENTER pra continuar:")
        limpaTela()
        menu = input("Digite um número de 1 a 9:")

"""while not ehNumero(menu):
    menu = input("O valor digitado não é um número. Digite um número entre 0 e 9: ")
    limpaTela()
while menu != "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0":
    menu = input("Digite o número de uma opção válida (entre 0 e 9): ")"""

if menu == "1":
    limpaTela()
    print(num1 + num2) #adição
elif menu == "2":
    limpaTela()
    print(num1 - num2) #subtração
elif menu == "3":
    limpaTela()
    print(num1 * num2) #multiplicação
elif menu == "4":
    limpaTela()    
    if num2 == 0:
        print("Impossível dividir por zero.")
    else:
        print(num1 / num2) #divisão
elif menu == "5":
    limpaTela()
    if num2 == 0:
        print("Impossível dividir inteiro por zero.")
    else:
        print(num1 // num2) #divisão inteira
elif menu == "6":
    limpaTela()
    if num2 == 0:
        print("Impossível módulo por zero.")
    else:
        print(num1 % num2) #módulo
elif menu == "7":
    print(num1 ** num2) #exponenciação
elif menu == "8":
    limpaTela()
    menuRaiz()
    raiz = input("Resposta: ")
    num1 = float(num1)
    num2 = float(num2)
    if raiz == "1":
        menuRaizQuad()
        quad = input("Resposta: ")
        if quad == "1":
            print((math.sqrt(num1)))
        elif quad == "2":
            print((num2) ** (1/2))
        else:
            print("Erro: digitou opção inválida.") #erro
    if raiz == "2":
        menuRaizCub()
        cub = input("Resposta: ")
        if cub == "1":
            print((math.cbrt(num1)))
        elif cub == "2":
            print((num2) ** (1/3))
        else:
            print("Erro: digitou opção inválida.")   #erro
elif menu == "9":
    limpaTela()
    num1 = int(num1)
    num2 = int(num2)
    menuFatorial()
    fatorial = input("Resposta :")
    if fatorial == "1":
        print(math.factorial(num1))
    elif fatorial == "2":
        print(math.factorial(num2))
    else:
        print("Opção inválida.")
elif menu == "0":
    """limpaTela()
    print("Programa encerrado.") """ # resolver esse problema depois
else:
    print("Opção inválida.")


    """
        if num1 == 0:
            print("O fatorial do primeiro número é 1.")
        elif num2 == 0:
            print("O fatorial do segundo número é 1.")
        else:
            fat1 = 1
            while fat1 < (num1 - 1):
                numfat1 = fat1 * fat1 + 1
                fat1 = fat1 + 1
            fat2 = 1
            while fat2 < (num2 - 1):
                numfat2 = fat2 * fat2 + 1
                fat2 = fat2 + 1           
            print("Os fatoriais dos dois números são: " + numfat1 + "e" + numfat2)"""


