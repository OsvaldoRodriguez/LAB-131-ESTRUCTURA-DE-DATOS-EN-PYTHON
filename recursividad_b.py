def eliminar_digitos_pares(numero):
    if numero == 0:
        return 0
    ultimo_digito = numero % 10
    numero_sin_ultimo_digito = eliminar_digitos_pares(numero // 10)

    if ultimo_digito % 2 == 0:
        return numero_sin_ultimo_digito
    else:
        return numero_sin_ultimo_digito * 10 + ultimo_digito

numero = 3578462
resultado = eliminar_digitos_pares(numero)
print("Número original:", numero)
print("Número sin dígitos pares:", resultado)
