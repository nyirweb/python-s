# A piacon burgonya, hagyma, padlizsan kiszamolo

# ÁR/KG
onion = float(149)
# ÁR/KG
potato = float(229)
# ÁR/KG
eggplant = float(79)

onionPieces = float(input("Mennyi hagymát szeretnél? (Kg-ban add meg)\n"))
potatoPieces = float(input("Mennyi burgonyát szeretnél? (Kg-ban add meg)\n"))
eggplantPieces = float(input("Mennyi padlizsánt szeretnél? (Kg-ban add meg)\n"))

onionSubTotal = onionPieces*onion
potatoSubTotal = potatoPieces*potato
eggplantSubTotal = eggplantPieces*eggplant

totalPrice = onionSubTotal+potatoSubTotal+eggplantSubTotal

print(
    "Krumpli : ",potatoPieces,"*",potato, "FT/KG","=",round(potatoSubTotal),"FT","\n"
    "Hagyma : ",onionPieces,"*",onion, "FT/KG","=",round(onionSubTotal),"FT","\n"
    "Padlizsán : ",eggplantPieces,"*",eggplant, "FT/KG","=",round(eggplantSubTotal),"FT","\n"
    "------------------------------------------------------------- Összesen:",round(totalPrice),"FT"
)

