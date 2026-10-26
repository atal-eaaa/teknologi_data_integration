import pandas as pd

# Opgave 1
# -------------------------
opgave = 1
lst = [5, 7, 13, 2, 1, -5, 6, 12, 15]
x = 0
for i in lst:
    if i / 2 == int(i/2):
        x = x + i - 1
print( f"Opgave {opgave}: x={x}")


# Opgave 2
# -------------------------
opgave +=1
navn1 = 'Anders And, Andeby' 
navn2 = navn1.replace("An", "x")
x = len(navn1) - len(navn2)
print( f"Opgave {opgave}: x={x}")




# Opgave 3
# -------------------------
opgave +=1
navn1 = 'Annette Antonsens vandland' 
navn2 = navn1.replace("an", "x")
x = len(navn1) - len(navn2)
print( f"Opgave {opgave}: x={x}")



# Opgave 4
# -------------------------
opgave +=1
navn1 = 'Annette Antonsens vandland' 
navn2 = navn1.upper().replace("an", "x")
x = len(navn1) - len(navn2)
print( f"Opgave {opgave}: x={x}")



# Opgave 5
# -------------------------
opgave = 4
opgave +=1
navn = 'Annette Antonsens vandland' 
if 'k' in navn:
    x = 1
elif 's' in navn[:5]:
    x = 2
elif 'l' in navn[-4:]:
    x = 3
else:
    x = 4      
print( f"Opgave {opgave}: x={x}")


# Opgave 6
# -------------------------
opgave = 6
lst = [1] 
lst.append(3)
x = sum(lst) / len(lst)
print( f"Opgave {opgave}: x={x}")


# Opgave 7
# -------------------------
opgave +=1
lst = [1, 2] 
lst.append(3)
lst.append([4, 4])
x = len(lst)
print( f"Opgave {opgave}: x={x}")



# Opgave 8
# -------------------------
opgave +=1
y = '10.10'
y = y.replace('.','')
if y.isnumeric() and int(y) == float(y):
    x = 1
elif len(y) < 5:
    x = 2
else:
    x = 3    
print( f"Opgave {opgave}: x={x}")



# Opgave 9
# -------------------------
opgave +=1
y = '7.77'
try: 
    x = int(y)
except: 
    x = 0    
print( f"Opgave {opgave}: x={x}")



# Opgave 10
# -------------------------
opgave +=1
headers = ['A', 'B']
lst = [[1, 5], [2, 10], [6, 6]]
df  = pd.DataFrame(lst, columns=headers)
x = df['A'].sum()
print( f"Opgave {opgave}: x={x}")


# Opgave 11
# -------------------------
opgave +=1
headers = ['A', 'B']
lst = [[1, 5], [10, 2], [6, 6]]
df  = pd.DataFrame(lst, columns=headers)
x = df['A'].max() - df['B'].min()
print( f"Opgave {opgave}: x={x}")


# Opgave 12
# -------------------------
opgave +=1
headers = ['A', 'B', 'C']
lst1 = [[1, 3, 5], [2, 4, 6]]
lst2 = [[3, 4, 6]]
df1  = pd.DataFrame(lst1, columns=headers)
df2  = pd.DataFrame(lst2, columns=headers)
df3  = pd.concat([ df1, df2])
x    = len(df3)
print( f"Opgave {opgave}: x={x}")





# Opgave 13
# -------------------------
opgave +=1
headers = ['A', 'B', 'C']
lst1 = [[1, 3, 5], [2, 4, 6]]
lst2 = [[3, 4, 6]]
df1  = pd.DataFrame(lst1, columns=headers)
df2  = pd.DataFrame(lst2, columns=headers)
df3  = pd.concat([ df1, df2])
x    = df3['A'].min() + df3['A'].max() + df3['A'].mean() 
print( f"Opgave {opgave}: x={x}")


# Opgave 14
# -------------------------
opgave +=1
x = 100
while x > 33:
    x = int(x/2) 
