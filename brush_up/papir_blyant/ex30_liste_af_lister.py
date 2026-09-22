# Øvelse 30 - Loop igennem en liste af lister (SVÆR)
#
# Læs koden herunder. Skriv på papir ALT det, programmet printer,
# linje for linje, i den rækkefølge det sker.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Tip: matrix er en liste, der indeholder tre andre lister.
# Det ydre loop tager én liste (én "row") ad gangen. Det indre
# loop går igennem tallene i den row.

matrix = [[1, 2], [3, 4], [5, 6]]

for row in matrix:
    for tal in row:
        print(tal)
