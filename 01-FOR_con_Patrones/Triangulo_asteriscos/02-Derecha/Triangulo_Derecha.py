# Pide al usuario cuántas filas (altura) tendrá el triángulo
n = int(input("Ingresa un numero entero y positivo: "))

# Recorre las filas del triángulo desde 1 hasta n
for j in range(1, n + 1):
    print(" " * (n - j) + "*" * j)
    # " " * (n - j): genera los espacios necesarios para empujar los asteriscos hacia la derecha.
    #                Al inicio hay muchos espacios, y cada fila tiene uno menos.
    #
    # "*" * j: genera los asteriscos de la fila. La primera fila tiene 1, la segunda 2, etc.
    #
    # Al concatenar 'espacios + asteriscos', la figura queda alineada a la derecha.
    

    # A diferencia del triangulo cargado a la izquierda, en este podemos omitir el salto de linea
    # Cada vez que print() termina de imprimir su contenido, agrega ese salto de línea.
