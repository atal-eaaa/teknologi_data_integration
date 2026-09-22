# Øvelse 16 - While-loop med break
#
# Læs koden herunder. Skriv på papir ALT det, programmet printer,
# linje for linje, i den rækkefølge det sker.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Ny ting: "while True" betyder, at loopet i princippet kører for
# evigt. "break" stopper loopet med det samme, uanset hvad.

tal = 1
while True:
    print(tal)
    if tal == 3:
        break
    tal = tal + 1
print("Færdig")
