from random import random

# Ilyet már csináltunk, de most te írod meg az egészet az
# elejétől.
# Írj egy programot, amiben két karakter harcol egymással.

kar1elet = 100
kar2elet = 100

kar1sebz = 20
kar2sebz = 30

kar1vedekezes = 0.5
kar2vedekezes = 0.4

# A harc addig tart, míg egyikük meg nem hal.
# Körönként zajlik a harc, írasd ki minden kör elején, hogy
# hányadik körben vagyunk.
# Az, hogy bent van-e az ütés, a random() véletlenszám-generáló
# függvénnyel döntsd el, ami 0 és 1 között generál számot.
# asd for git


from random import random

kor = 1
while kar1elet * kar2elet < 0:
    print("Ez volt a:", kor, "kör")

# Egyik karakter támad:

if random() < 0.4:
    kar2elet -= 20
    print("1-es karakter nyerte a kört")
else:
    print("Visszaverte a 2-es karakter.")

# Másik karakter támad:

if random() < 0.5:
    kar1elet -= 30
    print("2-es karakter nyerte a kört")
else:
    print("A 2-es szerette volna nyerni")

if kar1elet <= 0:
    kar1elet = 0
if kar2elet <= 0:
    kar2elet = 0

kor += 1

if kar1elet == 0:
    print("1-es karakter meghalt!")
if kar2elet == 0:
    print("2-es karakter meghalt!")