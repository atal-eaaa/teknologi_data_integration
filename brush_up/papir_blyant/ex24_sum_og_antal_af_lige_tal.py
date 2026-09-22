# Øvelse 24 - Loop med betingelse: Sum og antal af lige tal
#
# Læs koden herunder. Skriv på papir, hvad de to print-linjer udskriver.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Tip: Lav en lille tabel på papiret med kolonnerne "tal", "sum_lige"
# og "antal_lige", og opdater dem for hver omgang i loopet.

tal_liste = [4, 7, 10, 3, 8, 5]
sum_lige = 0
antal_lige = 0

for tal in tal_liste:
    if tal % 2 == 0:
        sum_lige = sum_lige + tal
        antal_lige = antal_lige + 1

print(sum_lige)
print(antal_lige)
