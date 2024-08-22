"""
b. Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y 
cuando las letras que componen dicha palabra estén en orden alfabético, y False 
en caso contrario.
"""

def es_abc(palabra):
    # Convertimos la plaba en minúsculas
    palabra = palabra.lower()
    
    # Iteracion sobre los caracteres
    for i in range(len(palabra) - 1):
        # Comparamos el carácter actual con el siguiente
        if palabra[i] > palabra[i + 1]:
            return False
        
    return True

# Ejemplos:

print(es_abc('abc'))   #true
print(es_abc('aegk'))  #true
print(es_abc('hello')) #false
print(es_abc('HOLA'))  #false
print(es_abc('zxya'))  #false