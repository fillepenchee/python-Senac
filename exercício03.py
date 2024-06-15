
soma = 0
numeros = []

contador = 1
while contador <= 5:
    num = float(input(f"Digite o número {contador}: \n")) # pede pro usuário digitar um número "num", que é numerado conforme a variável "contador"
    numeros.append(num) # coloca o "num" (variável) recém digitado pelo usuário no final da lista "numeros"
    soma += num # soma o valor da variável "num" ao total da variável "soma"
    contador += 1 # adiciona mais um ao "contador" (variável) pra continuar no loop (Até bater na condição <= 5)

print(f"\nNúmeros digitados:")
for contador, num in enumerate(numeros, start = 1): # o Loop for com parâmetros "contador" e "num" 
    # o Enumerate lista elementos da lista "numeros", a começar do 1o
    print(f"Número {contador}: {num}.")

print(f"\n A soma é: {soma}.")
