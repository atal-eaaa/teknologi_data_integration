# Øvelse 33 - Loop igennem bogstaverne i en tekst (SVÆR)
#
# Læs koden herunder. Skriv på papir, hvad programmet printer.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Tip: Et for-loop kan også gå igennem bogstaverne i en tekst,
# ét bogstav ad gangen. "or" betyder, at DET ER NOK, at ÉN af
# betingelserne er sand.

tekst = "python"
antal = 0

for bogstav in tekst:
    if bogstav == "o" or bogstav == "y":
        antal = antal + 1

print(antal)
