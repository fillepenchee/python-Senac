"""03. Criar um programa que leia números que o usuário digitar. O programa irá parar assim que o usuário digitar um número negativo
e imprimirá a soma dos números"""

# 05. Alterar o programa da questão 04 e perguntar ao usuário o que o programa fará com os números negativos: se deverá somar os negativos ou se deverá ignorar o sinal e somar o valor absoluto.

soma = 0
num = 0
listaNum = []

perguntaNegativo = str(input("Olá, usuário. O que devo fazer com os números negativos?\n"
"1. Somá-los com os positivos\n"
"2. Ignorar o sinal negativo e aí somá-los aos positivos\n"
"Digite o número da sua opção: "))

if perguntaNegativo == "1":
    while num >= 0:
        num = int(input(f"Digite um número: \n"))
        listaNum.append(num)
        if num >= 0:
            soma += num
        else:
            soma += num
            break
else:
    while num >= 0:
        num = int(input(f"Digite um número: \n"))
        listaNum.append(num)
        if num >= 0:
            soma += num
        else:
            soma += (num * -1)
            break

print(f"A soma dos números positivos digitados é {soma}. \n"
"Eis a lista de todos os números digitados: \n")
for num in enumerate(listaNum, start = 1):
    print(num)

