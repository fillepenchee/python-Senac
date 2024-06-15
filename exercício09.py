# 09. Criar um programa que leia 10 números e no final pergunte ao usuário se ele deseja listar: todos os números, somente os pares ou somente os ímpares.

count = 1
listNums = []

while count <= 10:
    nums = int(input(f"Digite o número {count} de 10: \n"))
    count += 1
    listNums.append(nums)



print(f"Você digitou números. \n")


