from concurrent.futures import ThreadPoolExecutor
import time

def trabajo(tarea):
    """Simula un trabajo que tarda tiempo"""
    print(f"Procesando {tarea}")
    time.sleep(2)
    print(f"Trabajo {tarea} completado")

def inicia():
    with ThreadPoolExecutor(max_workers=4) as executor:
        for i in range(4):
            executor.submit(trabajo, i)
    print("Todos los trabajos han sido completados")

if __name__ == "__main__":
    inicia()
    