# Øvelse 32 - While-loop med to summer på samme tid (SVÆR)
#
# Læs koden herunder. Skriv på papir, hvad de to print-linjer udskriver.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Tip: Lav en tabel på papiret med kolonnerne tal, sum_lige og
# sum_ulige, og opdater ALLE tre for hver omgang i loopet.

tal = 10
sum_lige = 0
sum_ulige = 0

while tal > 0:
    if tal % 2 == 0:
        sum_lige = sum_lige + tal
    else:
        sum_ulige = sum_ulige + tal
    tal = tal - 1

print(sum_lige)
print(sum_ulige)
