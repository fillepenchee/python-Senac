import tkinter as tk

class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Simone")
        self.root.resizable(False, False)
        self.root.config(bg="#831d1c")

        self.contador = 0

        self.display = tk.Label(root, text=str(self.contador), font=('Impact', 32), bg="#831d1c", fg='white')
        self.display.pack(pady=10)

        operacoes1 = tk.Frame(root, bg="#831d1c")
        operacoes1.pack(pady=20, padx=30)
        
        operacoes2 = tk.Frame(root, bg="#831d1c")
        operacoes2.pack(pady=20, padx=30)

        self.botaoAdicao = tk.Button(operacoes1, text="+", command=self.adicao)                      
        self.botaoAdicao.pack(side=tk.LEFT, padx=20, pady=20)

        self.botaoSubtracao = tk.Button(operacoes1, text="-", command=self.subtracao)                      
        self.botaoSubtracao.pack(side=tk.LEFT, padx=20, pady=20)

        self.botaoDivisao = tk.Button(operacoes2, text="/", command=self.divisao)                      
        self.botaoDivisao.pack(side=tk.LEFT, padx=20, pady=20)

        self.botaoMultiplica = tk.Button(operacoes2, text="x", command=self.multiplica)                      
        self.botaoMultiplica.pack(side=tk.LEFT, padx=20, pady=20)

    def adicao(self):
        self.contador += 10
        self.display.config(text=str(self.contador))
    
    def subtracao(self):
        self.contador -= 10
        self.display.config(text=str(self.contador))

    def divisao(self):
        self.contador /= 10
        self.display.config(text=str(self.contador))

    def multiplica(self):
        self.contador *= 10
        self.display.config(text=str(self.contador))


campoNumero = Entry(calculadora, width=63)
campoNumero.place(x= 50, y= 40)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContadorApp(root)
    root.mainloop()
