############
# ØVELSE 2 #
############

print(f'\nØVELSE 2\n')

yourlist = [1,5,3,2,3,2,8,1,5]

x=yourlist[-1] # sidste element i listen, altså 5.
i=0 # plads i listen

while yourlist[i] != 2: # looper gennem listen, indtil vi rammer 2
    x+=yourlist[i]
    i+=1 # opdaterer i, så vi går videre til næste element i listen.

x+=i # læg
print(x)