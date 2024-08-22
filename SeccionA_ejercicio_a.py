"""
a. Escribir una función de nombre palabra_no_tiene_letras(palabra,
letras_prohibidas), la cual retorne True si es que los caracteres que componen
una palabra no se encuentran en una lista de caracteres prohibidos.
"""

def palabra_no_tiene_letras(palabra, letras_prohibidas):
    # Convertimos la lista letras prohibidas en un conjunto para hacer la busqueda mas eficiente
    letras_prohibidas_set = set(letras_prohibidas)
    
    # Verificamos cada carácter en la palabra
    for letra in palabra:
        if letras_prohibidas_set:
            return False
    
    return True


# Ejemplo
 
palabra = 'hola'
letras_prohibidas = ['a', 'e','i','o','u']

resultado = palabra_no_tiene_letras(palabra,letras_prohibidas)
print(resultado)
