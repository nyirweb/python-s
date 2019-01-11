# Hasáb felszín és térfogat számítása
# https://www.calculat.org/hu/terfogat-felszin/teglatest.html
a = float(input("Add meg a TÉGLATEST 'a' élét\n"))
b = float(input("Add meg a TÉGLATEST 'b' élét\n"))
c = float(input("Add meg a TÉGLATEST 'c' élét\n"))

V = float(a*b*c)
A = float(2*(a*b+a*c+b*c))

print("A hasáb felszíne: ",round(A,2))
print("A hasáb térfogata: ",round(V,2))
