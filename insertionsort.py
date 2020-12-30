import random

def insertionsort(lista):

    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion_actual = i

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

    return lista

if __name__ == "__main__":
    tamano_lista = int(input('Ingresa en tamaño de la lista: '))

    lista = [random.randint(0, 1000) for i in range(tamano_lista)]
    print(lista)

    lista_ordenada= insertionsort(lista)
    print(f'La lista ordenada queda de la siguiente manera: {lista_ordenada}')