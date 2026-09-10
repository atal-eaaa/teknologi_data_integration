lst =[]             # Danner en tom liste
lst = sorted(lst)   # Sorterer en liste
length = len(lst)   # Tæller antal elementer i listen
sumlst = sum(lst)   # Summerer elementerne i listen
x      = lst[3]     # Værdien af element nummer 4 i listen
lst.append(x)       # Tilføjer værdien x til listen lst

# test for, om en liste indeholder et lige
# eller et ulige antal elementer
if len(lst) % 2 == 0:
    print("Lige antal elementer")
else:
    print("Ulige antal elementer")

