# Solicita al usuario cuantas filas tendra el triangulo (altura)
n = int(input("Ingresa un numero entero positivo: "))

# Este ciclo controla las filas del triangulo.
# Comienza en n + 1 y va descendiendo hasta 1, reduciendo de uno en uno.
# Esto permite que cada línea tenga un asterisco menos que la anterior.
for i in range(n + 1, 0, -1):

    # Este ciclo controla las columnas (cantidad de asteriscos por fila).
    # Imprime i - 1 asteriscos, logrando el efecto de triangulo invertido.
    for j in range(0, i - 1):
        print("*", end=" ")

    # Despues de imprimir los asteriscos de la fila,
    # se agrega un salto de línea para pasar a la siguiente.
    print()
