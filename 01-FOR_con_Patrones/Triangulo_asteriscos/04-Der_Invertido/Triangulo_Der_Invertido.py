# Solicita al usuario un número para definir la altura del triángulo
n = int(input("Ingresa un número entero y positivo: "))

# Recorre desde n hasta 1, reduciendo en cada iteración.
# Esto genera un triángulo invertido: primero muchos asteriscos, luego menos.
for j in range(n, 0, -1):

    print("  " * (n - j) + "* " * j)
    # "  " * (n - j):
    # El elemento cuenta con doble espacio, para marcar el empuje
    #   - Calcula cuántos espacios van antes de los asteriscos.
    #   - Mientras j disminuye, (n - j) aumenta.
    #   - Esto empuja la figura hacia la derecha.

    # "* " * j:
    #   - Genera j asteriscos separados por un espacio.
    #   - Cuando j es grande, se imprimen más asteriscos; cuando disminuye, menos.

 # Se imprime la fila completa (espacios + asteriscos)