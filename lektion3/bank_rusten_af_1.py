
############
# ØVELSE 1 #
############

print(f'\nØVELSE 1\n')

mylist = [1,5,4,3,2,2,8,1,5]
x=len(mylist) 

print(f'Længden af listen er: {x} \nDet vil sige at x starter med at være lig med {x}.\n')

print(f'Nu vil vi loope gennem listen og ændre x afhængigt af om i er lig med 2 eller ej.\n')
for i in mylist: # Nu looper vi gennem listen. i er elementet listen. i starter med 1, så 5, så 4 osv.
    print(f'Nu er i={i} og x={x}')
    if i==2: # hvis i er lig med 2, så trækker vi i fra x. 
        x-=i
    else: # ellers lægger vi i til x.
        x+=i

    print(f'Efter if-else betingelsen har x ændret værdi: i={i} og x={x}')
    print('---------------------')


# nu har vi looper gennem listen, og x er blevet ændret. Nu deler vi x med 2. 
x=x/2

print(f'Nu har vi divideret x med 2, og x er nu: {x}')
