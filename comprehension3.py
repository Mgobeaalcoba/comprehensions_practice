def main():
    # Example of set comprehension
    # Creo un conjunto de números pares del 1 al 10 usando una comprensión de conjuntos
    pares = {i for i in range(1, 11) if i % 2 == 0}

    # Imprimo el conjunto de números pares
    print("Conjunto de números pares del 1 al 10:", pares)

    # Creo un conjunto de los cuadrados de los números del 1 al 10 usando una comprensión de conjuntos
    cuadrados = {i ** 2 for i in range(1, 11)}

    # Imprimo el conjunto de los cuadrados de los números del 1 al 10
    print("Conjunto de los cuadrados de los números del 1 al 10:", cuadrados)

    # Los sets no tienen orden, por lo que no se puede acceder a sus elementos por índice y se imprimen de forma
    # desordenada


if __name__ == '__main__':
    main()
