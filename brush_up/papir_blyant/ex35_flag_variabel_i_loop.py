# Øvelse 35 - Flag-variabel i et loop (SVÆR)
#
# Læs koden herunder. Skriv på papir ALT det, programmet printer,
# linje for linje, i den rækkefølge det sker.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Tip: "fundet" er en flag-variabel. Den starter som False og
# skiftes til True, hvis loopet finder det, den leder efter.
# Den sidste print-linje ligger UDENFOR loopet.

fundet = False
tal_liste = [4, 9, 15, 22]

for tal in tal_liste:
    if tal % 5 == 0:
        fundet = True
        print("Fundet et tal deleligt med 5:", tal)

print(fundet)
