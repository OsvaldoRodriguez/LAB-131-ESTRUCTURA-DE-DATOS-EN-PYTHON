def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sumando_primos(vector, indice):
    if indice < 0:
        return 0

    elemento = vector[indice]
    if es_primo(elemento):
        return elemento + sumando_primos(vector, indice - 1)
    else:
        return sumando_primos(vector, indice - 1)

vector = [10, 7, 3, 8, 11, 4, 6, 5]
result = sumando_primos(vector, len(vector) - 1)
print("Suma de elementos primos:", result)
