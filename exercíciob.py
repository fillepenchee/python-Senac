
numeros_cubos = [x ** 3 for x in range(1, 5)]
numeros_cubos.pop()
print(','.join(map(str, numeros_cubos)))
