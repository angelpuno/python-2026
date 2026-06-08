colores_primarios= {"Azul", "Rojo", "Amarillo"}
colores_secundarios= set({"Naranja", "Verde", "Violeta"})

print(type(colores_primarios))

print(f"conjunto 1: {colores_primarios}")
print(f"conjunto 2: {colores_secundarios}")

colores_nuevos= {"Azul", "Rojo", "Celeste", "Azul", "Rojo"}
print(f"conjunto 3: {colores_nuevos}")

#agregando un nuevo elemento al set colores_nuevos add()
colores_nuevos.add("Cafe")
print(f"conjunto 3 actualizado: {colores_nuevos}")

#eliminando un elemento del set colores_nuevos discard()
colores_nuevos.discard("Cafe")
print(f"conjunto 3 actualizado sin el color cafe: {colores_nuevos}")

#Aplicando el metodo intersection()
interseccion= colores_primarios.intersection(colores_nuevos)
print(interseccion)