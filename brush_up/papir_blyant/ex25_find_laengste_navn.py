# Øvelse 25 - Find det længste navn i en liste
#
# Læs koden herunder. Skriv på papir, hvad programmet printer.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Tip: len(navn) tæller, hvor mange bogstaver der er i "navn".
# Lav en lille tabel på papiret med kolonnerne "navn" og "længste",
# og opdater "længste" for hver omgang i loopet.

navne = ["Mette", "Anders", "Zainab"]
længste = ""

for navn in navne:
    if len(navn) > len(længste):
        længste = navn

print(længste)
