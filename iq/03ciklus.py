# A ciklusok arra valók, hogy újra és újra végrehajtsanak egy kód-blokkot
# Ezt az ismételt végrehajtást iterációnak nevezzük és ezt a szót
# NAGYON SOKSZOR fogom használni :)
# Kétfajta ciklus van, a while és a for és mindkettő összetett utasítás
# (tehát kell kettőspont és behúzás)

# ------------
# while ciklus
# ------------

# a while ciklus addik ismétlődik, amíg a megadott feltétel igaz.
# i = 0
# while i < 10:
#     print("i értéke:", i)
#     i += 1
#
# # A while végére tehetünk egy else blokkot. Ez akkor fut le, ha a feltétel
# # hamisra váltott:
# i = 0
# while i < 3:
#     i += 1
#
# print("i értéke az else-ben:", i)

# Én személy szerint a while-t ritkán használom, de van egy nagyon praktikus alkalmazása
# Végtelen ciklus:
# print("Hello Szab", end="")
# while 1:
#     print("i", end="")  # A program futását leállíthatod, ha nyomsz egy Ctrl-C-t :)
#
# Ilyen végtelen ciklusokat gyakran használunk, például eseményfigyelőként:
dobasosszeg = 0
while dobasosszeg > 30:
    dobasosszeg += int(input("Kockadobás: "))

# Lista végigjárása while segítségével
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8]
i = 0  # az iterációs index
while i < len(lista):
    elem = lista[i]
    print("i =", i, "lista[i] =", elem)
    i += 1

# A break utasítással lehet "kitörni" a ciklusból.
# Egymásba ágyazott ciklusoknál nem működik
# (illetve csak abból tör ki, amelyikben benne van)

# ----------
# for ciklus
# ----------

# Na ezt a while-lal ellentétben valószínűleg RENGETEGET fogod használni
# Ez kifejezetten listák végigjárására használható és sokkal kompaktabb, mint a while
lista = [1, 2, 3, 4, 5, 6, 7, 8]
for element in lista:
    print(element)
# Mi történik? Megadunk egy változónevet (element). A ciklus végigmegy a listán és
# az aktuális elemet belepakolja a változóba. A változón végrehajtunk valamilyen utasítást
# vagy valamit csinálunk, aztán a ciklus végigér és átmegy a következő elemre.

# break a fornál is működik:
for element in lista:
    print(element)
    if element > 5:
        break

# Itt van egy újabb kulcsszó, a continue:
for element in lista:
    if element % 2 == 0:
        continue
    print(element)
# ha az element értéke kettővel osztva nulla maradékot ad
# (tehát kettővel osztható szám) (tehát páros :D)
# akkor megszakítjuk a ciklust és átugrunk a következő elemre.
# Itt nem szakad félbe a futás, csak átugorjuk az adott elemet.

# for után is állhat else. Az else ág akkor fut, ha a for által bejárt
# lista elemei elfogytak. Ilyet még sosem kellett használnom :)
# Egyetlen helyzetet tudok elképzelni, amikor ennek értelme lehet,
# de arról esetleg később
for element in lista:
    pass
else:
    print("Iteráció vége")

# Nézzük meg mi van, ha a listánk elemei összetett adattípusok (pl. listák):
nagylista = [[1, 2, 3, 4], [1, 2], [1, 2, 3]]
for kislista in nagylista:
    print("Kislista hossza:", len(kislista))
    print("Utolsó 2 eleme:", kislista[-2:])

# Ha a kislisták fix elemszámúak, pl. mindegyik 3 elemű, akkor ezt is bejátszhatod:
nagylista = [[1, 2, 3],
             [1, 3, 2],
             [2, 1, 3],
             [2, 3, 1],
             [3, 1, 2],
             [3, 2, 1]]
# Itt láthatod azt a trükköt is, hogy a zárójelek "eltörhetőek":
# zárójelpáron belül üthetsz entert, azt az értelmező figyelmen kívül hagyja
for a, b, c in nagylista:
    print("Kislista elemei:", a, b, c, sep="\t")

# ----------
# iterátorok
# ----------

# Létezik a Pythonban egy konstrukció, amit úgy hívnak, hogy iterátor.
# Iterátort képezhetünk iterálható adattípusokról (string, lista, tuple)
# Az iterátort végig lehet járni for ciklussal, viszont nem indexelhető
# és csak egyszer használatos:
iterator = iter(lista)
print(type(iterator))  # list_iterator típusú ez a valami
for element in iterator:
    print(element)
# Ugyanúgy kiír mindent, mintha a listát járnánk végig

for element in iterator:
    print(element)
# De többször nem lehet végigjárni, kiürült az iterátorunk

