"""
a. Escribir una función suma(numero) que resuelva la siguiente suma, asumiendo 
que numero = 10: 
 
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 
 
En el programa que invoque dicha función: 
i. El usuario debe poder ingresar el valor del parámetro numero. 
ii. Debe validarse que el dato ingresado por el usuario corresponda a 
un dígito, y no a otro tipo de dato como un carácter. 
iii. El  cálculo  debe  realizarse  utilizando  algún  tipo  de  bucle  (ej:  for, 
while). 
BONUS: Luego, codificar una función equivalente que utilice recursividad. 
"""

def suma(numero):
    total = 0
    for i in range(1, numero + 1):
        total += i
    return total

def suma_recursiva(numero):
    if numero == 1:
        return 1
    else:
        return numero + suma_recursiva(numero - 1)
    

def main():
    while True:
        try:
            numero = int(input('Por favor Ingrese un numero entero positivo: '))
            if numero > 0:
                break
            else:
                print('Por favor, ingrese un número mayor que cero')
        except ValueError:
            print('Entrada no válida. Por favor ingrese un numero entero. ')

    resultado = suma(numero)
    print(f'La suma es {resultado}')

    resultado_recursivo = suma_recursiva(numero)
    print(f'La suma recusiva es: {resultado_recursivo}')


if __name__ == '__main__':
    main()