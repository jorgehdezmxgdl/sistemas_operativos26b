import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import tkinter as tk
from tkinter import ttk, messagebox
import random
from procesos.Proceso import Proceso
from estructura.Cola import Encolamiento

QUANTUM = 3
TICK_MS = 600
COLORES = ['#FFB3BA','#BAFFC9','#BAE1FF','#FFFFBA','#E0BBE4','#FEC8D8','#D0F4DE']

class Application:
    def __init__(self, root):
        self.root = root
        root.title("SO · Planificador de Procesos")
        root.geometry("560x720")
        root.update_idletasks()
        root.geometry(f"+{(root.winfo_screenwidth()-560)//2}+{(root.winfo_screenheight()-720)//2}")

        menubar = tk.Menu(root)
        archivo = tk.Menu(menubar, tearoff=0)
        archivo.add_command(label="Cerrar app", command=root.destroy)
        menubar.add_cascade(label="Archivo", menu=archivo)
        procesos = tk.Menu(menubar, tearoff=0)
        procesos.add_command(label="Visor", command=self.on_procesos_visor)
        procesos.add_command(label="Planificador", command=self.on_procesos_planificador)
        menubar.add_cascade(label="Procesos", menu=procesos)
        root.configure(menu=menubar)

        tk.Label(root, text="App a ejecutar:").place(x=20, y=15)
        self.cmbApp = ttk.Combobox(root, values=["Spotify","Calculadora","Bloc de Notas","Compaq"], state="readonly")
        self.cmbApp.place(x=120, y=12, width=160, height=26)
        self.cmbApp.current(0)
        tk.Button(root, text="Crear proceso", bg="#4CAF50", fg="white",
                  command=self.on_crear_proceso).place(x=300, y=10, width=120, height=30)
        tk.Button(root, text="Pausar / Continuar", bg="#FF9800",
                  command=self.on_toggle).place(x=430, y=10, width=120, height=30)

        self.notebook = ttk.Notebook(root)
        self.notebook.place(x=20, y=55, width=520, height=200)
        for t in ["Spotify","Calculadora","Bloc de Notas","Compaq"]:
            self.notebook.add(ttk.Frame(self.notebook), text=t)

        tk.Label(root, text="  Estados del Sistema Operativo  ⬇",
                 font=("Arial",11,"bold")).place(x=20, y=265)
        self.canvas = tk.Canvas(root, bg="#1e1e1e", highlightthickness=0)
        self.canvas.place(x=20, y=290, width=520, height=400)

        self.cola_listos = Encolamiento()
        self.procesos = []
        self.cpu = None
        self.bloqueados = []
        self.terminados = []
        self.contador = 0
        self.pausado = False
        self.tick()

    def on_crear_proceso(self):
        app = self.cmbApp.get()
        self.contador += 1
        nombre = f"P{self.contador}"
        actividad = random.choice(["suma","resta","multiplicacion","division"])
        p = Proceso(nombre, actividad)
        p.estado = "listo"
        p.quantum = QUANTUM
        p.ticks_bloq = 0
        p.color = random.choice(COLORES)
        p.app = app
        self.cola_listos.adiciona(p)
        self.procesos.append(p)

    def on_toggle(self):
        self.pausado = not self.pausado

    def tick(self):
        if not self.pausado:
            if self.cpu is None and not self.cola_listos.esta_vacio():
                self.cpu = self.cola_listos.sig_elemento_procesar()
                self.cpu.estado = "ejecutando"
                self.cpu.quantum = QUANTUM

            if self.cpu is not None:
                self.cpu.quantum -= 1
                if random.random() < 0.18:
                    self.cpu.estado = "bloqueado"
                    self.cpu.ticks_bloq = random.randint(2, 4)
                    self.bloqueados.append(self.cpu)
                    self.cpu = None
                elif random.random() < 0.12:
                    self.cpu.estado = "terminado"
                    self.terminados.append(self.cpu)
                    self.cpu = None
                elif self.cpu.quantum <= 0:
                    self.cpu.estado = "listo"
                    self.cola_listos.adiciona(self.cpu)
                    self.cpu = None

            for p in list(self.bloqueados):
                p.ticks_bloq -= 1
                if p.ticks_bloq <= 0:
                    p.estado = "listo"
                    self.bloqueados.remove(p)
                    self.cola_listos.adiciona(p)

            self.dibujar()
        self.root.after(TICK_MS, self.tick)

    def dibujar(self):
        self.canvas.delete("all")
        areas = [
            ("LISTOS",     [p for p in self.procesos if p.estado=="listo"],     "#4CAF50"),
            ("CPU",        [self.cpu] if self.cpu else [],                      "#FF9800"),
            ("BLOQUEADOS", self.bloqueados,                                     "#2196F3"),
            ("TERMINADOS", self.terminados[-6:],                                "#9E9E9E"),
        ]
        w = 120
        for i,(titulo,lista,color) in enumerate(areas):
            x = 10 + i*(w+10)
            self.canvas.create_rectangle(x, 10, x+w, 385, outline=color, width=2, fill="#2a2a2a")
            self.canvas.create_text(x+w//2, 28, text=titulo, fill=color, font=("Arial",11,"bold"))
            if titulo == "CPU" and lista:
                self.canvas.create_text(x+w//2, 48, text=f"q={lista[0].quantum}", fill="yellow", font=("Arial",9))
            for j,p in enumerate(lista[:7]):
                y = 65 + j*42
                self.canvas.create_rectangle(x+5, y, x+w-5, y+36, fill=p.color, outline="black")
                self.canvas.create_text(x+w//2, y+12, text=p.nombre_proceso, font=("Arial",10,"bold"))
                self.canvas.create_text(x+w//2, y+26, text=f"{p.app} · {p.actividad}", font=("Arial",8))

    def on_procesos_visor(self):
        messagebox.showinfo("Visor", f"Procesos creados: {len(self.procesos)}")
    def on_procesos_planificador(self):
        messagebox.showinfo("Planificador", f"Algoritmo: Round-Robin\nQuantum: {QUANTUM} ticks")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()