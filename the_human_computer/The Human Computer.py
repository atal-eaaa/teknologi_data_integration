# Opgave 1
#-------------------
opgave = 1
x = 7
for i in range(3):
    x += 1
print(f"Opgave {opgave}: x={x}")



# Opgave 2
#-------------------
opgave +=1
x = 5
for i in range(4):
    if i < 2:
        x += 1
    else:
        x += 2
print(f"Opgave {opgave}: x={x}")    



# Opgave 3
#-------------------
opgave +=1
x = 7
x = int(x/3)
print(f"Opgave {opgave}: x={x}")



# Opgave 4
#-------------------
opgave +=1
x = 12
y = 1
while y < x:
    x -= 2
    y += 1
print(f"Opgave {opgave}: x={x}, y={y}")
     


# Opgave 5
#-------------------
opgave +=1
x = 'Ole'
try:
    x = x / 3
except:
    x = len(x)
print(f"Opgave {opgave}: x={x}")  



# Opgave 6
#-------------------
opgave +=1
lst = [5, 6, 7, 8]
x   = lst[2]
print(f"Opgave {opgave}: x={x}")



# Opgave 7
#-------------------
opgave +=1
lst = [5, 6, 7, 8]
x   = lst[-2]
print(f"Opgave {opgave}: x={x}")



# Opgave 8
#-------------------
opgave +=1
lst = [5, 6, 7, 8]
x   = lst[:2][-1]
print(f"Opgave {opgave}: x={x}")



# Opgave 9
#-------------------
opgave +=1
lst = [[1,2,4,8], [4,3,2,1], [-1, 0, 1]]
x = lst[1][-3]
print(f"Opgave {opgave}: x={x}")



# Opgave 10
#-------------------
opgave +=1
lst = [[1,2,3,4], [4,3,2,1], [-1, 0, 1]]
x = sum(lst[2])
print(f"Opgave {opgave}: x={x}")



# Opgave 11
#-------------------
opgave +=1
lst = [[1,2,3,4,5], [4,3,2,1], [-1, 0, 1, 0, -1]]
x = len(lst[0])
print(f"Opgave {opgave}: x={x}")



# Opgave 12
#-------------------
opgave +=1
x = 0
lst = [[1,1,1], [2,2,2], [-1, -1, -1]]
for i in lst:
    x += sum(i) 
print(f"Opgave {opgave}: x={x}")    



# Opgave 13
#-------------------
opgave +=1
lst = [[1,2,3,4,5], [4,3,2,1], [-1, 0, 7, 0, -1]]
x = min(lst[0]) + max(lst[1]) + sum(lst[2])/len(lst[2])
print(f"Opgave {opgave}: x={x}")



# Opgave 14
#-------------------
opgave +=1
i = 6.7
x = int(2 * i)
y = 2 * int(i)
print(f"Opgave {opgave}: x={x}, y={y}")



# Opgave 15
#-------------------
opgave +=1
lst = [1, 2, 5, 4, 5, 6, 7]
x = []
for i in lst:
    if i < 5:
        x.append(x)
    elif i < 6:    
        x.append( 2 * i )
    else:
        pass
x = len(x)
print(f"Opgave {opgave}: x={x}")



# Opgave 16
#-------------------
opgave +=1
navn = "Ejnar gik en tur i Esbjerg"
x = navn.count('e')
print(f"Opgave {opgave}: x={x}")



# Opgave 17
#-------------------
opgave +=1
navn = "Ejnar gik en tur i Esbjerg"
x = navn.lower().count('E')
print(f"Opgave {opgave}: x={x}")



# Opgave 18
#-------------------
opgave +=1
def regnemaskine_1(a, b):
    x = 4 * a / b
    return x

x = regnemaskine_1(5, 2)
print(f"Opgave {opgave}: x={x}")



# Opgave 19
#-------------------
opgave +=1
x = 7
x = x == 7
print(f"Opgave {opgave}: x={x}")



# Opgave 20
#-------------------
opgave +=1
def regnemaskine_2(a):
    a = 2 * a
    if a < 10:
        a = regnemaskine_2(a)
    return a

x = regnemaskine_2(1)
print(f"Opgave {opgave}: x={x}")
