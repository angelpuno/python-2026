#Operadores en python
a= 10
b= 5
c= 4
d= 10

print("=== OPERADORES ARITMETICOS ===\n")
print(f"la suma entre la variable a y b es: {a + b}")
print(f"la resta entre la variable a y b es: {a - b}")
print(f"la multiplicacion entre la variable a y b es: {a * b}")
print(f"la division entre la variable a y b es: {a / b}")
print(f"el modulo entre la variable a y b es: {a % b}")
print(f"el coeficiente entre la variable b y c es: {b // c}")
print(f"el resultado de la potencia de b elevado a c (5^4)es : {b ** c}")

#se puede hacer esta operacion?
print("Hola"* (int((10*2)/5)), "\n")
print("=== OPERADORES DE COMPARACION ===")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(c >= d)
print(c <= d)

print("=== OPERADORES LOGICOS ===")

bencina = False
encendido = True
#edad = 19

#if = si
#else = sino
#Utilizando el operador AND
if bencina and encendido:
    print("el vehiculo puede arrancar")
else: print("El vehiculo no puede arrancar")