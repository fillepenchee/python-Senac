
num1 = int(input("Digite um número inteiro: \n"))

if num1 == 0:
    print("Este é um número neutro.")
elif num1 % 2 == 0:
    print("Este número é par")
else:
    print("Este número é ímpar")

print("O número é neutro." if num1 == 0 else "O número é par." if num1 % 2 == 0  else "O número é ímpar.") #
