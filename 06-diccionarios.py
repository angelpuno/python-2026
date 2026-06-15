#DICCIONARIOS


#primera forma de declarar un diccionario
paciente= {
    "nombre":"Benjamin Bahamonde",
    "edad":18,
    "ciudad":"Ancud",
    "fechas_atencion": [5,8,12],
    "diagnostico": "refrío común",
    "informacion_extra": {      #creacion de sub diccionario
        "tipo de sangre": "A+",
        "hemograma": False
    }
}

print(type(paciente))
print(f"===ficha paciente=== \n\n{paciente}")

#segunda forma de declarar un diccionario
medico= dict(
    nombre= "Ignacio Saez",
    edad= "19",
    especialidad= "Cardiologo"
)

print(f"======Ficha Medico====== \n\n{medico}")

#Consulta de informacion de diccionario

#consulta el valor de la clave paciente (consultando solo un campo)
print(f"nombre del paciente: {paciente["nombre"]}")

#a diferencia de los corchetes [], este metodo no genera error si no existe la clave
#metodo get() obtiene el valor de una clave, si no existe retorna none
print(f"Rut del paciente: {paciente.get("rut", "N/D (No Data)")}")


print(f"Nombre del medico: {medico.get("nombre")}")

#Retornar las claves, los valores a ambos como pares
print(f"\n{paciente.keys()}") #solo claves

print(f"\n {paciente.values()}")#solo Valores

print(paciente.items()) #genera una lista de tuplas ([(Clave-Valores)], [(Clave-Valores)]...)

#retonar el numero de claves que tiene el diccionario (igual que las listas)
print(len(medico)) #cuenta la cantidad de par clave-valor (3)

print(len(paciente))# (6)

#Modificació del diccionario
#Agregar una clave nueva
paciente["telefono"]= "+56936361020"
print(f"\n======FICHA PACIENTE CON TELEFONO====== \n\n{paciente}")

#sobreescribir valor de una clave (Forma n°1)
paciente["edad"]= 20
paciente["telefono"]= "+56936361020"
print(f"\n======FICHA PACIENTE CON EDAD ACTUALIZADA====== \n\n{paciente}")

#Fusiona otro diccionario (o pares clave-valor) en el actual
#Util para actualizar varios campos a la vez (actualizar varias claves)
paciente.update({"edad": 21, "ciudad": "Castro"})
print(paciente["edad"])
print(paciente["ciudad"])

#Eliminar una clave sin retorno
del(paciente["informacion_extra"])
print(paciente)

#Eliminar una clave y retornar su valor (adiferencia de del, que no retorna)
edad_eliminada= paciente.pop("edad")
print(f"edad eliminada: {edad_eliminada}")
print(paciente)

#Otras utilidades del diccionario

#Con in se verifica si una clave existe en el diccionario sin utilizar condicionales "todavia"
print("nombre" in paciente)
print("rut" in paciente)

#Con copy() re crea una copia independiente del diccionario
paciente2= paciente.copy()
paciente2["nombre"]= "Javiera"
print(paciente["nombre"])
print(paciente2["nombre"])
print(paciente2)

#Con clear() elimina todos los elementos del diccionario, dejandolo vacio (a diferencia del del() )

medico2= medico.copy()
print(f"\n======DICCIONARIO COPIA (MEDICO2)====== \n\n{medico2}")
medico2.clear()
print(medico2)

n= [1, 2, 3, 4, 5]
n_str= list(map(str,n))
print(f"Lista de números como strings: {", ".join(n_str)}")

#Métodos para Datos Iterables
a= [1,2,3,4,5]
b= ["A","B","C","D"]
comprimir= list(zip(a,b))
print(comprimir)