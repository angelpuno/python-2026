tramo1= complex(50, 30)
tramo2= complex(40, -10)

lineacomunicacion= tramo1+tramo2

print(f"Impedancia Total = {lineacomunicacion}")
print(f"Resistencia = {lineacomunicacion.real}")
print(f"Reactancia = {lineacomunicacion.imag}")