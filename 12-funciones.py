def funcion(x):
    return x * 10

y= funcion (5)
print(f"el resultado de la funcion es {y}")

def suma(a, b):
    return a+ b

resultado = suma(2, 3)
print(resultado)

def resta(a, b=5):
    return a - b

resultado1= resta(6)
print(f"resultado numero 1 por defecto: {resultado1}")

resultado2= resta(4, 4)
print(f"resultado numero 2 colocando valor: {resultado2}")

def potencia(base, exponente):
    return base ** exponente

resultado0= potencia(base=3, exponente=3)
print(resultado0)