print( f"Opgave {opgave}: x={x}")


# Opgave 15
# -------------------------
opgave +=1
tekst = "Olsens automobil-børs"
while tekst[-1] != 'm':
    tekst = tekst[:-1]
x = len(tekst)
print( f"Opgave {opgave}: x={x}")


# Opgave 16
# -------------------------
opgave +=1
headers = ['Produkt', 'Type', 'Antal', 'Pris']
lst = [
       ['Skrue', 'Rustfri', 2, 3],
       ['Skrue', 'Blank', 4, 2],
       ['Søm', 'Rustfri', 5, 2],
       ['Søm', 'Blank', 4, 1]
      ]

df  = pd.DataFrame(lst, columns=headers)
df['Omsætning'] = df['Antal'] * df['Pris']
x = df['Omsætning'].sum()
print( f"Opgave {opgave}: x={x}")


# Opgave 17
# -------------------------
opgave +=1
headers = ['Produkt', 'Type', 'Antal', 'Pris']
lst = [
       ['Skrue', 'Rustfri', 2, 3],
       ['Skrue', 'Blank', 4, 2],
       ['Søm', 'Rustfri', 5, 2],
       ['Søm', 'Blank', 4, 1]
      ]

df  = pd.DataFrame(lst, columns=headers)
df1 = df[df['Produkt'] == 'Skrue'] 
x = df['Antal'].min()
print( f"Opgave {opgave}: x={x}")


# Opgave 18
# -------------------------
opgave +=1
headers = ['Produkt', 'Type', 'Antal', 'Pris']
lst = [
       ['Skrue', 'Rustfri', 2, 3],
       ['Skrue', 'Blank', 4, 2],
       ['Søm', 'Rustfri', 5, 2],
       ['Søm', 'Blank', 4, 1],
       ['Bolt', 'Rustfri', 2, 5],
       ['Bolt', 'Blank', 1, 3],
      ]

df  = pd.DataFrame(lst, columns=headers)
df1 = df[(df['Produkt'] == 'Skrue') & (df['Type'] == 'Rustfri') ] 
x = len(df1)
print( f"Opgave {opgave}: x={x}")


# Opgave 19
# -------------------------
opgave +=1
headers = ['Produkt', 'Type', 'Antal', 'Pris']
lst = [
       ['Skrue', 'Rustfri', 2, 3],
       ['Skrue', 'Blank', 4, 2],
       ['Søm', 'Rustfri', 5, 2],
       ['Søm', 'Blank', 4, 1],
       ['Bolt', 'Rustfri', 2, 5],
       ['Bolt', 'Blank', 1, 3],
      ]

df  = pd.DataFrame(lst, columns=headers)
df1 = df[(df['Produkt'] == 'Skrue') | (df['Produkt'] == 'Bolt') ] 
x = df1['Antal'].sum()
print( f"Opgave {opgave}: x={x}")


# Opgave 20
# -------------------------
opgave +=1
headers = ['Produkt', 'Afsætning', 'Omsætning']
lst = [
       ['Æbler', 3, 6],
       ['Æbler', 2, 4],
       ['Blommer', 3, 3],
       ['Pærer', 4, 8],
       ['Blommer', 1, 1],
       ['Blommer', 2, 2]
      ]

df  = pd.DataFrame(lst, columns=headers)
df1 = df.groupby(['Produkt']).sum()
x = len(df1)
print( f"Opgave {opgave}: x={x}")


# Opgave 21
# -------------------------
opgave +=1
headers = ['Produkt', 'Afsætning', 'Omsætning']
lst = [
       ['Æbler', 3, 6],
       ['Æbler', 2, 4],
       ['Blommer', 3, 3],
       ['Pærer', 4, 8],
       ['Blommer', 1, 1],
       ['Blommer', 2, 2]
      ]

