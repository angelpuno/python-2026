#Angel Damian Stefan Punonanco Soto
#Matias Esteban Villacura Figueroa

conceptos_clave=["Inmutable", "Iterable", "Inmutable", "Hashable", "interpretado", "Iterable"]
setc= set(conceptos_clave)
conceptos_clave= list(setc)
conceptos_clave= sorted(conceptos_clave)
print(conceptos_clave)
glosario= {
    f"{conceptos_clave[0]}":"Objeto cuyo valor hash nunca cambia y puede ser clave.",
    f"{conceptos_clave[1]}":"Objeto con un valor fijo que no se puede modificar.",
    f"{conceptos_clave[2]}":"Lenguaje donde el código se ejecuta línea a línea.",
    f"{conceptos_clave[3]}":"Objeto capaz de devolver sus elementos uno a la vez."
}

palabra= input(f"ingrese el concepto a buscar: ")
print(glosario[f"{palabra}"])
registro_tupla= tuple(glosario.items())
print(registro_tupla)