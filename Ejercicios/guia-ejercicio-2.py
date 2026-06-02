rut_original = input(f"ingrese su numero de cedula:")

rut=rut_original.strip()

rut= rut.replace(".", "")

print(f"hay {len(rut)} caracteres")
print(rut)