df  = pd.DataFrame(lst, columns=headers)
df1 = pd.concat([df, df])
df1 = df.groupby(['Produkt']).sum()
x = len(df1)
print( f"Opgave {opgave}: x={x}")


# Opgave 22
# -------------------------
opgave +=1
headsalg = ['Produkt', 'Afsætning', 'Omsætning']
salg = [
        ['Æbler', 3, 9],
        ['Æbler', 2, 6],
        ['Blommer', 3, 6],
        ['Pærer', 4, 12],
        ['Blommer', 1, 2],
        ['Blommer', 2, 4]
       ]
headcost = ['Produkt', 'VE']
cost = [
        ['Æbler', 2],
        ['Blommer', 1],
        ['Pærer', 2],
        ['Appelsiner', 3]
       ]
df1 = pd.DataFrame(salg, columns=headsalg)
df2 = pd.DataFrame(cost, columns=headcost)
df  = pd.merge(df1, df2, left_on='Produkt', right_on='Produkt', how='left')
x = len(df)
print( f"Opgave {opgave}: x={x}")




# Opgave 23
# -------------------------
opgave +=1
headsalg = ['Produkt', 'Afsætning', 'Omsætning']
salg = [
        ['Æbler', 3, 9],
        ['Æbler', 2, 6],
        ['Blommer', 3, 6],
        ['Pærer', 4, 12],
        ['Blommer', 1, 2],
        ['Blommer', 2, 4]
       ]
headcost = ['Produkt', 'VE']
cost = [
        ['Æbler', 2],
        ['Blommer', 1],
        ['Pærer', 2],
        ['Appelsiner', 3]
       ]
df1 = pd.DataFrame(salg, columns=headsalg)
df2 = pd.DataFrame(cost, columns=headcost)
df  = pd.merge(df1, df2, left_on='Produkt', right_on='Produkt', how='right')
x = len(df)
print( f"Opgave {opgave}: x={x}")


# Opgave 24
# -------------------------
opgave +=1
lst = [3, 5, 8, 5, 1, 1, 6, 3, 1, 11]
x = lst.count(1) 
print( f"Opgave {opgave}: x={x}")



# Opgave 25
# -------------------------
opgave +=1
x = 0
i = 0
lst = [3, 5, 8, 5, 1, 1, 6, 3, 1, 11]
while lst[i] < 7:
    x += lst.count(lst[i])
    i += 1
print( f"Opgave {opgave}: x={x}")


# Opgave 26
# -------------------------
opgave +=1
lst = [3, 5, 8, 5, 1, 1, 6, 3, 1, 11]
lst = sorted(lst)
x = lst[-1] - lst[-2] 
print( f"Opgave {opgave}: x={x}")


# Opgave 27
# -------------------------
opgave +=1
lst = [3, 5, 8, 5, 1, 1, 6, 3, 1, 11]
lst = sorted(lst, reverse=True)
x = lst[0] + lst[-1] * lst[-2]
print( f"Opgave {opgave}: x={x}")


# Opgave 28
# -------------------------
opgave +=1
lst = [3, 5, 8, 5, 1, 1, 6, 3, 1, 11]
lst = sorted(lst[:9], reverse=True)
x = lst[0] + lst[-1] * lst[-2]
print( f"Opgave {opgave}: x={x}")


# Opgave 29
# -------------------------
opgave +=1
new_lst = []
lst = [3, '5', [8, 5], 1, "Ole", 2, 4]
for element in lst:
    if isinstance(element, int) == True:
        new_lst.append(element)
        if element == "Ole":
            new_lst.append(element)
x = new_lst.count("Ole")
x += sum(new_lst)
print( f"Opgave {opgave}: x={x}")


# Opgave 30
# -------------------------
prime_numbers = [2]
for tal in range(3, 100):
    for faktor in prime_numbers:
        is_prime = (tal / faktor != int(tal/faktor))
        if not is_prime or tal/faktor < 2:
            break
    if is_prime:
        prime_numbers.append(tal)        
print( prime_numbers)