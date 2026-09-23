antal_kager = input("Hvor mange kager er der i dåsen? ")
antal_kager = int(antal_kager)

if antal_kager >= 2:
    print("HELDIGT! Vi får begge en kage!")
    antal_kager = antal_kager - 2
elif antal_kager == 1:
    print("Synd for dig! Du får ingen kage.")
    antal_kager = antal_kager - 1
else: 
    print("Øv, øv, øv! Jeg får ingen kage")
    print("Og det gør du heller ikke!")

print("Farvel og tak for i dag!")