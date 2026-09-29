tilfredshed = [3, 4, 2, 5, "super god", 0, 3, 4, 4, 3, 1, 5, 4, 3, 1, 2, 10, -1000, 5, 3, 2, 100, 4, 4, 3, 4, 3, 4, 5, 4, 3, "vil ikke svare", 3, 4, 4]
renset = []
utilfreds_graense = 2

for score in tilfredshed:
    try:
        score = int(score)
        if score >=1 and score <= 5:
            renset.append(score)
    except:
        pass

utilfredse = 0
for score in renset:
    if score <= 2:
        utilfredse +=1

utilfreds_pct = round(utilfredse/len(renset) * 100, 2)
print("Andel af utilfredse gæster :", utilfreds_pct, "%")