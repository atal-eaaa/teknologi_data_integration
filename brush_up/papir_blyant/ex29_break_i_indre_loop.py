# Øvelse 29 - Break i det indre loop (SVÆR)
#
# Læs koden herunder. Skriv på papir ALT det, programmet printer,
# linje for linje, i den rækkefølge det sker.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Tip: break stopper kun det INDERSTE loop, den er placeret i.
# Det ydre loop (i) fortsætter helt normalt bagefter.

for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(i, j)
