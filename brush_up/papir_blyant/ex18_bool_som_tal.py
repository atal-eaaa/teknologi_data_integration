# Øvelse 18 - Konvertering: Boolean bliver til tal
#
# Læs koden herunder. Skriv på papir, hvad de to print-linjer udskriver.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Ny ting: Python opfatter True som tallet 1 og False som tallet 0,
# hvis man bruger dem sammen med + eller -.

er_myndig = True
har_rabat = False

pris = 100
pris_med_bonus = pris + er_myndig
pris_med_rabat = pris - har_rabat

print(pris_med_bonus)
print(pris_med_rabat)
