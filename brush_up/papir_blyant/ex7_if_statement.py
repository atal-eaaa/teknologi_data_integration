# Øvelse 7 - If-statement
#
# Læs koden herunder. Skriv på papir, hvad de to print-linjer udskriver.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Ny ting: "and" betyder, at BEGGE betingelser skal være sande,
# for at hele udtrykket bliver True.

alder = 17
har_koerekort = True

maa_koere_bil = alder >= 18 and har_koerekort
print(maa_koere_bil)

if alder >= 18 and har_koerekort:
    print("Du må køre bilen")
else:
    print("Du må ikke køre bilen")
