"""03. Criar um programa que leia números que o usuário digitar. O programa irá parar assim que o usuário digitar um número negativo
e imprimirá a soma dos números"""

soma = 0
num = 0
listaNum = []

while num >= 0:
    num = int(input(f"Digite um número: \n"))
    listaNum.append(num)
    if num >= 0:
        soma += num

print(f"A soma dos números positivos digitados é {soma}. \n"
"Aqui não gostamos de números negativos! \n"
"Eis a lista de todos os números digitados: \n")
for num in enumerate(listaNum, start = 1):
    print(num)
