#Listas 

#primera forma de hacer una lista
lista1 = ["Angel", 32, True, "Angel"]

#segunda forma de hacer una lista
n = list([1,2,3,4,5]) #lista numerica

ramos = []

#metodos para las listas

print(lista1[0])#imprime el primer elemento de una lista

#01-Count()  cuantas veces se repite un elemento en una lista

print(lista1.count("Angel"))

print(ramos)

#agregar un elemento al final de la lista

ramos.append("Quimica")
print(ramos)

ramos.append("Habilidades Comunicativas")
print(ramos)

ramos.append("Programación")
print(ramos)

#otra forma de insertar un elemento a una lista

ramos.insert(0, "introducción a la matematica")
print(ramos)
#modificar un elemento en especifico en una lista

ramos[2] = "Habilidades comunicativas para ingenieros/as"
print(ramos)

#eliminar el ultimo elemento de la lista

ramos.pop()
print(ramos)

#ordenar los elementos de una lista de forma descendente a ascendente
ramos.sort()
print(ramos)

n.sort()
print(n)

#ordenar los elementos de una lista segun la cant. de caracteres de cada elemento
ramos.sort(key=len)
print(ramos)

# extender una lista a partir de otra

ramos_segundo_semestre = ["Ciudadania", "Algebra", "Introducción a la fisica"]
print(ramos_segundo_semestre)

ramos.extend(ramos_segundo_semestre)
print(ramos)