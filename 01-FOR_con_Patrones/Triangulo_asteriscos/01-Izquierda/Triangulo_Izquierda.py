# Pide al usuario cuantas filas (altura) tendra el triangulo
n = int(input("Ingresa un numero entero y positivo: "))

# Recorre las filas del triangulo desde 0 hasta n-1
for i in range(0, n):
    # En cada fila se imprime i+1 asteriscos, donde i es el numero de fila (empezando en 0)
    for j in range(0, i + 1):
        # end=' ' -> indica que despues de cada asterisco se imprime un espacio en lugar de un salto de línea.
        print("*", end=' ')
    
    # Despues de terminar la fila, hace un salto de línea.
    print("\r")
