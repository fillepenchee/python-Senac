constelacoes_zodiaco = [
    "Áries",
    "Touro",
    "Gêmeos",
    "Câncer",
    "Leão",
    "Virgem",
    "Libra",
    "Escorpião",
    "Sagitário",
    "Capricórnio",
    "Aquário",
    "Peixes"
]

naturalidade = ["Niteroiense", "Carioca"]

print("Melhor signo do zodíaco:", constelacoes_zodiaco[4], ".")
print(f"Melhor signo do zodíaco: {constelacoes_zodiaco[4]}.")

print(constelacoes_zodiaco)


print("Lista das Constelações do Zodíaco (Astrologia):\n")
for constelacao in constelacoes_zodiaco:
    print(constelacao)

indice_escorpiao = constelacoes_zodiaco.index("Escorpião")
constelacoes_zodiaco.insert(8, "Serpentário")
print("Lista das Constelações do Zodíaco (Astronomia):\n")
for constelacao in constelacoes_zodiaco:
    print(constelacao)

constelacoes_zodiaco.insert(0, "Dinossauro")
print("Lista das Constelações do Zodíaco (Astronomia):\n")
for constelacao in constelacoes_zodiaco:
    print(constelacao)

constelacoes_zodiaco.append("Gonçalense")
print("Lista das Constelações do Zodíaco (Astronomia):\n")
for constelacao in constelacoes_zodiaco:
    print(constelacao)

constelacoes_zodiaco.extend(naturalidade)
print("Lista das Constelações do Zodíaco (Astronomia):\n")
for constelacao in constelacoes_zodiaco:
    print(constelacao)

constelacoes_zodiaco.remove("Dinossauro")
print("Lista das Constelações do Zodíaco (Astronomia):\n")
for constelacao in constelacoes_zodiaco:
    print(constelacao)

constelacoes_zodiaco.pop(14)
print("Lista das Constelações do Zodíaco (Astronomia):\n")
for constelacao in constelacoes_zodiaco:
    print(constelacao)

constelacoes_zodiaco.clear()
print("Lista das Constelações do Zodíaco (Astronomia):\n")
for constelacao in constelacoes_zodiaco:
    print(constelacao)

constelacoes_zodiaco = (
    "Áries",
    "Touro",
    "Gêmeos",
    "Câncer",
    "Leão",
    "Virgem",
    "Libra",
    "Escorpião",
    "Sagitário",
    "Capricórnio",
    "Aquário",
    "Peixes"
)

print("Melhor signo do zodíaco:", constelacoes_zodiaco[4], ".")
print(f"Melhor signo do zodíaco: {constelacoes_zodiaco[4]}.")

print(constelacoes_zodiaco)

constelacoes_zodiaco = list(constelacoes_zodiaco)

indice_escorpiao = constelacoes_zodiaco.index("Escorpião")
constelacoes_zodiaco.insert(8, "Serpentário")
print(constelacoes_zodiaco)

constelacoes_zodiaco = tuple(constelacoes_zodiaco)
print(constelacoes_zodiaco)




	