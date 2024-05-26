def main():
    # Creo un diccionario de personas con sus respectivas edades
    personas = {'Juan': 20, 'Maria': 25, 'Pedro': 30, 'Ana': 35}

    # Creo un diccionario de personas con sus respectivas edades usando una comprensión de diccionarios
    personas2 = {nombre: edad for nombre, edad in personas.items()}

    # Armo dos listas, una con 10 personas y otra con 10 edades y luego las combino en un diccionario usando una
    # comprensión de diccionarios
    nombres = ['Juan', 'Maria', 'Pedro', 'Ana', 'Luis', 'Laura', 'Carlos', 'Sofia', 'Diego', 'Valeria']
    edades = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
    personas3 = {nombre: edad for nombre, edad in zip(nombres, edades)}

    # Imprimo los diccionarios con separadores para visualizar mejor los resultados
    print("Diccionario de personas original:", personas)
    print("******************************")
    print()
    print("Diccionario de personas usando comprensión de diccionarios:", personas2)
    print("******************************")
    print()
    print("Diccionario de personas usando comprensión de diccionarios y zip:", personas3)
    print("******************************")
    print()


if __name__ == '__main__':
    main()
