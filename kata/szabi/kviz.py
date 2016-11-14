# Írj egy kvízt, amiben 5 kérdést teszel fel.
# (egyszerű választás stílusban például)
# A megszerzett pontokat kövesd nyomon.
# A végén szövegesen is értékeld a delikvenst.
# Bónusz pont, ha az input prompt jól néz ki :)

pontok = 0

ElsoKerdes = print("Hany TV csatornat indit Vajna bacsi, csak mert raer?")
megoldas = "1"
print("valasz1 : 1-es lehetőség : egyet")
print("valasz2 : 2-es lehetőség : hármat")
print("valasz3 : 3-as lehetőség : kilencet")

megoldas = input("válaszlehetőség száma:")

if megoldas == valasz3:
    pontok += 1
    print("Okos!")
else:
    print("Nem követed a híreket")

MasodikKerdes = print("Hany gigabites internet van Szabieknal?")
valasz1 = "2"
valasz2 = "3"
valasz3 = "1"
print("valasz1 : 1-es lehetőség : kettő")
print("valasz2 : 2-es lehetőség : három")
print("valasz3 : 3-as lehetőség : egy")

megoldas = input("válaszlehetőség száma:")

if megoldas == valasz3:
    pontok += 1
    print("Szabiéknál DIGI van")
else:
    print("Szabiéknál sajnos nem NASA van")

HarmadikKerdes = print("Hany honapja szenved Csabi azzal, hogy megtanítsa a Pythont?")
valasz1 = "3"
valasz2 = "1"
valasz3 = "Már Csabi sem tudja"
print("valasz1 : 1-es lehetőség : 3")
print("valasz2 : 2-es lehetőség : 1")
print("valasz3 : 3-as lehetőség : Már Csabi sem tudja")

megoldas = input("Válaszlehetőség száma:")

if megoldas == valasz3:
    pontok += 1
    print("Csabinak már csak őszhajszála fog nőni")
else:
    print("Csak szeretné Csabi ha ennyi ideje szenvedne")

print("Értékelés:")
if pontok < 0:
    print("Hát ez elég gyenge lett")
else:
    print("Jólvan, megy ez")