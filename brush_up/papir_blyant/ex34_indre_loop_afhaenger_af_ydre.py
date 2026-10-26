# Øvelse 34 - Det indre loop afhænger af det ydre (SVÆR)
#
# Læs koden herunder. Skriv på papir, hvad print(resultat) udskriver
# til sidst - inklusiv linjeskift.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Tip: range(i) betyder, at det indre loop kører "i" gange - altså
# et ANDET antal gange, hver gang det ydre loop (i) skifter værdi.
# "\n" i en string betyder "skift til ny linje".

resultat = ""
for i in range(1, 4):
    for j in range(i):
        resultat = resultat + "*"
    resultat = resultat + "\n"

print(resultat)
