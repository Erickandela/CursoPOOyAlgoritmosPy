import random

def busqueda_binaria(lista, comienzo, final, objetivo, contador_binario=0):
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]}')
    contador_binario += 1
    if comienzo > final:
        return (False, contador_binario)
    medio = (comienzo + final) // 2
    if lista[medio] == objetivo:
        return (True,contador_binario)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, contador_binario)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, contador_binario)

if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño sera la lista ? '))
    objetivo = int(input('Que numero quieres encontrar: '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])

    (encontrado, contador_binario) = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento: {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Iteraciones busqueda binaria: {contador_binario}')