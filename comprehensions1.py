def main():
    # Creo una lista de números del 1 al 10 de forma manual
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Creo una lista de números del 1 al 100 usando un ciclo for tradicional
    numeros2 = []
    for i in range(1, 101):
        numeros2.append(i)

    # Creo una lista de números del 1 al 100 usando una comprensión de listas
    numeros3 = [i for i in range(1, 101)]

    # Creo una lista de los cuadrados de los números del 1 al 10 usando una comprensión de listas
    cuadrados = [i ** 2 for i in range(1, 11)]

    # Creo una lista de los cuadrados primos de los números del 1 al 100 usando un for tradicional
    cuadrados_primos = []
    for i in range(1, 101):
        if es_primo(i):
            cuadrados_primos.append(i ** 2)

    # Creo una lista de los cuadrados primos de los números del 1 al 100 usando solo una comprensión de listas
    cuadrados_primos2 = [i ** 2 for i in range(1, 101) if es_primo(i)]

    # Imprimo las listas con separadores para visualizar mejor los resultados
    print("Lista de números del 1 al 10:", numeros)
    print("******************************")
    print()
    print("Lista de números del 1 al 100 (for tradicional):", numeros2)
    print("******************************")
    print()
    print("Lista de números del 1 al 100 (comprensión de listas):", numeros3)
    print("******************************")
    print()
    print("Lista de cuadrados de los números del 1 al 10:", cuadrados)
    print("******************************")
    print()
    print("Lista de cuadrados primos de los números del 1 al 100 (for tradicional):", cuadrados_primos)
    print("******************************")
    print()
    print("Lista de cuadrados primos de los números del 1 al 100 (solo comprensión de listas):", cuadrados_primos2)
    print("******************************")
    print()


def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()
