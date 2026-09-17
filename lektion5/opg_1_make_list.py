number = 0
lst = []
while number < 71:
    if number / 7 == int(number / 7):
        lst.append(number)
    number += 1

print(lst)