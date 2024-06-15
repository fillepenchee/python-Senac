
def limpaTela():
    if os.name == 'posix':  # Para sistemas Unix/Linux/MacOS.
        os.system('clear')
    elif os.name == 'nt':  # Para sistemas Windows.
        os.system('cls')

def obterVolume(mensagem, numLiv):
    while True:
        print(mensagem)
        for vol, liv, title, year, author, dompub in numLiv.items():
            print(f"Volume: {vol} Livro: {liv} Ano:{year} Autor: {author} Ano de domínio público: {dompub}.")
        if resposta = input(numLiv):
            for 
        else:
            print("Opção incorreta, Digite um número válido de 0 a 6: \n")




print("2,1	The Sea Fairies	1911	L. Frank Baum	1987")
print("2,2	Sky Island	1912	L. Frank Baum	1988")



    menu = obter_opcao("Digite...", {"1": "ADIÇÃO", "2": "SUBTRAÇÃO", "3": "MULTIPLICAÇÃO", "4": "DIVISÃO", "5": "DIVISÃO INTEIRA", "6": "MÓDULO", "7": "EXPONENCIAÇÃO", "8": "RAIZ", "9": "FATORIAL", "10": "LOGARITMAÇÃO", "0": "SAIR DO SOFTWARE"})