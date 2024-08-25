"""
a. Escribir una función de nombre palabra_no_tiene_letras(palabra,
letras_prohibidas), la cual retorne True si es que los caracteres que componen
una palabra no se encuentran en una lista de caracteres prohibidos.
"""

def palabra_no_tiene_letras(palabra, letras_prohibidas):
    # Verificamos cada carácter en la palabra
    for letra in palabra:
        if letra in letras_prohibidas:  
            return False
    return True


# Ejemplo

# prueba 1
palabra = 'hola'
letras_prohibidas = ['a', 'e','i','o','u']

resultado = palabra_no_tiene_letras(palabra,letras_prohibidas)
print(resultado)

# prueba 2
palabra2 = 'pmns'
print(palabra_no_tiene_letras(palabra2, letras_prohibidas))
