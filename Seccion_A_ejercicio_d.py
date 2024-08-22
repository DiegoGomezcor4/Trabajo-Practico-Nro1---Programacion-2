"""
d. Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2) 
que tome ambas como parámetros e imprima dos listas, cada una con: 
i. Los elementos en común, en orden inverso. 
ii. Los elementos no comunes, en orden alfabético. 
El programa debería arrojar el siguiente resultado: 
listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c']) 
['c', 'b'] 
['a', 'e', 'd']
"""

def listas_diferencia(lista1, lista2):
    # Convertir las listas a conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    # Encontrar elementos comunes
    elementos_comunes = list(conjunto1.intersection(conjunto2))
    
    # Ordenar los elementos comunes en orden inverso
    elementos_comunes.sort(reverse=True)

    # Encontrar elementos no comunes
    elementos_no_comunes = list(conjunto1.symmetric_difference(conjunto2))

    # Ordenar los elementos no comunes alfabéticamente
    elementos_no_comunes.sort()
    
    # Imprimir
    print(elementos_comunes)
    print(elementos_no_comunes)
    
    # Ejemplo
    
listas_diferencia(['i', 'a', 'c','e'], ['z','e','b','d','c'])