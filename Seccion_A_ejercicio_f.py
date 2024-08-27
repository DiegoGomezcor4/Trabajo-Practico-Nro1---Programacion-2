"""
f. Un  portal  web  requiere  un  formulario  de  alta  de  usuario  donde  se  ingrese, 
mínimamente, un usuario y su correspondiente contraseña. Escriba, en Python, 
una  función  contrasena_valida(contrasena)  que  devuelva  True  en  caso  de 
superar  las  siguientes  validaciones  sobre  la  contraseña  proporcionada  por  el 
usuario: 
i. Longitud entre 6 y 20 caracteres. 
ii. Debe contener al menos un número. 
iii. Debe contener al menos dos mayúsculas. 
iv. Debe contener al menos un carácter especial. 
v. No puede contener espacios. 
 
La salida esperada es la siguiente: 
abc.123 es válida:      False 
Abc.123 es válida:      False 
AbC.123 es válida:      True 
AbC.1 23 es válida:     False 
ÁbC.123 es válida:      False 
"""

import re

def contrasena_valida(contrasena):
    # Verifica que la longitud esté entre 6 y 20 caracteres
    if not (6 <= len(contrasena) <= 20):
        return False
    
    # Verifica que no contenga espacion
    if ' ' in contrasena:
        return False
    
    # Verifica que contenga al menos un número
    if not re.search(r'\d', contrasena):
        return False
    
    # Verificar que contenga al menos dos letras mayúsculas
    if len(re.findall(r'[A-Z]', contrasena)) < 2:
        return False
    
    # Verificar que contenga al menos un caracter especial
    if not re.search(r'[$&+,:;=?@#|<>.^*()%!-]', contrasena):
        return False
    
    # si cumple con todas las condiciones
    return True
    
# Pruebas

contrasenas = ['abc.123', 'Abc.123', 'AbC.123', 'AbC.1 23', 'ÁbC.123']

for contrasena in contrasenas:
    print(f'{contrasena} es valida: {contrasena_valida(contrasena)}')