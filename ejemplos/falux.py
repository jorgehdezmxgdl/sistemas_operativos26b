from estructura.Cola import Encolamiento
from procesos.Proceso import Proceso

class Falux():
    def __init__(self):
        self.colaListos = Encolamiento()
        self.colaE_S    = Encolamiento()

    def adiciona_proceso(self, proceso):
        self.colaListos.adiciona(proceso)

    def ejecuta_planificador(self):
        while not self.colaListos.esta_vacio():
            proceso = self.colaListos.sig_elemento_procesar()
            print(proceso.info())
        print("No hay mas procesos")

f = Falux()
f.adiciona_proceso(Proceso("nombre1","suma"))
f.adiciona_proceso(Proceso("nombre2","division"))
f.adiciona_proceso(Proceso("nombre3","resta"))
f.ejecuta_planificador()
