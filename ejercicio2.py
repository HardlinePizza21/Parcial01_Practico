import time
import math

def swap(conjunto, i, j):
    conjunto[i], conjunto[j] = conjunto[j], conjunto[i]

def generarPermutaciones(conjunto, inicio, fin, tiempos_ejecucion):
    if inicio == fin:
        print(conjunto)
    else:
        for i in range(inicio, fin + 1):
            swap(conjunto, inicio, i)
            
            inicio_tiempo = time.time()
            generarPermutaciones(conjunto, inicio + 1, fin, tiempos_ejecucion)
            fin_tiempo = time.time()
            
            tiempo_ejecucion = fin_tiempo - inicio_tiempo
            tiempos_ejecucion.append(tiempo_ejecucion)
            
            swap(conjunto, inicio, i)

conjuntos = [
    [1, 2, 3],
    [1, 2, 3, 4],
    ['a', 'b', 'c', 'd', 'e'],
    [1, 2, 3, 4, 5, 6]
 
]


# Procesa cada conjunto
for conjunto in conjuntos:
    tiemposEjecucion = []
    print(f"\nGenerando permutaciones para el conjunto: {conjunto}")
    

    if len(conjuntos) >= 19:
        print("Hay demasiados conjuntos")
        break
        
    if len(conjunto) >= 10:
        print("El conjunto es demasiado grande")
        continue
    
    # Generar permutaciones y medir tiempos
    generarPermutaciones(conjunto, 0, len(conjunto) - 1, tiemposEjecucion)

    # Numero de permutaciones
    num_permutaciones = math.factorial(len(conjunto))
    print(f"Permutaciones generadas: {num_permutaciones}")
    
    # Validacion
    if len(tiemposEjecucion) == 0:
        print("No se generaron permutaciones.")
    else:
        # Calcula el tiempo promedio de ejecucion
        tiempo_promedio = sum(tiemposEjecucion) / len(tiemposEjecucion)
        print(f"Timepo promedio de ejecucion por permutacion {tiempo_promedio:.10f} segundos")

