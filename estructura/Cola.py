import queue

class Encolamiento():
    def __init__(self):
        self.cola = queue.Queue()

    def adiciona(self, proceso):
        self.cola.put(proceso)

    def sig_elemento_procesar(self):
        return self.cola.get() if not self.esta_vacio() else None

    def total_elementos(self):
        return self.cola.qsize()

    def esta_vacio(self):
        return self.cola.empty()


