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
    # Encontrar elementos comunes
    elementos_comunes = []
    for elemento in lista1:
        if elemento in lista2:
            elementos_comunes.append(elemento)
    
    # Ordenar los elementos comunes enorden inverso
    elementos_comunes.sort(reverse=True)
    
    # Encontrar elementos no cumunes
    elementos_no_comunes = []
    for elemento in lista1:
        if elemento not in lista2:
            elementos_no_comunes.append(elemento)
    for elemento in lista2:
        if elemento not in lista1:
            elementos_no_comunes.append(elemento)
            
    # Ordenar elementos no comunes alfabéticamente
    elementos_no_comunes.sort()
    
    print(elementos_comunes)
    print(elementos_no_comunes)


# Ejemplo
    
listas_diferencia(['b', 'a', 'c'], ['e','b','d','c'])