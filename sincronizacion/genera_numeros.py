import tkinter as tk
from tkinter import ttk
import threading
import time

class Application:
    def __init__(self, root):
        self.root = root
        root.title("Sistemas operativos :: Sincronización")
        root.geometry("460x250")
        root.update_idletasks()
        root.geometry(
            f"+{(root.winfo_screenwidth() - 460) // 2}"
            f"+{(root.winfo_screenheight() - 250) // 2}"
        )

        self.label1 = tk.Label(root, text="Generación de números", fg="#2a7aac", font=("Helvetica", 10, "bold"))
        self.label1.place(x=90, y=10, width=190, height=30)

        self.label2 = tk.Label(root, text="Par")
        self.label2.place(x=35, y=44, width=90, height=26)

        self.label3 = tk.Label(root, text="Impar")
        self.label3.place(x=200, y=44, width=90, height=26)

        self.listaPar = tk.Listbox(root)
        self.listaPar.place(x=35, y=80, width=110, height=120)

        self.listaImpar = tk.Listbox(root)
        self.listaImpar.place(x=180, y=80, width=110, height=120)

        self.btnNoHilos = tk.Button(root, text="Sin hilos", command=self.on_btnNoHilos)
        self.btnNoHilos.place(x=330, y=80, width=96, height=32)

        self.btnConHilos = tk.Button(root, text="Con hilos", command=self.on_btnConHilos)
        self.btnConHilos.place(x=330, y=125, width=96, height=32)

        self.btnSincroniza = tk.Button(root, text="Sincronización", command=self.on_btnSincroniza)
        self.btnSincroniza.place(x=330, y=168, width=96, height=32)

    def on_btnNoHilos(self):
        self.listaPar.delete(0, tk.END)
        self.listaImpar.delete(0, tk.END)
        for i in range(1000000):
            if i % 2 == 0: #% residuo de la división
                self.listaPar.insert("end", i)
            else:
                self.listaImpar.insert("end", i)
        

    def genera(self, opcion):
        for i in range(10000000):
            if opcion == "par":
                if i % 2 == 0:
                    self.listaPar.insert("end", i)
            elif opcion == "impar":
                if i % 2 != 0:
                    self.listaImpar.insert("end", i)
            time.sleep(0.03)
            

    def on_btnConHilos(self):
        self.listaPar.delete(0, tk.END)
        self.listaImpar.delete(0, tk.END)
        par   = threading.Thread(target=self.genera,args=("par",))
        impar = threading.Thread(target=self.genera,args=("impar",))
        par.start()
        impar.start()

    def on_btnSincroniza(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
