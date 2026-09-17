def convert(string):
    try:
        number = int(string)
    except:
        number = 0
    return number


lst = ["3", "-2", "2.5", "Olsen", "0", "5", "", "4"]
total = 0
for text in lst:
    total += convert(text)

print(total)