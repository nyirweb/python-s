# ATM penzvaltas
money = int(input("Add meg mennyi pénzt kérsz?"))

otezresek = int(5000)
ezresek = int(1000)
otszazasok = int(500)
szazasok = int(100)

countOtezer = int(0)
countEzer = int(0)
countOtszaz = int(0)
countSzaz = int(0)

maradek = money

if(maradek >= otezresek):
    maradek = money-otezresek
    countOtezer += 1
    while(maradek >= otezresek):
        maradek = maradek-otezresek
        countOtezer += 1
if(maradek >= ezresek):
   maradek = maradek-ezresek
   countEzer += 1
   while(maradek >= ezresek):
       maradek = maradek - ezresek
       countEzer += 1
if(maradek >= otszazasok):
    maradek = maradek-otszazasok
    countOtszaz += 1
    while(maradek >= otszazasok):
        maradek = maradek - otszazasok
        countOtszaz += 1
if(maradek >= szazasok):
    maradek = maradek-szazasok
    countSzaz += 1
    while(maradek >= szazasok):
        maradek = maradek - szazasok
        countSzaz += 1

print("Kiadott ötezresek: ",countOtezer,
                  "Kiadott Ezresek: ", countEzer,
                  "Kiadott Ötszázasok: ", countOtszaz,
                  "Kiadott Százasok: ", countSzaz,
                  "Bent Maradt: ", maradek)

#Összegző kiiratás
countSubTotal = countOtezer+countEzer+countOtszaz+countSzaz
print(
    money,"Kifizetése: \n",
    countOtezer," X ", otezresek,"\n",
    countEzer," X ", ezresek,"\n",
    countOtszaz," X ", otszazasok,"\n",
    countSzaz," X ", szazasok,"\n",
    "---------------------------------------------------\n",
    "Összes kiadott papírpénz és érme: ",countSubTotal,"\n"
    "Nem kifizethető: ",maradek
)