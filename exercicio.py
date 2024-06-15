#Criar um enunciado para a prova abaixo.


""" 01. a) Crie uma lista de frutas "frutas" contendo "maçã", "banana", "laranja" e "uva. b) anexe o elemento "morango" ao fim da lista e c) depois remova o elemento "banana".
"""
01. 
a) frutas = ['maçã', 'banana', 'laranja', 'uva']
b) frutas.append('morango')
c) frutas.remove('banana')

""" 02. a) Crie uma tupla com números 1 a 5 (inclusive). b) crie uma variável que receba o terceiro elemento da tupla pelo índice.
"""

02. 
a) numeros = (1, 2, 3, 4, 5)
b) terceiro_elemento = numeros[2]

""" 03. a) Crie um dicionário de nome "notas" com 3 alunos, de nome João, Maria e Carlos, e atribua, respectivamente, suas notas 8, 9 e 7 (tipo int).
b) Baixe a nota de Ana para 6. c) Remova as notas de Carlos.
"""

03. 
a) notas = {'João': 8, 'Maria': 9, 'Carlos': 7}
b) notas['Ana'] = 6
c) del notas['Carlos']

""" 04. a) Crie uma lista dos números pares de 2 a 11, usando range. b) Crie uma lista dos números ímpares de 2 a 10, usando range. c) crie nova lista concatenando
 ambas as listas anteriores (primeiro os pares, depois os ímpares).
"""

04. 
a) numeros_pares = list(range(2, 11, 2))
b) numeros_impares = list(range(1, 10, 2))
c) todos_numeros = numeros_pares + numeros_impares

""" 05. a) A partir da lista "frutas" do exercício 1 imprima todos os elementos na tela. b) a partir da tupla "numeros" do exercício 2, imprima todos os elementos na tela
usando o loop while, "len" e referência ao índice
"""

05. 
a)	for fruta in frutas:
    		print(fruta)
b)	i = 0
	while i < len(numeros):
    		print(numeros[i])
    		i += 1

""" 06. a) coloque numa lista todos os quadrados de números inteiros entre 1 e 5
b) inverta a lista (coloque elementos do maior para o menor)
c) imprima a lista em formato de string, usando vírgula como separador
"""

06. 
a) numeros_quadrados = [x ** 2 for x in range(1, 6)]
b) numeros_quadrados.reverse()
c) print(','.join(map(str, numeros_quadrados)))

""" 07. a) coloque numa tupla as cores "vermelho", "verde", "azul" e "amarelo"
b) estoque apenas as cores primárias em uma segunda tupla, usando sintaxe de range de índice (index range)
"""

07. 
a) cores = ('vermelho', 'verde', 'azul', 'amarelo')
b) cores_primarias = cores[:2]

""" 08. a) Faça um dicionário atribuindo idades a 3 pessoas {'nome' : idade}
b) crie um loop que imprima, um por um, os itens do dicionário com suas idades respectivas na forma "Fulano tem X anos."
"""

08. 
a) idades = {'Alice': 25, 'Bob': 30, 'Charlie': 22}
b)	for nome, idade in idades.items():
    		print(f"{nome} tem {idade} anos")

"""09. a) coloque numa lista todos os cubos de números inteiros entre 1 e 4 (inclusive)
b) retire o último elemento da lista com .pop
c) imprima a lista em formato de string, usando vírgula como separador
"""

09. 
a) numeros_cubos = [x ** 3 for x in range(1, 5)]
b) numeros_cubos.pop()
c) print(','.join(map(str, numeros_cubos)))

"""10. a) coloque numa lista o dobro dos números pares entre 2 e 8 (inclusive)
b) coloque numa tupla o quadrado dos números ímpares entre 1 e 7 (inclusive)
"""

10. 
a) dobro_pares = [x * 2 for x in range(2, 9, 2)]
b) quadrado_impares = tuple(x ** 2 for x in range(1, 8, 2))
