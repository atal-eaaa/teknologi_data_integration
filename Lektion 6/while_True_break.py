import random
hemmeligt_tal = random.randint(1,100)
print(hemmeligt_tal)


while True:
    navn = input ("Hvad er dit navn :")
    if navn == "STOP":
        break
    print("Hej ", navn)
print("Farvel og tak for i dag!")