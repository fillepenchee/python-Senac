

def limpaTela():
    if os.name == 'posix':  # Para sistemas Unix/Linux/MacOS.
        os.system('clear')
    elif os.name == 'nt':  # Para sistemas Windows.
        os.system('cls')

def escolheVol():
    while True:
        limpaTela()
        if numVol in menuVol:
            return respostaVol
        else:
            input("Opção inválida. Pressione ENTER para continuar.")

def menuVol(opcao):
    menuVol = input("Digite...", {"1": "1,1	The Wonderful Wizard of Oz; 1,2	The Marvelous Land of Oz; 1,3 Ozma of Oz; 1,4 Dorothy and the Wizard in Oz; 1,5	The Road to Oz;"
    "1,6 The Emerald City of Oz", "2": "2,1	The Sea Fairies; 2,2	Sky Island", "3": "3,1	The Patchwork Girl of Oz; 3,2	Tik-Tok of Oz; 3,3	The Scarecrow of Oz;"
    "3,4	Rinkitink in Oz; 3,5	The Lost Princess of Oz; 3,6	The Tin Woodman of Oz; 3,7	The Magic of Oz; 3,8	Glinda of Oz", "4": "4,1 The Royal Book of Oz;"
"4,2	Kabumpo in Oz; 4,3;	The Cowardly Lion of Oz; 4,4	Grampa in Oz; 4,5	The Lost King of Oz; 4,6	The Hungry Tiger of Oz; 4,7	The Gnome King of Oz",
"5": "5,1	The Wishing Horse of Oz; 5,2	Captain Salt in Oz; 5,3	Handy Mandy in Oz; 5,4	The Silver Princess in Oz; 5,5	Ozoplaning with the Wizard of Oz",
"6": "6,1	The Magical Mimics in Oz; 6,2	The Shaggy Man of Oz", "0": "SAIR"})

while True:
    escolheVol()


















"""def escolheLiv(numLiv, descLiv):
    while True:
        limpaTela()
        numLiv = input("Digite o número do Livro desejado: \n")
        if numLiv in menuLiv:
            return resposta
        else:
            input("Opção inválida. Pressione ENTER para continuar.")





menuVol = "Digite...", {"1": "ADIÇÃO", "2": "SUBTRAÇÃO", "3": "MULTIPLICAÇÃO", "4": "DIVISÃO", "5": "DIVISÃO INTEIRA", "6": "MÓDULO", "0": "SAIR DO SOFTWARE"})

menuLiv = "Digite...", {"1": "ADIÇÃO", "2": "SUBTRAÇÃO", "3": "MULTIPLICAÇÃO", "4": "DIVISÃO", "5": "DIVISÃO INTEIRA", "6": "MÓDULO", "0": "SAIR DO SOFTWARE"})
fazer 6
"""
