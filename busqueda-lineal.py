import random

def busqueda_lineal(lista, objetivo, contador_lineal=0):
    match = False

    for elemento in lista:
        contador_lineal += 1
        if elemento == objetivo:
            match = True
            break
    return (match, contador_lineal)

if __name__ == '__main__':
    tamano_lista = int(input("De que tamaño sera la lista ?"))
    objetivo = int(input('Que numero quieres encontrar'))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    (encontrado, contador_lineal) = busqueda_lineal(lista, objetivo)

    print(lista)
    print(f'El elemento: {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Iteraciones en busqueda lineal: {contador_lineal}')