# Samuel Madrid Ossa

### Complejidad del algoritmo de verificación de palíndromos usando Recursividad:

El algoritmo, en cada llamada, compara la primera posición con la última posición, lo que indica que la profundidad máxima de la recursión es n/2, donde n es la cantidad de datos. En el peor caso, el algoritmo realiza n/2 llamadas recursivas, así que la complejidad es **O(n)**.

### Complejidad del algoritmo de generación de permutaciones de un conjunto:

La cantidad total de permutaciones de un conjunto de tamaño n es n!. En la primera llamada, el bucle se ejecuta n veces; en la segunda llamada, n-1 veces, y así sucesivamente. Por lo tanto, la complejidad es **O(n!)**.

### Complejidad del algoritmo de cálculo de monedas para cambio mínimo:

En el peor de los casos, se realizan operaciones proporcionales a la cantidad, como cuando las monedas son de la cantidad exacta, por ejemplo, una moneda de 100 para devolver 100. De igual forma, aunque el peor caso no siempre es el que más se demora, se tarda más dependiendo de la cantidad y la variedad de monedas. Por lo tanto, yo este algoritmo lo categorizaría como **O(cantidad × número de monedas)** y no como algo al cuadrado, porque ambas iteraciones dependen de magnitudes distintas.# Parcial01_Practico

# Instrucciones para Ejecutar Mi Implementación

Estas son las instrucciones para construir el proyecto:

1. Clona el repositorio en tu máquina local.
    ```bash
    git clone https://github.com/ssramirezr/assignment1-juan-jose-gomez-samuel-madrid-ossa
    ```

2. Asegúrate de tener Python instalado:

    [Instala la versión más reciente de Python](https://www.python.org/downloads/)

3. Verifica la instalación de Python:

    ```bash
    py --version
    ```

5. Navega desde tu sistema de archivos al repositorio que clonaste y ejecuta nuestro código con el siguiente comando:

    ```bash
    py ejercicio1.py
    ```
    
    ```bash
    py ejercicio2.py
    ```
    
    ```bash
    py ejercicio3.py
    ```



Ortografia y entendimiento ayudado por Chat-GPT