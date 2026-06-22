#Angel Damian Stefan Punoñanco Soto
#Matias Esteban Villacura Figueroa

num= 500
num2=456
total = 0

while num <= 800:
    print(num)
    total += num
    if num == 800:
        print(f"El resultado es: {total}")
        break
    print("+")
    print(num2)
    total += num2
    print("+")
    num += 10
    num2 -= 2
