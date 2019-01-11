# GOMB FELSZIN ES TERFOGAT
# https://www.calculat.org/hu/terfogat-felszin/gomb.html
PI = float(3.14)
r = float(input("Add meg a gömb sugarát!\n"))

#HATVANYOZAS A PYTHON NYELVBEN --> ** <--
#TERFOGAT
Vgomb = float(4/3)*PI*float(r**3)
#FELSZIN
Agomb = float(4*PI)*float(r**2)

print(
    "A gömb felszíne : ",round(Agomb,2),"\n"
    "A gömb térfogata : ",round(Vgomb,2)
)