score_agf        = input('Hvor mange mål scorede AGF :')
score_modstander = input('Hvor mange mål scorede modstanderen :')
score_agf        = int(score_agf)
score_modstander = int(score_modstander)

if score_agf > score_modstander:
    points_agf = 3
    points_modstander = 0
elif score_agf == score_modstander:
    points_agf = 1
    points_modstander = 1
else:
    points_agf = 0
    points_modstander = 3

print("Points til AGF :", points_agf)    
print("Points til modstander :", points_modstander)    
    