enunciado01 = "Como fazer comentário de várias linhas em Python?"
opcoes01 = 'a) Colocar duas cerquilhas (##) antes e duas cerquilhas depois (##) \n b) Colocar três exclamações (!!!) antes e três exclamações depois (!!!) \n c) Colocar dois sinais de menor e dois hífens antes (<<--) e dois hífens e dois sinais de maior depois (-->>)\n d) Colocar três aspas duplas (""") antes e três aspas duplas depois (""") \n'
enunciado02 = "O que faz o método pop() em Python?"
opcoes02 = "a) Printa um texto na tela\n b) Apaga (esvazia) uma lista\n c) Remove um elemento de uma lista\n d) Enumera os elementos de uma lista\n"

print("Bem-vindo ao programa de perguntas sobre Python!")

print(f"Questão 1: \n {enunciado01} \n {opcoes01}")
resposta01 = str(input("Digite a letra correspondente a sua resposta: \n"))

print(f"Questão 2: \n {enunciado02} \n {opcoes02}")
resposta02 = str(input("Digite aqui sua resposta: \n"))

nota = 0

if resposta01 == "d" or "D":
    nota = nota + 5
if resposta02 == "c" or "C":
    nota = nota + 5

print(f"Fim do questionário. Sua nota é {nota} de 10.")
