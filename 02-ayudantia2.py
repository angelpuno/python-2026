notas = {
    "Ana": 6.2,
    "Luis": 4.8,
    "Pedro": 3.9,
    "Sofía": 5.5
} 
for i in notas:
    print(f"Nombre: {i} - nota: {notas[i]}")
print("")
aprobados= 0

for i,nota in notas.items():
    if nota >= 4:
        aprobados+= 1
        print(f"{i} esta aprobado")
    else:
        print(f"{i} esta reprobado")
print("")
print(f"cantidad total de aprobados: {aprobados}")
