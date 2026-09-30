new_list_1 = []
new_list_2 = []
numbers = [ 5, 3, 2, 3, 7, 4]
for number in numbers:
    if number > 4:
        new_list_1.append(number)
    if number != 3:
        new_list_2.append(number)

x = sum(new_list_1)
x = x + len(new_list_2)

print(x)