import time

def minimoMonedas(cantidad, monedas):

    min_monedas = [float('inf')] * (cantidad + 1)
    min_monedas[0] = 0 
    
    for m in range(1, cantidad + 1):
        for moneda in monedas:
            if moneda <= m:
                min_monedas[m] = min(min_monedas[m], min_monedas[m - moneda] + 1)
    
    # Verifica la solucion
    if min_monedas[cantidad] == float('inf'):
        return -1  # Indica que no es posible dar el cambio exacto
    else:
        return min_monedas[cantidad]

# Lista de conjuntos de denominaciones de monedas y valores a probar
casos_de_prueba = [
    (10000000, [1, 2, 5,10, 20, 30 ,50, 60, 75, 13]),          
    (7, [2, 5, 10]),          
    (17, [1, 3, 4]),          
    (8, [1, 3, 4, 5]),       
]

# Procesar cada caso de prueba
for cantidad, monedas in casos_de_prueba:

    if cantidad >= 100000000:
        print("Valor muy alto, prueba otro")
        continue
    if len(monedas) >= 15:
        print("Mucha variedad de monedas")
        continue


    # Medir el tiempo de ejecución de la función minimo_monedas
    inicio_tiempo = time.time()
    resultado = minimoMonedas(cantidad, monedas)
    fin_tiempo = time.time()
    
    tiempoEjecucion = fin_tiempo - inicio_tiempo
    
    # Imprimir resultados
    if resultado == -1:
        print(f"Para la cantidad {cantidad} con monedas {monedas}, no es posible dar el cambio exacto.")
    else:
        print(f"Para la cantidad {cantidad} con monedas {monedas}, el número mínimo de monedas necesarias es: {resultado}")
    
    # Imprimir el tiempo de ejecución
    print(f"Tiempo de ejecución para el caso de prueba: {tiempoEjecucion:.10f} segundos\n")
