"""03. Criar um programa que leia números que o usuário digitar. O programa irá parar assim que o usuário digitar um número negativo
e imprimirá a soma dos números"""

soma = 0
num = 1

while num != 0:
    num = int(input(f"Digite um número: \n"))
    if num != 0:
        soma += num
    else:
        break

print(f"A soma dos números positivos é {soma}. \n"
"Aqui não gostamos de números negativos!")
