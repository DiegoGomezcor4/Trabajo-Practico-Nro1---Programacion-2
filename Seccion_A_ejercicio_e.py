"""
e. Escribir un procedimiento numeros_par_impar(entrada) que, dada una lisa de 
números, eleve cada elemento impar en ella al cuadrado y los mueva a otra lista 
e imprima ambas. La lista de números la ingresa el usuario en forma de números 
separados por coma. 
Suponiendo que el usuario ingresa la siguiente lista: 
1,2,3,4,5,6,7,8,9 
Entonces, la salida del programa debería ser: 
2,4,6,8 
1,9,25,49,81 
"""

def numeros_par_impar(entrada):
    # transformando la cadena en una lista
    lista_original = []
    
    entrada = entrada. split(',')
    
    for numero in entrada:
        lista_original.append(int(numero))
        
    lista_pares = []
    lista_impares = []
    
    for numero in lista_original:
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero ** 2)
            
    print('Números pares:', lista_pares)
    print('Números impares elevados al cuadrado:', lista_impares)
    
    
entrada = input('Ingrese una lista de numeros separados por coma: ')
numeros_par_impar(entrada)
        