from PIL import TiffImagePlugin
from PIL import TiffImagePlugin
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  

class MainVentana():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sistemas operativos")
        self.ventana.geometry("500x300")
        self.creaEtiqueta("Ingresa un numero", 30, 30, 100, 20)
        self.text01 = self.creaCampoTexto(150, 30, 100, 20)
        self.creaButton("Enviar dato", 270, 30, 100, 20)
        self.creaImagen("imgs/images.jpg", 80, 80, 100, 100)
        self.ventana.mainloop()

    def creaEtiqueta(self, texto, posicionx, posiciony, ancho, largo):
        etiqueta = tk.Label(self.ventana, text=texto)
        etiqueta.place(x=posicionx, y=posiciony, width=ancho, height=largo)

    def creaCampoTexto(self, posicionx, posiciony, ancho, largo):
        campoTexto = tk.Entry(self.ventana)
        campoTexto.place(x=posicionx, y=posiciony, width=ancho, height=largo)
        return campoTexto

    def creaImagen(self, ubicacion, posicionx, posiciony, ancho, largo):
        pil_image = Image.open(ubicacion)
        pil_image = pil_image.resize((ancho,largo))
        tk_image  = ImageTk.PhotoImage(pil_image)
        etiqueta  = tk.Label(self.ventana, image=tk_image)
        etiqueta.image = tk_image 
        etiqueta.place(x=posicionx, y=posiciony, width=ancho, height=largo)

    def evento_button(self):
        datoLeido = self.text01.get()
        messagebox.showinfo("Informacion", "Se ha presionado el boton " + datoLeido)

    def creaButton(self, texto, posicionx, posiciony, ancho, largo):
        boton = tk.Button(self.ventana, text=texto, command=self.evento_button)
        boton.place(x=posicionx, y=posiciony, width=ancho, height=largo)

ui = MainVentana()
