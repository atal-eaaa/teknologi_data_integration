liste = []
while True:
    tal = input("Tast et heltal (S for stop):")
    if tal == "S":
        break
    tal = int(tal)
    liste.append(tal)
    print(liste)

print(f"Summen af liste er : {sum(liste)}")

