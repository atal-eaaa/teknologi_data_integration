# Øvelse 14 - For-loop med betingelse: Lige og ulige tal
#
# Læs koden herunder. Skriv på papir ALT det, programmet printer.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Ny ting: Tegnet % hedder "modulo" og giver resten ved division.
# Eksempel: 7 % 2 giver 1 (fordi 7 delt med 2 er 3 med 1 i rest).
# Et tal er LIGE, hvis resten ved division med 2 er 0.

for tal in range(1, 8):
    if tal % 2 == 0:
        print(tal, "er lige")
    else:
        print(tal, "er ulige")
