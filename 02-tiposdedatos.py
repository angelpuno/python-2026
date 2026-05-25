#Dato Numericos

#Numeros Enteros
edad = 18
año = 2008

#Numeros Flotantes (reales)
estatura = 1.70
peso = 63.3

#Numeros Complejos
# j = i (imaginario)
numero_complejo = 1 + 4j
#función complex 
otro_numero_complejo = complex(4, 3)

print(numero_complejo)
print(otro_numero_complejo)

#operaciones basicas

base = 8
altura = 12.5
PI= 3.14159

area = (base * altura) / 2

print(f"El area del triangulo es: {area} cm")

#formato  de salida de numeros(numeros imprimidos en terminal)
print(f"el numero PI tiene un valor de {PI: .4f}")

#metodo de redondeo
print(round(area))
print(f"el area del trinagulo es de {round(area)} cm")

#Transformaciones
print(float(edad)) #Transforma el numero entero a flotante


#Cadenas de texto

carrera= "Ingenieria en Informatica"
institucion= "Universidad de los Lagos"

print(carrera[0:11]) #Imprime los caracteres desde el indice 0 hasta el 10 (0 es el primer caracter, 11 no se incluye)

print(institucion[0])#caracter

print(carrera.split)

print("hola " * 4)

#metodo Len() permite contar caracteres de una cadena de texto (incluye espacios)
print(len(institucion)) #Imprime la cantidad de caracteres que tiene la variable institucion





#arreglos (listas)

print("-------Arreglos (Listas)-------")

colores = ["rojo", "verde", "azul", "amarillo"] #arreglo de palabras (stings)

numeros = [1, 2, 3, 4, 5, 6] #arreglo de numeros enteros

lista_mixta = [1, "amarillo", 3.14, True] #arreglo de multiples tipos de datos

print(colores[0]) #Imprime el color en el indice 0 del arreglo colores

print(numeros[-1]) #Imprime el ultimo numero del arreglo numeros

print(lista_mixta)

#Booleanos(Logicos)
luz_electrica = True
interruptor = False

print(luz_electrica)
print(interruptor)

print(f"El tipo de dato es {type(numero_complejo)}")#type dice que tipo de dato es una variable

#Evaluando datos booleanos
print("-------evaluando datos booleanos-------")
print(bool(1))
print(bool(0))
print(bool(""))
print(type(bool("True")))
print(bool(4000))

#evaluando numeros con operadores de comparación
print(100 > 50)

print(10 == 10)

print(20 < 0)