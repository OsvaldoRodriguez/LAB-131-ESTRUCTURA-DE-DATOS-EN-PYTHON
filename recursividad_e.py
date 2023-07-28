def intercambiar_diagonales(matriz, fila=0):
    n = len(matriz)

    if fila == n:
        return

    temp = matriz[fila][fila]
    matriz[fila][fila] = matriz[fila][n - 1 - fila]
    matriz[fila][n - 1 - fila] = temp

    intercambiar_diagonales(matriz, fila + 1)

matriz_cuadrada = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
for fila in matriz_cuadrada:
    print(fila)

intercambiar_diagonales(matriz_cuadrada)

print("\nMatriz con diagonales intercambiadas:")
for fila in matriz_cuadrada:
    print(fila)
