# usuário vai escolher o volume e depois o capítulo e vc tem que mostrar tudo
# 6 opções no menu

def limpaTela():
    if os.name == 'posix':  # Para sistemas Unix/Linux/MacOS.
        os.system('clear')
    elif os.name == 'nt':  # Para sistemas Windows.
        os.system('cls')

print("Digite...")
print("1 para o volume I")
print("2 para o volume II")
print("3 para o volume III")
print("4 para o volume IV")
print("5 para o volume V")
print("6 para o volume VI")
print("0 para sair do programa")
resposta = input("Resposta: ")

if resposta == "0":
    limpaTela()
    print("Programa encerrado.")
elif resposta == "1":
    print("1,1 The Wonderful Wizard of Oz	1900	L. Frank Baum	1956")
    print("1,2	The Marvelous Land of Oz	1904	L. Frank Baum	1960")
    print("1,3	Ozma of Oz	1907	L. Frank Baum	1983")
    print("1,4	Dorothy and the Wizard in Oz	1908	L. Frank Baum	1984")
    print("1,5	The Road to Oz	1909	L. Frank Baum	1985")
    print("1,6	The Emerald City of Oz	1910	L. Frank Baum	1986")
elif resposta == "2":
    print("2,1	The Sea Fairies	1911	L. Frank Baum	1987")
    print("2,2	Sky Island	1912	L. Frank Baum	1988")
elif resposta == "3":
    print("3,1	The Patchwork Girl of Oz	1913	L. Frank Baum	1989")
    print("3,2	Tik-Tok of Oz	1914	L. Frank Baum	1990")
    print("3,3	The Scarecrow of Oz	1915	L. Frank Baum	1991")
    print("3,4	Rinkitink in Oz	1916	L. Frank Baum	1992")
    print("3,5	The Lost Princess of Oz	1917	L. Frank Baum	1993")
    print("3,6	The Tin Woodman of Oz	1918	L. Frank Baum	1994")
    print("3,7	The Magic of Oz	1919	L. Frank Baum	1995")
    print("3,8	Glinda of Oz	1920	L. Frank Baum	1996")
elif resposta == "4":
    print("4,1	The Royal Book of Oz	1921	Ruth Plumly Thompson	1997")
    print("4,2	Kabumpo in Oz	1922	Ruth Plumly Thompson	1998")
    print("4,3	The Cowardly Lion of Oz	1923	Ruth Plumly Thompson	2019")
    print("4,4	Grampa in Oz	1924	Ruth Plumly Thompson	2020")
    print("4,5	The Lost King of Oz	1925	Ruth Plumly Thompson	2021")
    print("4,6	The Hungry Tiger of Oz	1926	Ruth Plumly Thompson	2022")
    print("4,7	The Gnome King of Oz	1927	Ruth Plumly Thompson	2023")
elif resposta == "5":
    print("5,1	The Wishing Horse of Oz	1935	Ruth Plumly Thompson	1963")
    print("5,2	Captain Salt in Oz	1936	Ruth Plumly Thompson	1964")
    print("5,3	Handy Mandy in Oz	1937	Ruth Plumly Thompson	1965")
    print("5,4	The Silver Princess in Oz	1938	Ruth Plumly Thompson	1966")
    print("5,5	Ozoplaning with the Wizard of Oz	1939	Ruth Plumly Thompson	1967")
elif resposta == "6":
    print("6,1	The Magical Mimics in Oz	1946	Jack Snow	1974")
    print("6,2	The Shaggy Man of Oz	1949	Jack Snow	1977")
else:
    limpaTela()
    print("Opção inválida")

input("Pressione ENTER para continuar.")
