mañana = float(input(f"ingresa el valor de la mañana "))
mediodia = float(input(f"ingresa el valor del mediodia "))
tarde = float(input(f"ingresa el valor de la tarde "))
noche = float(input(f"ingresa el valor de la noche "))

listagb=[mañana, mediodia, tarde, noche]

mañana = listagb[0]
mediodia = listagb[1]
tarde = listagb[2]
noche = listagb[3]

print(f"mañana = {listagb[0]} GB")
print(f"mediodia = {listagb[1]} GB")
print(f"tarde = {listagb[2]} GB")
print(f"noche = {listagb[3]} GB")

promedio= sum(listagb)/len(listagb)
print(f"el promedio de consumo de GB en el dia es: {promedio} GB")

print(f"la diferencia entre el mayor y el menor valor es: {max(listagb)-min(listagb)} GB")