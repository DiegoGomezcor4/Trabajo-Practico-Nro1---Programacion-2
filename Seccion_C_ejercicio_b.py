"""
b. Escribir  un  programa  que  resuelva  la  secuencia  de  Fibonacci  a  pedido  del 
usuario. Deberá codificar una función fibonacci(numero), cuyo parámetro 
numero debe ser ingresado por el usuario y su tipo, al igual que en el ejercicio 
anterior,  validado.  La  función  debe  encargarse  de  calcular  la  secuencia  para 
dicho  número.  A  continuación,  una  descripción  matemática  de  la  famosa 
secuencia:
"""

def fibonacci(numero):
    # Validar que el número sea un entero positivo
    if not isinstance(numero, int) or numero < 0:
        return "Error: Debe ingresar un número entero positivo."
    
    # Caso especial para cuando el número es 0 o 1
    if numero == 0:
        return [0]
    elif numero == 1:
        return [0,1]
    
    # Calcular la secuencia de Fibonacci
    secuencia = [0, 1]
    for i in range(2, numero + 1):
        secuencia.append(secuencia[i - 1] + secuencia[i - 2])

    return secuencia

# Solicitar al usuario ingresar un número
numero = input("Ingrese un número entero positivo: ")

# Validar que la entrada sea un número entero

try:
    numero = int(numero)
    print(fibonacci(numero))
except ValueError:
    print("Error: Debe ingresar un número entero válido.")