# Az iterátor valójában nem tárolja az adatokat, csak azok az instrukciók
# vannak benne, hogy hogyan "érhető el" a következő elem.
# Ezt azért fontos leírni, mert be szeretnék mutatni pár hasznos iterátor
# alapú kifejezést.

for i in range(10):
    print(i)
# A range függvény létrehoz egy iterátort, ami számokat ad vissza
# Három argumentuma van: start, end és step, hasonlóan az indexeléshez
# A startot elhagyhatod, ekkor az első argumentumot veszi end-nek
for i in range(3, -9, -4):
    print(i)
# Itt is lehet erősen trükközni: háromtól -9-ig (-9 már nem!)
# hátrafelé négyes lépésközzel :) 3, 0, -4, -8

# listává alakíthatsz egy range-et, ha pl. egynél többször fogod használni:
szamok = list(range(3, -9, -4))  # Persze ez lehet tuple is
print(szamok)

# Problémafelvetés: mi van, ha párhuzamosan több listát kell bejárnunk?
emberek = ["Szabi", "Anyu", "Apu", "Csabi", "Zita"]
pontok = [-1, 20, 8, 15, 18]
# Ki kéne írni, kinek hány pontja van...
# Csinálhatod pl. while ciklussal:
i = 0
while i < len(emberek):
    print(emberek[i], "pontja:", pontok[i])

# Csinálhatod for + range segítségével:
for i in range(len(emberek)):
    print(emberek[i], "pontja:", pontok[i])

# Vagy használhatod az enumerate() iterátorkészítőt, ami
# egy neki átadott lista elemeihez sorszámokat rendel.
enumeracio = list(enumerate(emberek))
print(enumeracio)  # Láthatod, hogy 2-elemű tuple-k jöttek létre
# Azt pedig már mutattam, hogy ha fix elemszámúak egy lista elemei,
# akkor használhatod az alábbi konstrukciót: (kislistás ügy)
for i, nev in enumerate(emberek):
    print(nev, "pontjai:", pontok[i])

# Még egy iterátorkészítőt mutatok, amit gyakran szoktam használni:
# Ha van két (vagy több) azonos elemszámú listád, akkor párbaállíthatóak
# a megfelelő elemeik a zip() függvény segítségével:
parok = list(zip(emberek, pontok))
print(parok)  # Itt is 2-elemű tuple-k jöttek létre
for nev, pontszam in zip(emberek, pontok):
    print(nev, "pontjai:", pontszam)

# Létezik a listakészítésnek egy nagyon elegáns és kompakt formája Pythonban
# Ezt comprehensionnek (röviden comp) hívják, megint csak nincs rá jó magyar
# szó, a list compot talán listaépítő kifejezésnek lehetne lefordítani.

# Legegyszerűbb formája talán a következő:
szamok = [i for i in range(10)]
# A compban lévő for végigjárja a range-et, az aktuális értéket az i-be teszi
# (ez a "for i in range(10)" rész)
# utána a listába beteszi az i-t (ez az első i az elején)
# Ugye ugyanezt elérhetjük egy sima list(range(10)) kifejezéssel is, így magába
# ritkán használjuk ezt, de vegyük a következő példát:

# pl. két vektor skaláris szorzata három dimenzióban (koordinátákkal) :D
#         [x, y]
vektor1 = [2, 3, 1]
vektor2 = [1, 2, 4]
# skaláris szorzat = vektor1.x * vektor2.x + vektor1.y * vektor2.y + vektor1.z * vektor2.z
# első lépés: szorzatok képzése:
szorzatok = [i * j for i, j in zip(vektor1, vektor2)]
# a két vektort összezipeljük (x-et az x-szel, y-t az y-nal)
# ellenőrizd le, mit ad a zip, ha gondolod:
print(list(zip(vektor1, vektor2)))
print(szorzatok)  # ezt is csekkolhatod, hogy helyes-e.
# Én nem ellenőriztem, de elvileg [2, 6, 4]

# Ha megvannak a szorzatok, össze kell adni őket:
# skalaris_szorzat = szorzatok[0] + szorzatok[1] + szorzatok[2]
# Persze Szabi, a hacker ilyet nem csinál:
skalaris_szorzat = sum(szorzatok)  # ugye, ugye??
# És Szabi, ha elkezd Pythonban gondolkodni, akkor ilyet sem csinál...
# Szabi egy sorba besúvasztja a fenti kifejezést:
besuvasztva = sum([i * j for i, j in zip(vektor1, vektor2)])
# a végén assertolhatjuk, hogy a két eredmény megegyezik:
assert skalaris_szorzat == besuvasztva, "A két eredmény eltér!"
# A stringet írja ki, ha nem egyenlő az assertben a két kifejezés
