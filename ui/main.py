import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Application:
    def __init__(self, root):
        self.root = root
        root.title("Configuración de procesos")
        root.geometry("520x380")
        root.update_idletasks()
        root.geometry(
            f"+{(root.winfo_screenwidth() - 520) // 2}"
            f"+{(root.winfo_screenheight() - 380) // 2}"
        )

        menubar = tk.Menu(root)
        self.archivo_menu = tk.Menu(menubar, tearoff=0)
        self.archivo_menu.add_command(label="Cerrar app", command=self.on_archivo_cerrar_app)
        menubar.add_cascade(label="Archivo", menu=self.archivo_menu)
        self.procesos_menu = tk.Menu(menubar, tearoff=0)
        self.procesos_menu.add_command(label="Visor", command=self.on_procesos_visor)
        self.procesos_menu.add_command(label="Planificador", command=self.on_procesos_planificador)
        self.procesos_menu.add_separator()
        menubar.add_cascade(label="Procesos", menu=self.procesos_menu)
        root.configure(menu=menubar)

        self.w1 = tk.Label(root, text="Ejecutar App")
        self.w1.place(x=20, y=40, width=90, height=26)

        self.w_cmbApp = ttk.Combobox(root, values=["Spotify", "Calculadora", "Bloc de Notas", "Compaq"])
        self.w_cmbApp.place(x=130, y=38, width=160, height=28)

        self.btnEjecutarProceso = tk.Button(root, text="Ejecutar proceso", command=self.on_btnEjecutarProceso)
        self.btnEjecutarProceso.place(x=310, y=36, width=170, height=30)

        self.notebook1 = ttk.Notebook(root)
        self.notebook1_tab1 = ttk.Frame(self.notebook1)
        self.notebook1.add(self.notebook1_tab1, text="Spotify")
        self.notebook1_tab2 = ttk.Frame(self.notebook1)
        self.notebook1.add(self.notebook1_tab2, text="Calculadora")
        self.notebook1_tab3 = ttk.Frame(self.notebook1)
        self.notebook1.add(self.notebook1_tab3, text="Bloc de notas")
        self.notebook1_tab4 = ttk.Frame(self.notebook1)
        self.notebook1.add(self.notebook1_tab4, text="Compaq")
        self.notebook1.place(x=30, y=105, width=460, height=170)

        self.label2 = tk.Label(self.notebook1_tab1, text="Seleccionar canción")
        self.label2.place(x=30, y=20, width=140, height=30)

        self.button2 = tk.Button(self.notebook1_tab1, text="Anterior", command=self.on_button2)
        self.button2.place(x=40, y=85, width=96, height=32)

        self.button3 = tk.Button(self.notebook1_tab1, text="Reproducir", command=self.on_button3)
        self.button3.place(x=182, y=85, width=96, height=32)

        self.button4 = tk.Button(self.notebook1_tab1, text="Siguiente", command=self.on_button4)
        self.button4.place(x=330, y=85, width=96, height=32)

        self.listCanciones = tk.Listbox(self.notebook1_tab1)
        self.listCanciones.insert("end", "The fate of Ophellia")
        self.listCanciones.insert("end", "Danceteria")
        self.listCanciones.insert("end", "We can´t be friends")
        self.listCanciones.place(x=176, y=20, width=250, height=60)

        self.label4 = tk.Label(self.notebook1_tab2, text="Número")
        self.label4.place(x=30, y=20, width=90, height=26)

        self.txtNumero = tk.Entry(self.notebook1_tab2)
        self.txtNumero.place(x=120, y=18, width=150, height=28)

        self.btnSuma = tk.Button(self.notebook1_tab2, text="+", command=self.on_btnSuma)
        self.btnSuma.place(x=60, y=80, width=40, height=30)

        self.btnResta = tk.Button(self.notebook1_tab2, text="-", command=self.on_btnResta)
        self.btnResta.place(x=100, y=80, width=30, height=30)

        self.btnMutiplica = tk.Button(self.notebook1_tab2, text="X", command=self.on_btnMutiplica)
        self.btnMutiplica.place(x=130, y=80, width=30, height=30)

        self.btnDivide = tk.Button(self.notebook1_tab2, text="/", command=self.on_btnDivide)
        self.btnDivide.place(x=155, y=80, width=30, height=30)

        self.btnIgual = tk.Button(self.notebook1_tab2, text="=", command=self.on_btnIgual)
        self.btnIgual.place(x=185, y=80, width=30, height=30)

        self.txtCalculadora = tk.Text(self.notebook1_tab2, state="disabled")
        self.txtCalculadora.place(x=318, y=7, width=120, height=110)

        self.txtEditor = tk.Text(self.notebook1_tab3)
        self.txtEditor.place(x=10, y=10, width=440, height=120)

        self.btnCargar = tk.Button(self.notebook1_tab4, text="Cargar nómina", command=self.on_btnCargar)
        self.btnCargar.place(x=20, y=50, width=120, height=30)

        self.btnProcesar = tk.Button(self.notebook1_tab4, text="Procesar", command=self.on_btnProcesar)
        self.btnProcesar.place(x=176, y=48, width=96, height=32)

        self.btnImprimir = tk.Button(self.notebook1_tab4, text="Imprimir", command=self.on_btnImprimir)
        self.btnImprimir.place(x=318, y=46, width=96, height=32)

    def on_btnEjecutarProceso(self):
        pass

    def on_button2(self):
        pass

    def on_button3(self):
        pass

    def on_button4(self):
        pass

    def on_btnSuma(self):
        pass

    def on_btnResta(self):
        pass

    def on_btnMutiplica(self):
        pass

    def on_btnDivide(self):
        pass

    def on_btnIgual(self):
        pass

    def on_btnCargar(self):
        pass

    def on_btnProcesar(self):
        pass

    def on_btnImprimir(self):
        pass

    def on_archivo_cerrar_app(self):
        if messagebox.askyesno("Message", "Hello!"):
            pass  # TODO: what happens when they say yes

    def on_procesos_visor(self):
        pass

    def on_procesos_planificador(self):
        pass

