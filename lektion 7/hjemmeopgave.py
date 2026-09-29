""" 
Du skal veksle et beløb til så få mønter som muligt. Du har kun mønter af værdien 20, 10, 5 og 1 kr. 
  belob = 47
  antal_moenter = 0
Skriv et while-loop, der - så længe belob er større end 0 - trækker den størst mulige mønt fra belob 
(brug if/elif til at vælge mønten) og tæller antal_moenter op med 1, hver gang en mønt bruges.Print 
til sidst, hvor mange mønter der blev brugt i alt.
"""

beloeb = int(input("Indtast beløb : "))
moent_20 = 0
moent_10 = 0
moent_5  = 0
moent_1  = 0

while beloeb > 0:
    if beloeb >= 20:
        moent_20 +=1
        beloeb -=20
    elif beloeb >= 10:    
        moent_10 +=1
        beloeb -=10
    elif beloeb >= 5:    
        moent_5 +=1
        beloeb -=5
    else:
        moent_1 += 1
        beloeb -=1

print("Vekselpenge:")
print("----------------")
print(f"20'ere  : {moent_20} stk")
print(f"10'ere  : {moent_10} stk")
print(f" 5'ere  : {moent_5} stk")
print(f" 1'ere  : {moent_1} stk")
print("----------------")
