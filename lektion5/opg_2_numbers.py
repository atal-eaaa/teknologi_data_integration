numbers = [3, 2, 4, 4, 3, 5, 2, 1, 3, 6]
count1 = 0
count2 = 0
for number in numbers:
    if number <= 3:
        count1 +=1
    elif number != 3:
        count2 +=1

print(count1, count2)    

