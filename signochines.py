
#signo chinês
# lista dos animais do zodíaco chinês
# fórmula corrigida para determinar signo com base no ano de nascimento
# return o resultado
# exibir o resultado
# 

dataNasc = str(input(f"Digite sua data de nascimento, separada por barras: "))

listaNasc = dataNasc.split('/')

diaNasc = int(listaNasc[0])
mesNasc = int(listaNasc[1])
anoNasc = int(listaNasc[2])

def determinarSigno(anoNasc):
    animais = ["Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Carneiro", "Macaco", "Galo", "Cão", "Javali"]

    indiceAnimal = (anoNasc - 1900) % 12 # indiceAnimal é baseado nas datas do signo do Rato listado na Wikipedia. O índice da lista permite "ir e voltar" no tempo

    return animais[indiceAnimal]

print(f"Seu signo do horóscopo chinês é: {determinarSigno(anoNasc)}")
