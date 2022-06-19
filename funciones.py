""""
- Crear una función donde se pedirá el tamaño de lista y la cantidad de
números que serán ingresado por consola (los números serán llenados de
manera aleatoria dentro de la lista), esta lista será escrita dentro del file
“notas.txt”
"""
import random
import math


def escribir_archivo_num_al(tamaño,cantidad):
    lista = []
    lista2 = []
    for elemento in range(1,tamaño+1):
        lista.append(random.randint(1, tamaño))
    for i in range(1,cantidad+1):
        valores = input('Ingrese los valores: ')
        lista2.insert(lista[i-1],valores)
    return lista2



"""
- Crear una función donde se usará la librería math para obtener la raíz
cuadrada de los números que han sido llenados en la lista anterior y los
cuales serán escritos en el file “notas.txt”.
"""
def raiz_cuadrada(lista):
    lista2 = []
    for elemento in lista:
        lista2.append(math.sqrt(elemento))
    return lista2


