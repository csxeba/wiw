# A ciklusok arra valók, hogy újra és újra végrehajtsanak egy kód-blokkot
# Ezt az ismételt végrehajtást iterációnak nevezzük és ezt a szót
# NAGYON SOKSZOR fogom használni :)
# Kétfajta ciklus van, a while és a for és mindkettő összetett utasítás
# (tehát kell kettőspont és behúzás)

# ------------
# while ciklus
# ------------

# a while ciklus addik ismétlődik, amíg a megadott feltétel igaz.
i = 0
while i < 10:
    print("i értéke:", i)
    i += 1

# A while végére tehetünk egy else blokkot. Ez akkor fut le, ha a feltétel
# hamisra váltott:
i = 0
while i < 3:
    i += 1
else:
    print("i értéke: ", i)

# Én személy szerint a while-t ritkán használom, de van egy nagyon praktikus alkalmazása
# Végtelen ciklus:
print("Hello Szab", end="")
while 1:
    print("i")  # A program futását leállíthatod, ha nyomsz egy Ctrl-C-t :)

# Ilyen végtelen ciklusokat gyakran használunk, például eseményfigyelőként:
dobasosszeg = 0
while 1:
    dobasosszeg += int(input("Kockadobás: "))
    if dobasosszeg > 30:
        break

# Lista végigjárása while segítségével
lista = [1, 2, 3, 4, 5, 6, 7, 8]
i = 0  # az iterációs index
while i < len(lista):
    print("i =", i, "lista[i] =", lista[i])

# A break utasítással lehet "kitörni" a ciklusból.
# Egymásba ágyazott ciklusoknál nem működik
# (illetve csak abból tör ki, amelyikben benne van)

# ------------
# for ciklus
# ------------

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

# Itt van egy újabb kulcsszó is, a continue:
for element in lista:
    if element % 2 == 0:
        continue
    print(element)
# ha az element értéke kettővel osztva nulla maradékot ad
# (tehát kettővel osztható szám) (tehát páros :D)
# akkor megszakítjuk a ciklust és átugrunk a következő elemre.
# Itt nem szakad félbe a futás, csak átugorjuk az adott elemet.

# TODO: for-finally
# TODO: range, enumerate, iterátorok
# TODO: listaépítés (comprehension)
