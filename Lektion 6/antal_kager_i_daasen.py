antal_kager = 5

if antal_kager > 0:
    print("Der er kager tilbage!")
    print("Jeg tager en chokoladekage.")
    antal_kager = antal_kager - 1

if antal_kager > 0:
    print("Der er også en kage til dig!")
    print("Du får en med nødder.")
    antal_kager = antal_kager - 1


print("Nu fortsætter dagen.")
print(f"Der er {antal_kager} kager tilbage.")

