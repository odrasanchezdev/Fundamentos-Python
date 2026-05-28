# Solicita al usuario la cantidad de filas que tendrá el triangulo
n = int(input("Ingrese un numero positivo y entero: "))

# Recorre desde n hasta 1, reduciendo en cada iteración.
# Esto genera un triángulo invertido: primero muchos asteriscos, luego menos.
for j in range(n, 0, -1):
    print(" " * (n-j) + "* " * j)
    # "  " * (n - j):
    #   - Calcula cuántos espacios van antes de los asteriscos.
    #   - Mientras j disminuye, (n - j) aumenta.

    # "* " * j:
    #   - Genera j asteriscos separados por un espacio.
    #   - Cuando j es grande, se imprimen más asteriscos; cuando disminuye, menos.

 # Se imprime la fila completa (espacios + asteriscos)