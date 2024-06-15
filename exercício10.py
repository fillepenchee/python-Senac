# 10. Criar um programa que calcule o IMC de um usuário.


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print(f"O seu IMC é {imc}.")