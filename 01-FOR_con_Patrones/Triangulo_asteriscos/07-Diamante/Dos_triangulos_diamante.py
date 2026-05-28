# Definimos la altura máxima del rombo (la mitad superior tendrá 5 filas)
rows = 5

# ==========================================
# PARTE SUPERIOR (El triángulo que crece)
# ==========================================
# range(1, 6) genera los números: 1, 2, 3, 4, 5
for j in range(1, rows + 1):
    # 1. (rows - j) calcula los espacios en blanco necesarios a la izquierda.
    # 2. "* " * j imprime el asterisco seguido de un espacio la cantidad de veces que diga j.
    # 3. El signo "+" concatena (une) los espacios con los asteriscos en una sola línea.
    print(" " * (rows - j) + "* " * j)


# ==========================================
# PARTE INFERIOR (El triángulo que decrece)
# ==========================================
# range(4, 0, -1) empieza en 4 (rows - 1), disminuye de -1 en -1 y se detiene ANTES del 0.
# Genera los números: 4, 3, 2, 1
for j in range(rows - 1, 0, -1):
    # Aplica la misma fórmula, pero como 'j' va disminuyendo:
    # - Los espacios (rows - j) van aumentando.
    # - Los asteriscos ("* " * j) van disminuyendo.
    print(" " * (rows - j) + "* " * j)