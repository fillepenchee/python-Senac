"""Criar um programa que apresente 2 questões sobre programação em Python. Cada questão deverá conter 4
possíveis respostas.

O programa deverá falar a nota do usuário.

Colocar o código em...

Utilizar a pasta com seu nome."""

enunciado = {0: "Como fazer comentário de várias linhas em Python?", 
             1: "O que faz o método pop() em Python?", 
             2: "Qual é a função utilizada para imprimir na tela em Python?",
               3: "Qual é o operador utilizado para realizar uma exponenciação em Python?",
             4: "Qual é a função do método 'append' em listas?", 
             5: "Qual é a função do método 'extend' em listas?", 
             6: "O que significa 'def' na linguagem Python?", 
             7: "O que acontece se utilizarmos o 'while' no Python?", 
             8: "O que é uma CLASSE em Python?", 
             9: "Das opções abaixo, qual define melhor a definição de 'Class Inheritance' em Python?",
             10: "Qual a linguagem que está dominando a programação?", 
             11: "Qual a linguagem mais antiga da programação?", 
             12: "Qual o comando em Python para criar uma função?", 
             13: "O que é um 'for'?", 
             14: "Qual foi o ano que a linguagem de programação Python foi criada?", 
             15: "Quem foi o criador do Python?", 
             16: "Qual linguagem de programação é representada por um símbolo?", 
             17: "Qual a declaração dada pelo usuário no sistema que não pode ser mudada ao decorrer do programa?",
             18: "Qual alternativa não faz parte da atribuição da programação em Python?", 
             19: "Quais são as aplicações do Python?", 
             20: "O Python foi criado em qual país?", 
             21: "Qual das linguagens de programação abaixo é a mais importante?"}
opcoes = {0: 'a) Colocar duas cerquilhas (##) antes e duas cerquilhas depois (##) \n b) Colocar três exclamações (!!!) antes e três exclamações depois (!!!) \n c) Colocar dois sinais de menor e dois hífens antes (<<--) e dois hífens e dois sinais de maior depois (-->>)\n d) Colocar três aspas duplas (""") antes e três aspas duplas depois (""") \n',
           1:"a) Printa um texto na tela\n b) Apaga (esvazia) uma lista\n c) Remove um elemento de uma lista\n d) Enumera os elementos de uma lista\n",
           2: "a) print() \n b) display() \n c) show() \n d) output()", 
           3: "a) ^ \n b) ** \n c) exp() \n d) power()", 
           4: "a) Adiciona um elemento ao final da lista \n b) Remove o último elemento da lista \n c) Inverte a ordem dos elementos \n d) Cria uma nova lista",
           5: "a) Adiciona um elemento ao final da lista \n b) Inverte a ordem dos elementos \n c) Inserir mais de um item em uma lista \n d) Cria uma nova lista", 
           6: "a) Definição de uma função \n b) Definição extra funcional \n c) Definição Exógena Fonética \n d) Definição de uma variável", 
           7: "a) Vai dar um erro, pois só funciona em JC \n b) É uma forma de criar um looping para tal condição \n c) Cria uma variável\n d) Nenhuma das opções anteriores",
           8: "a) Uma classe é uma VARIÁVEL \n b) Uma classe é um endereço de memória onde o Python armazena informações \n c) Uma classe é uma template para criação de objetos \n d) Uma classe é uma lista ou tupla especificamente", 
           9: "a) Class Inheritance é o mesmo que renomear uma classe \n b) Inheritance significa herdar os atributos e métodos de uma classe pai \n c) Inheritance significa atribuir um valor a uma variável dentro de uma única expressão \n d) Uma classe é uma lista ou tupla especificamente",
           10: "a) Java \n b) PHP \n c) Python \n d) C#", 
           11: "a) COBOL\n b) Simula \n c) LISP \n d) APL", 
           12: "a) function \n b) def \n c) função \n d) for", 
           13: "a) Estruturas de repetição \n b) Uma função \n c) Um framework \n d) Uma linguagem de programação", 
           14: "a) 1991 \n b) 1999\n c) 1989 \n d) 2009",
           15: "a) Bill Gates \n b) João Paulo \n c) Guido Van Rossum \n d) Michael", 
           16: "a) Python \n b) JAVA \n c) C++ \n d) Portugol", 
           17: "a) Variável \n b) Vetor \n c) Matriz \n d) Constante", 
           18: "a) Desenvolvimento Web (Django e Flask) \n b) Big Data \n c) Não é uma programação lógica \n d) Machine Learning", 
           19: "a) Não consegue desenvolver site \n b) Linguagem defasada \n c) Testagem de software/banco de dados \n d) Não trabalha com dados",
           20: "a) Holanda \n b) Portugal \n c) Reino Unido \n d) Tailândia", 
           21: "a) Python \n b) Java \n c) C# \n d) Todas as listadas acima"}
resposta = {0: "d", 1: "c", 2: "a", 3: "b", 4: "a", 5: "c", 6: "a", 7: "b", 8: "c", 9: "b", 10: "c", 11: "a", 12: "b", 13: "a", 14: "c", 15: "a", 16: "c", 17: "d", 18: "a", 19: "c", 20: "a", 21: "d"}
nota = 0

print("Bem-vindo ao programa de perguntas sobre Python!")

def questao():
    nota=0
    questnum = 1
    i = 0
    while i <= (len(enunciado) - 1):
        print(f"Questão {questnum}: \n {enunciado[i]} \n {opcoes[i]}")
        respquest = str(input("Digite a letra correspondente a sua resposta: \n")).lower()
        if respquest == resposta[i]:
            nota = nota + 5
        questnum += 1
        i += 1
    return nota

resultado=questao()

print(f"Fim do questionário. Sua nota é {resultado} de 120.")
