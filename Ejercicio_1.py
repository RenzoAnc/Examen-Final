#Ejercicio:
"""
1. Escribir un programa para el manejo de listas el cuál cumplirá los siguientes
requerimientos:
Reglas:
- Crear una función que le permitirá almacenar 10 número aleatorios.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimir por pantalla.
- Crear una lista para ordenar de mayor a menor la lista que se creará en
ítem 2 (número no repetidos) y otra lista para ordenarlas de menor a
mayor, retornar este valor e mostrar por pantalla.
- Crear una función para indicar cuál es mayor número de la lista (lista del
ítem 2), retornar este valor e imprimirlo por pantalla.

"""

import random

def almacenar_numeros_aleatorios(numero):
    lista = []
    for i in range(1, numero+1):
        lista.append(random.randint(1, numero))  # No especifica el rango de valores. Asumo de 1 al 10.
    print("La lista de numeros aleaorios es: ", lista)
    return lista


lista_numeros_aleatorios = almacenar_numeros_aleatorios(10)

def numeros_no_repetidos(lista2):
    lista3 = []
    for elemento in lista2:
        cantidad = lista2.count(elemento)  # No especifica el rango de valores. Asumo de 1 al 10.
        if cantidad > 1:
            continue
        elif cantidad == 1:
            lista3.append(elemento)
    return lista3


listelenorep = numeros_no_repetidos(lista_numeros_aleatorios)
print('La lista que contiene elementos no repetidos es:', listelenorep)

def menor_a_mayor(lista):
    lista.sort()
    return lista


listanorepordenada = menor_a_mayor(listelenorep)
print('La lista ordenada de menor a mayor es: ', listanorepordenada)


def mayor_a_menor(lista):
    lista.sort()
    lista.reverse()
    return lista


listanorepordenada_2 = mayor_a_menor(listanorepordenada)
print('La lista ordenada de mayor a menor es: ', listanorepordenada_2)

def maximo_valor(lista):
    valor_maximo = max(lista)
    return valor_maximo


Maximo_valor = maximo_valor(listelenorep)
print('El maximo valor es: ', Maximo_valor)