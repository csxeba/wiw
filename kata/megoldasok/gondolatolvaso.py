# Ezt a stringet mindig a végére szeretném írni
# Ha bedobom egy változóba az elején, akkor nem kell
# mindig kiírni majd az egészet.
suffix = "\nHa kész, üss enter-t!"

# itt az inputot kiíratásra használom.
# Ez annyiban más, hogy miután kiírta a promptot,
# vár egy entert. Amivel visszatér, azzal nem foglalkozunk.
input("Gondolj egy számra!" + suffix)
input("Adj hozzá ötöt!" + suffix)
input("Vonj ki belőle hármat!" + suffix)
input("Vond ki belőle az eredeti számot!" + suffix)

szerintem = (5 - 3)

input("Szerintem az eredmény: " + str(szerintem) + suffix)

# itt már elkapjuk a user által adott bemenetet.
eredmeny = input("Neked mennyi jött ki? > ")
eredmeny = int(eredmeny)  # Átalakítjuk számmá

if eredmeny != szerintem:
    print("Hazudsz, te disznó!")
else:
    print("Menő, mi?")
