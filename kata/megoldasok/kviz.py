pontok = 0  # ide gyűjtjük majd a pontokat
suffix = ">\t"  # ezt itt definiálom, hogy ne kelljen mindig kiírni

# Felépítem az első kérdés-stringet
k1 = "\t1.kérdés:\tHogy hívják a vak akkumulátort?\n"
k1 += "1) aksi\n"
k1 += "2) kaksi\n"
k1 += "3) vaksi\n"
# Bekérem a választ
# ezt így értelmezd: prompt ARGUMENTUM legyen egyenlő k1 VÁLTOZÓ tartalma + suffix VÁLTOZÓ tartalma
v1 = input(prompt=k1 + suffix)
v1 = int(v1)

if v1 == 3:
    pontok += 1
    print("Helyes válasz!")
else:
    print("Rossz válasz!")

print("Pontok:", pontok)

# Itt egyben definiálom a kérdés-stringet:
# tripla idézőjelet használok, mert akkor az entert is beleveszi a stringbe
k2 = """\t2. kérdés\tMi a címe a hackeres sorozatnak, amit ajánlottam?
1) Walter Mitty különös élete
2) Mr. Robot
3) Pentatronix
"""  # Vedd észre, a végén van egy enter!

v2 = int(input(k2 + suffix))  # itt nem írtam ki a kulcsszó nevét

if v1 == 2:
    pontok += 1
    print("Helyes válasz!")
else:
    print("Rossz válasz!")

print("Pontok:", pontok)

k3 = """\t3. kérdés (a mindent eldöntő)\tMikor kezdünk már programozni?
1) Majd
2) Ha betöltötted a 18-at, kisfiam
3) Már most is ezerrel azt csináljuk
"""

v3 = int(input(k3 + suffix))

if v3 == 1:
    pontok = 0
    print("Mivel szemtelenkedsz, elvesztetted az összes pontodat!")
elif v3 == 3:
    pontok = 0
    print("Jaj de nagy arcod lett hirtelen! :D")
else:
    pontok += 1

print("Végső értékelés:")
if pontok > 0:
    print(pontok, "pont,", end=" ")
    if pontok == 1:
        print("elég satnya eredmény")
    elif pontok > 1:
        print("te mekkora stréber vagy :D")
else:
    print("Ennyire számítottam... Mindig a sör meg a csajok, tanulás meg semmi.")
