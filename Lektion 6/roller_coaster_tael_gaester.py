# Initier tællevariable, der tææller hhv.
# antal godkendte og antal afviste.
antal_afviste   = 0
antal_godkendte = 0
while True:
    hojde = input("Gæstens højde i cm :")

    # Stop loopet, hvis der indtastes S eller s
    if hojde == "S" or hojde == "s":
        break

    # Konverter indtastning til integer    
    hojde = int(hojde) 

    # Er højden under 130 afvises gæsten,
    # i modsat fald får gæsten adgang.
    # Relevant tællevariabel tælles een op
    if hojde < 130:
        print("Afvis gæsten")
        antal_afviste +=1
    else:
        print("Ønsk gæsten god tur")
        antal_godkendte +=1

# Dagen er slut. Dagsrapport udskrives
print("Dagsrapport")
print("-----------------------------")
print("Antal godkendte :", antal_godkendte)
print("Antal afviste   :", antal_afviste)            