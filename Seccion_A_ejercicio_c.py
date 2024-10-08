"""
c. Escriba un procedimiento procesar_palabras(entrada) que acepte una 
secuencia de palabras separadas por coma, las ordene y las imprima. 
Suponiendo que la entrada provista al programa es la siguiente: 
te,felicito,que,bien,actuas 
La salida esperada es: 
actuas,bien,felicito,que,te
"""

def procesar_palabras(entrada):
    # Dividimos la entrada en palabras usando la coma como delimitador
    palabras = entrada.split(',')
    
    
    # Ordenamos las palabras utilizando el metodo sorted()
    palabras_ordenadas = sorted(palabras)
    
    resultado = ','.join(palabras_ordenadas)
    
    print(resultado)
  
  
# Ejemplo: 

entrada = 'te,felicito,que,bien,actuas'
procesar_palabras(entrada)

entrada2 = 'hola,como,estas,el,dia,de,hoy'
procesar_palabras(entrada2)