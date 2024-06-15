
# 08. Criar um programa que leia a quantidade de números a serem digitados. Em seguida o programa deverá ler todos os números e no final imprimir: a soma e a média aritmética.

quantNums = int(input("Diga quantos números você quer digitar: \n"))
count = 1
soma = 0

while count <= quantNums:
    nums = int(input("Digite um número: \n"))
    count += 1
    soma = soma + nums

media = soma + quantNums

print(f"Você digitou {quantNums} números. \n"
f"A soma deles é {soma} e a média aritmética é {media}.")
