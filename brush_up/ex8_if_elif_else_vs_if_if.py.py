# Øvelse 8 - If-elif-else vs. if-if-if
#
# Læs koden herunder. Skriv på papir, hvad Version A og Version B printer.
# Du må IKKE køre koden, bruge lommeregner, Google eller AI.
#
# Spørgsmål:
# 1) Hvad printer Version A?
# 2) Hvad printer Version B?
# 3) Hvorfor er der forskel på, hvor meget de to versioner printer,
#    selvom de bruger de samme betingelser?

point = 80

# ---------- Version A: if-elif-else ----------
# Computeren tjekker betingelserne oppefra og ned.
# Så snart én betingelse er sand, udføres den gren,
# og resten af elif/else springes helt over.
if point >= 90:
    print("A: Guld")
elif point >= 75:
    print("A: Sølv")
elif point >= 50:
    print("A: Bronze")
else:
    print("A: Ingen medalje")


# ---------- Version B: if-if-if-if ----------
# Her er der fire ADSKILTE if-statements.
# Computeren tjekker dem ALLE, uafhængigt af hinanden.
# Der kan derfor godt blive printet mere end én linje.
if point >= 90:
    print("B: Guld")
if point >= 75:
    print("B: Sølv")
if point >= 50:
    print("B: Bronze")
if point < 50:
    print("B: Ingen medalje")
