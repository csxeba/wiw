# Írj egy kvízt, amiben 5 kérdést teszel fel.
# (egyszerű választás stílusban például)
# A megszerzett pontokat kövesd nyomon.
# A végén szövegesen is értékeld a delikvenst.
# Bónusz pont, ha az input prompt jól néz ki :)

prompt = "\t> "
kerdesek = [
    "Hanyadik keruletben lakik Csabi?",
    "10-es skálán mennyire szeret Csabi programozni Szabival?",
    "Hány felhasználója van az nCore-nak?",
    "Milyen színe van az égnek?"
]

valaszok = []
pontok = 0

# 1. kérdés
kerulet = input(kerdesek[0] + prompt)
valaszok += [ip]

if ip == "7":
    print("1. kérdés helyes!")
    pontok += 1
else:
    print("Ajj nem jó!")

# 2. kérdés
eletkedv = input(kerdesek[1] + prompt)
valaszok += [eletkedv]

if eletkedv == "1":
    print("2. kérdés helyes!")
    pontok += 1
else:
    print("Ajj, nem jó!")

# 3. kérdés
felhasznalo = input(kerdesek[2] + prompt)
valaszok += [felhasznalo]

if felhasznalo == "691987":
    print("3. kérdés helyes!")
    pontok += 1
else:
    print("Ajj, nem jó!")

# 4. kérdés
eg_szine = input(kerdesek[3] + prompt)
valaszok += [eg_szine]

if eg_szine == "kék":
    print("4. kérdés helyes!")
    pontok += 1
else:
    print("Ajj, nem jó!")

# Értékelés
print("-" * 50)
print("Pontjaid száma:", pontok, "/", 4)
print("-" * 50)
print("Válaszok:", valaszok[0], valaszok[1],
      valaszok[2], valaszok[3], sep="\n")
print("-" * 50)

if pontok > 0:
    print("Ügyes vagy!")
else:
    print("Béna voltál!")