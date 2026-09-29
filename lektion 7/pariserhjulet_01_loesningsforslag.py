respondenter = [7, 39, 18, 12, 9, 42, 67, 11, 51, 34, 7, 6, 8, 32, 9, 38, 33, 4, 6, 77, 72, 8, 29, 4, 34, 10, 46, 6, 7]
aldersgraense = 15
boern = []
for respondent in respondenter:
    if respondent <= aldersgraense:
        boern.append(respondent)

procent_del = round(len(boern) / len(respondenter) * 100, 2)
gns_alder   = round(sum(boern) / len(boern), 1)

print("Andel af børn        :", procent_del, "%")
print("Børnenes gennemsnitsalder :", gns_alder)