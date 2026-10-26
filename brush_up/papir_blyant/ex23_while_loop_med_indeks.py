# Øvelse 23 - While-loop med indeks over en liste
#
# Læs koden herunder. Skriv på papir ALT det, programmet printer,
# linje for linje, i den rækkefølge det sker.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Tip: len(navne) er antallet af elementer i listen "navne".
# navne[i] er det element, der står på plads "i" i listen.

navne = ["Ida", "Oskar", "Freja"]
i = 0
while i < len(navne):
    print(i, navne[i])
    i = i + 1
