from random import random

# Ilyet már csináltunk, de most te írod meg az egészet az
# elejétől.
# Írj egy programot, amiben két karakter harcol egymással.

kar1elet = 100
kar2elet = 100

kar1sebz = 20
kar2sebz = 30

kar1vedekezes = 0.6
kar2vedekezes = 0.6

# A harc addig tart, míg egyikük meg nem hal.
# Körönként zajlik a harc, írasd ki minden kör elején, hogy
# hányadik körben vagyunk.
# Az, hogy bent van-e az ütés, a random() véletlenszám-generáló
# függvénnyel döntsd el, ami 0 és 1 között generál számot.

kor = 1
while kar1elet * kar2elet:
    print("\n" + "-"*50)
    print("Harci kör:", kor)

    # kar1 támad:
    print("Csabi támadja Szabit!")
    if random() < kar2vedekezes:
        kar2elet -= kar1sebz
        print("Csabi sebzi Szabit!")
        print("Szabinak maradt", kar2elet, "élete!")
    else:
        print("Szabi hárítja Csabi támadását!")

    # kar2 támad:
    print("Szabi visszatámad!")
    if random() < kar1vedekezes:
        kar1elet -= kar2sebz
        print("Szabi sebzi Csabit!")
        print("Csabinak maradt", kar1elet, "élete!")
    else:
        print("Csabi hárítja Szabi támadását!")

    if kar1elet <= 0:
        kar1elet = 0
    if kar2elet <= 0:
        kar2elet = 0

    kor += 1

if not kar1elet:
    print("\n" + "-" * 50 + "\nCsabi meghalt!")
if not kar2elet:
    print("\n" + "-" * 50 + "\nSzabi meghalt!")
