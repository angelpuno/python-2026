# Definicon de Variables
nombre = "Angel"
apellido = "Punonanco"
edad = 18
#Lo que se ve en la salida


#Forma 1: Clásica separando variables y texto por comas
print("Mi nombre es", nombre, ", mi apellido es", apellido, "y mi edad es de" , edad, "años")

#Forma 2: Utilizando f-strings
print(f"Mi nombre es {nombre}, mi apellido es {apellido} y mi edad es de {edad} años")

#Forma 3: Concatenacion (utilizando el operardor +)
#str transformar texto en valor (cadena de texto)
print("Mi nombre es " + nombre + " y mi apellido es " + apellido + " y mi edad es de " + str(edad) + "años")

#Utilizando el método input y creando una variable creando una carrera
carrera = input("¿Que carrera estudias?")
print(f"Yo estudio la carrera de: {carrera}")