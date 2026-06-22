#Angel Damian Stefan Punoñanco Soto
#Matias Esteban Villacura Figueroa

s= 0
m= 0
h= 0

while s< 60:
    s+= 1
    if s== 60:
        s= 0
        m+= 1
        if m== 60:
            m= 0
            h+= 1
            if h==24:
                h= 0
                break
    print(f"{h:02d}:{m:02d}:{s:02d} horas")