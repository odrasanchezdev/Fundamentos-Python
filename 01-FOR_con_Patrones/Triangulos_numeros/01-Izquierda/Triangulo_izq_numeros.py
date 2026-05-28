# Pide al usuario la cantidad de filas y columnas a imprimir
n = 6

# Recorre la cantidad de filas de tu piramide. Se añade un "+1" porque el valor final se detiene antes del número indicado
for i in range(1, n + 1):
  # Recorre la cantidad de numeros en cada columna 
  for j in range (1, i + 1):
    # Imprime las columnas con un salto de linea
    print (j, end = ' ')
  print (' ')