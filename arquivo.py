import tkinter as tk

class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador App")
        self.root.resizable(False, False)
        self.root.config(bg="#831d1c")

        self.contador = 0

        self.display = tk.Label(root, text=str(self.contador), font=('Impact', 32), bg="#831d1c", fg='white')
        self.display.pack(pady=10)

        operacoes1 = tk.Frame(root, bg="#831d1c")
        operacoes1.pack(pady=10)
        
        operacoes2 = tk.Frame(root, bg="#831d1c")
        operacoes2.pack(pady=10)

        self.botaoDezMais = tk.Button(operacoes1, text="Clique para aumentar 10 unidades", command=self.mais_10_contador)                      
        self.botaoDezMais.pack(side=tk.LEFT, padx=10)

        self.botaoMais = tk.Button(operacoes1, text="Clique para aumentar uma unidade", command=self.incrementar_contador)                      
        self.botaoMais.pack(side=tk.LEFT, padx=10)

        self.botaoZero = tk.Button(operacoes1, text="Clique para zerar o contador", command=self.zerar_contador)                      
        self.botaoZero.pack(side=tk.LEFT, padx=10)

        self.botaoMenos = tk.Button(operacoes1, text="Clique para diminuir uma unidade", command=self.decrescer_contador)                      
        self.botaoMenos.pack(side=tk.LEFT, padx=10)

        self.botaoDezMenos = tk.Button(operacoes1, text="Clique para diminuir 10 unidades", command=self.menos_10_contador)                      
        self.botaoDezMenos.pack(side=tk.LEFT, padx=10)

        self.botaoVezesDois = tk.Button(operacoes2, text="Clique para multiplicar por 2", command=self.vezes_2_contador)                      
        self.botaoVezesDois.pack(side=tk.LEFT, padx=10)

        self.botaoDividirDois = tk.Button(operacoes2, text="Clique para dividir por 2", command=self.dividir_2_contador)                      
        self.botaoDividirDois.pack(side=tk.LEFT, padx=10)

    def mais_10_contador(self):
        self.contador += 10
        self.display.config(text=str(self.contador))
        
    def incrementar_contador(self):
        self.contador += 1
        self.display.config(text=str(self.contador))

    def zerar_contador(self):
        self.contador = 0
        self.display.config(text=str(self.contador))

    def decrescer_contador(self):
        self.contador -= 1
        self.display.config(text=str(self.contador))

    def menos_10_contador(self):
        self.contador -= 10
        self.display.config(text=str(self.contador))
    
    def vezes_2_contador(self):
        self.contador = self.contador * 2
        self.display.config(text=str(self.contador))

    def dividir_2_contador(self):
        self.contador = self.contador / 2
        self.display.config(text=str(self.contador))

if __name__ == "__main__":
    root = tk.Tk()
    app = ContadorApp(root)
    root.mainloop()
