
from datetime import datetime

def converter_cal_chines(data_gregoriana):
    data_inicial = datetime.strptime("1900-01-31", "%Y-%m-%d")
    diferenca_dias = (data_gregoriana - data_inicial).days

    ciclo_sexagenario = 12
    ciclo_inicial = 36

    ano_chines = ciclo_inicial + (diferenca_dias / 365.25)

    zodiaco_chines = ["🐭 Rato ou Camundongo", "Boi ou Búfalo", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Carneiro ou Bode", "Macaco", "Galo", "Cachorro", "Porco ou Javali"]
    animal_zodiaco = zodiaco_chines[int(ano_chines) % ciclo_sexagenario]
    elementos = [" de metal", " de água", " de madeira", " de fogo", " de terra"]

    ano_elemento = ano_chines

    if ano_elemento > 95.986 and ano_elemento <= 155.978:
        ano_elemento = ano_elemento - 59.983
    elif ano_elemento > 155.978:
        ano_elemento = ano_elemento - 119.978

    if 0 <= ano_elemento and ano_elemento < 38.02:
        elemento = elementos[0]
    elif 38.02 < ano_elemento and ano_elemento <= 40.03:
        elemento = elementos[1]
    elif 40.03 < ano_elemento and ano_elemento <= 41.97:
        elemento = elementos[2]
    elif 41.97 < ano_elemento and ano_elemento <= 44:
        elemento = elementos[3]
    elif 44 < ano_elemento and ano_elemento <= 46.02:
        elemento = elementos[4]
    elif 46.02 < ano_elemento and ano_elemento <= 48.04:
        elemento = elementos[0]
    elif 48.04 < ano_elemento and ano_elemento <= 49.98:
        elemento = elementos[1]
    elif 49.98 < ano_elemento and ano_elemento <= 52:
        elemento = elementos[2]
    elif 52 < ano_elemento and ano_elemento <= 54.02:
        elemento = elementos[3]
    elif 54.02 < ano_elemento and ano_elemento <= 56.04:
        elemento = elementos[4]
    elif 56.04 < ano_elemento and ano_elemento < 57.98:
        elemento = elementos[0]
    elif 57.98 < ano_elemento and ano_elemento <= 60:
        elemento = elementos[1]
    elif 60 < ano_elemento and ano_elemento <= 62.03:
        elemento = elementos[2]
    elif 62.03 < ano_elemento and ano_elemento <= 63.97:
        elemento = elementos[3]
    elif 63.97 < ano_elemento and ano_elemento <= 65.99:
        elemento = elementos[4]
    elif 65.99 < ano_elemento and ano_elemento <= 68.01:
        elemento = elementos[0]
    elif 68.01 < ano_elemento and ano_elemento <= 70.03:
        elemento = elementos[1]
    elif 70.03 < ano_elemento and ano_elemento <= 71.97:
        elemento = elementos[2]
    elif 71.97 < ano_elemento and ano_elemento <= 73.99:
        elemento = elementos[3]
    elif 73.99 < ano_elemento and ano_elemento <= 76.01:
        elemento = elementos[4]
    elif 76.01 < ano_elemento and ano_elemento <= 78.03:
        elemento = elementos[0]
    elif 78.03 < ano_elemento and ano_elemento <= 79.97:
        elemento = elementos[1]
    elif 79.97 < ano_elemento and ano_elemento <= 82:
        elemento = elementos[2]
    elif 82 < ano_elemento and ano_elemento <= 84.02:
        elemento = elementos[3]
    elif 84.02 < ano_elemento and ano_elemento <= 86.04:
        elemento = elementos[4]
    elif 86.04 < ano_elemento and ano_elemento <= 87.98:
        elemento = elementos[0]
    elif 87.98 < ano_elemento and ano_elemento <= 90:
        elemento = elementos[1]
    elif 90 < ano_elemento and ano_elemento <= 92.02:
        elemento = elementos[2]
    elif 92.02 < ano_elemento and ano_elemento <= 94.04:
        elemento = elementos[3]
    elif 94.04 < ano_elemento and ano_elemento <= 95.986:
        elemento = elementos[4]
    else:
        elemento = " (Elemento a definir)"

    return f"Signo chinês: {animal_zodiaco}{elemento}."

print("Calculadora de Horóscopo Chinês com Elemento (de 1900 a 2080) \n De Simone Campos com base em programa do professor Carlos Alberto Machado Jr.")
data_nascimento = input("Digite a data do seu nascimento (DD/MM/AAAA): ")
data_gregoriana = datetime.strptime(data_nascimento, "%d/%m/%Y")

data_chinesa = converter_cal_chines(data_gregoriana)
print(data_chinesa)
