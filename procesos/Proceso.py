import threading
import random

class Proceso():
    def __init__(self, nombre_proceso, actividad):
        self.nombre_proceso = nombre_proceso
        self.actividad = actividad

    def define_actividad(self):
        numero1 = random.randint(1, 100)
        numero2 = random.randint(1, 100)
        self.ejecuta(self.actividad, numero1, numero2)

    def ejecuta(self, operacion, num1, num2):
        print(f'El proceso {self.nombre_proceso} está ejecutando la operacion {operacion} con los numeros {num1} y {num2}')
        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            if num2 == 0:
                print(f'El proceso {self.nombre_proceso} no puede ejecutar la operacion division con el numero {num2} porque es cero')
                return
            resultado = num1 / num2
        print(f'El proceso {self.nombre_proceso} terminó de ejecutar la operacion {operacion} con los numeros {num1} y {num2} y el resultado es {resultado}')
        
    def crea_proceso(self, num_procesos):
        for i in range(num_procesos):
            operacion = random.choice(["suma", "resta", "multiplicacion", "division"])
            p = Proceso("hilo" + str(i), operacion)
            hilo = threading.Thread(target=p.define_actividad)
            hilo.start()

    def info(self):
        return f"Nombre del proceso: {self.nombre_proceso}"

