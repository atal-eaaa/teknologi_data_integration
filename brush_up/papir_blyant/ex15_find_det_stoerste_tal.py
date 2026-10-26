# Øvelse 15 - Find det største tal i en liste
#
# Læs koden herunder. Skriv på papir, hvad programmet printer.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
# Tip: Lav en lille tabel på papiret med kolonnerne "tal" og "størst",
# og opdater "størst" for hver omgang i loopet.

tal_liste = [3, 8, 2, 10, 5]
størst = 0
for tal in tal_liste:
    if tal > størst:
        størst = tal
print("Det største tal er", størst)
