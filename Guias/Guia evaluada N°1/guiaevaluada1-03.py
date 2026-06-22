from colorama import init, Fore
init()

#Angel Damian Stefan Punoñanco Soto
#Matias Esteban Villacura Figueroa

sueldo_base = 529000

vendedores = {
    "Matias": [120000, 150000, 200000, 180000, 160000],
    "angel": [300000, 250000, 200000, 180000, 170000],
    "jordan": [400000, 350000, 300000, 250000, 280000]
}

for nombre, ventas in vendedores.items():

    total_ventas = sum(ventas)
    promedio = total_ventas / len(ventas)

    if total_ventas >= 1500000:
        bono = sueldo_base * 0.20
    else:
        if total_ventas >= 1000000:
            bono = sueldo_base * 0.10
        else:
            if total_ventas >= 500000:
                bono = sueldo_base * 0.05
            else:
                bono = 0

    sueldo_total = sueldo_base + bono

    print(Fore.LIGHTCYAN_EX + "=================")
    print("Vendedor:", nombre)
    print("Ventas diarias:", ventas)
    print("Total ventas semanales: $", total_ventas)
    print("Promedio semanal: $", promedio)
    print("Bono: $", bono)
    print("Sueldo total a pagar: $", sueldo_total)