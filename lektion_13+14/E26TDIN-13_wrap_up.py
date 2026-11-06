# %% : ØVELSE 1

tekst = 'Der er et yndigt land'
x = len(tekst)
tekst = tekst.replace('er', '')
x -= len(tekst)
print(x)



# %% : ØVELSE 2
import pandas as pd

salg = { 
    'mandag' : {'Æbler' : 3, 'Pærer' : 3}, 
    'tirsdag' : {'Æbler' : 4, 'Pærer' : 2},
    'onsdag' : {'Æbler' : 3, 'Pærer' : 5}
}
df = pd.DataFrame.from_dict(salg, orient='index')
print(df['Æbler'].sum())



# %% : ØVELSE 3

liste = [1, 1]
for i in range(10):
    if i % 2 == 0:
        liste[0] += i
    elif i % 3 == 0:
        liste[1] += i
    else:
        liste.append(i)    
print(len(liste))


# %% : ØVELSE 4

x = 2
x = x ** 2
x = x // 3
x -= x % 3
print(x)


# %% : ØVELSE 5

x = [2, 3, 4]
y = [1, 5, 6]

if sum(y)/2 > max(x):
    x.append(5)
else:
    y.append(3)    
x = sum(x) - sum(y)
print(x)


# %% : ØVELSE 6
import statistics as sts

p = [100, 200, 300]
x = 0
for i in range(sts.mean(p)):
    if i-1 in p:
        x += i
print(x)



# %% : ØVELSE 7


i = 0
j = 1
for x in range(4):
    j = j + i
    i = j - i
print(j)



# %% - ØVELSE 8

liste = ['1235', '3789', '9825', '8833' ]

for i, j in enumerate(liste):
    if int(j[i]) == i:
        break
print(j)


# %%
