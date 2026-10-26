# Øvelse 31 - Byg en liste af par med nested loop (SVÆR)
#
# Læs koden herunder. Skriv på papir, hvad programmet printer.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Tip: (i, j) er et "par" (en tuple). par.append((i, j)) lægger
# parret til sidst i listen "par". Skriv listen "par" op på papiret,
# og tilføj ét par ad gangen, som loopet arbejder sig igennem.

par = []
for i in range(1, 3):
    for j in range(1, 3):
        par.append((i, j))

print(par)
