respondents = [ 9, 7, 8, 9, 10, 9, 10, 9, 8, 7, 6, 0, 10, 7, 9, 5, 7, 9, 10, 9, 9, 7, 8, 9, 10, 1, 9, 8, 6, 9]
promoters = 0
passives = 0
detractors = 0

for score in respondents:
    if score > 8:
        promoters  += 1
    elif score < 7:
        detractors += 1
    else:       
        passives +=1

nps = round(( promoters / len(respondents) - detractors / len(respondents) ) * 100, 0)
print("NPS-score  : ", nps)
print("Promoters  : ", promoters)
print("Passives   : ", passives)
print("Detractors : ", detractors)