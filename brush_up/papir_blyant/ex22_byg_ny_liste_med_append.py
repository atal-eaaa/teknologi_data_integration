# Øvelse 22 - Byg en ny liste med .append()
#
# Læs koden herunder. Skriv på papir, hvad programmet printer.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Tip: dobbelt.append(x) lægger x til sidst i listen "dobbelt".
# Lav evt. en tegning af listen "dobbelt", og tilføj ét tal ad gangen.

tal = [1, 2, 3, 4]
dobbelt = []
for t in tal:
    dobbelt.append(t * 2)
    print(dobbelt)
