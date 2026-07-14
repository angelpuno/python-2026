productos = ["Pan", "Leche", "Pan", "Queso", "Leche", "Jugo", "Pan"] 
cant_productos= len(productos)
productos_registrados= set(productos)

print("=====REGISTRO=====\n")
print(f"canttidad de productos: {cant_productos}")
print(f"productos distintos:")
for i in productos_registrados:
    print(i)

if "Jugo" in productos_registrados:
    print("el Jugo fue vendido")
else:
    print("el jugo no fue vendido")



