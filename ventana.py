import tkinter as tk

class Aplicacion:
    def __init__(self) -> None:
        self.valor=1
        self.v1=tk.Tk()
        self.v1.title("SEGUNDO INFORMATICA")
        self.lbl_numero= tk.Label(self.v1, text=self.valor)
        self.lbl_numero.grid(column=0, row=0)
        self.lbl_numero.configure(foreground="red")

        self.btn_inc = tk.Button(self.v1, text="Incrementar" command=self.incrementar)
        self.btn_inc.grid(column=0, row=1)

        self.btn_dec = tk.Button(self.v1, text="Decrementar")
        self.btn_dec.grid(column=0, row=2)

        self.v1.mainloop()

    def incrementar(self):
        self.valor = self.valor +1
        self.lbl_num.config(text=self.valor)

app = Aplicacion()
        

