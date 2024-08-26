import time

def es_palindromo(cadena, inicio, fin):
    if inicio >= fin:
        return True
    if cadena[inicio] != cadena[fin]:
        return False
    return es_palindromo(cadena, inicio + 1, fin - 1)

def limpiar_cadena(cadena):
    cadena = ''.join(c for c in cadena if c.isalnum())
    return cadena.lower()


palabras = ["radar", "solos", "reconocer", "anilina", "sometemos",
            "python", "computadora", "desarrollador", "inteligencia", "programación"] 


tiempos_ejecucion = []

for palabra in palabras:

    #Validacion
    if(len(palabras) > 10000):
        print("Demasiadas palabras para analizar, prueba bajar la cantidad")
        break
    
    cadena_limpia = limpiar_cadena(palabra)
    
    inicio = time.time()
    resultado = es_palindromo(cadena_limpia, 0, len(cadena_limpia) - 1)
    fin = time.time()
    
    tiempo_ejecucion = fin - inicio
    tiempos_ejecucion.append(tiempo_ejecucion)
    
    if resultado:
        print(f'La cadena "{palabra}" es un palíndromo.')
    else:
        print(f'La cadena "{palabra}" no es un palíndromo.')



#Validacion 
if(len(palabras) == 0):
    print("Sin palabras para analizar")
else:
    tiempo_promedio = sum(tiempos_ejecucion) / len(tiempos_ejecucion)
    print(f"\nTiempo promedio de ejecución: {tiempo_promedio:.10f} segundos")
        
