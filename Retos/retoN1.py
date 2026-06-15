#reto de laboratorio numero 1
notas_lab= []

laboratorio1= float(input("Ingrese la nota del laboratorio 1: "))
laboratorio2= float(input("Ingrese la nota del laboratorio 2: "))
laboratorio3= float(input("Ingrese la nota del laboratorio 3: "))

notas_lab.append(laboratorio1)
notas_lab.append(laboratorio2)
notas_lab.append(laboratorio3)

promedio_lab= (notas_lab[0]*0.4 + notas_lab[1]*0.4 + notas_lab[2]*0.2)

print(f"\n------REPORTE------\n")

print(f"Notas:\n")

print(f"Laboratorio 1: {laboratorio1}")
print(f"Laboratorio 2: {laboratorio2}")
print(f"Laboratorio 3: {laboratorio3}\n")

print(f"Promedio Ponderado Final: {round(promedio_lab,2)}\n")