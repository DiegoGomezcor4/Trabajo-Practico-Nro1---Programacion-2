"""
c. Tal como sucede con la lógica proposicional, en Python muchas veces las 
expresiones booleanas pueden ser simplificadas manteniendo el valor de 
verdad de la expresión. Así, por ejemplo, (a and b) or (b and a) es equivalente 
a a and b. A continuación, intente simplificar las siguientes expresiones y 
escriba un procedimiento procesar_sentencias(a, b, c) que permita evaluar el 
valor de verdad de las expresiones ya simplificadas: 
 
i. (a or b) or (b and c) 
 
ii. b and c or False 
 
iii. a and b or c or (b and a) 
 
iv. a == True or b == False 
"""

def procesar_sentencias (a, b, c):
    # Expresión i simplificada
    expresion1 = a or b
    print(f'Resultado de la expresión i: {expresion1}')
    
    # Expresión ii simplificada
    expresion2 = b and c
    print(f'Resultado de la expresión ii: {expresion2}')
    
    # Expresión iii simplificada
    expresion3 = (a and b) or c
    print(f'Resultado de la expresión iii: {expresion3}')
    
    # Expresión iv simplificada
    expresion4 = a or not b
    print(f'Resultado de la expresión iv: {expresion4}')
    
    
def probar_expresiones_originales(a, b, c):
    # Expresión i original
    expr1 = (a or b) or (b and c)
    print(f"Resultado de la expresión i original: {(a or b) or (b and c)}")
    
    # Expresión ii original
    expr2 = b and c or False
    print(f"Resultado de la expresión ii original: {b and c or False}")
    
    # Expresión iii original
    expr3 = a and b or c or (b and a)
    print(f"Resultado de la expresión iii original: {a and b or c or (b and a)}")
    
    # Expresión iv original
    expr4 = a == True or b == False
    print(f"Resultado de la expresión iv original: {a == True or b == False}")
    
# Ejemplo

a = True
b = False
c = True

procesar_sentencias(a, b, c)

probar_expresiones_originales(a, b, c)