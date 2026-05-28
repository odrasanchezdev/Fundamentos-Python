# Solicita al usuario la cantidad de filas que tendrá la pirámide
n = int(input("Ingresa un número entero y positivo: "))

# Este ciclo controla las filas de la pirámide.
# Comienza en 1 (una estrella) y aumenta hasta n, formando la estructura de abajo hacia arriba.
for j in range(1, n + 1):

    # " " * (n - j): genera los espacios necesarios para alinear la pirámide a la derecha.
    #                Al principio se imprimen muchos espacios y en cada fila se reduce uno.
    #
    # "* " * j: genera el número de asteriscos que corresponden a esa fila.
    #           La primera fila imprime 1, la segunda 2, y así sucesivamente.
    #
    # Al combinar los espacios y los asteriscos, se forma la pirámide alineada a la derecha.
    print(" " * (n - j) + "* " * j)

    # No es necesario agregar un salto de línea manualmente,
    # ya que print() lo incluye automáticamente al finalizar cada impresión.
