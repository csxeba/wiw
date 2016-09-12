# Ez komment

# Adattípusok, változó deklaráció
a = 2  # integer, vagy egész szám
b = 2.  # float, vagy lebegőpontos szám
# floatokról annyit kell tudni, hogy korlátozott a pontosságuk
# a 64 biten tárolt float 15-17 tizedesjegyig pontos, ezt
# double-nek is hívják pl. C/C++-ban (dupla pontosságú)
d = True  # bool, vagy igazság-érték, lehet True és False

# Kiíratás -> műveletek különböző adattípusokkal
print(a + b)  # 4.0  (mert <b> float)
print(a + a)  # 4    (mert <a> int)
print(a + d)  # 3    (ilyet is szabad)
print(b + d)  # 3.0  (sőt, ilyet is)

c = "2_"  # ez string, vagy karakterlánc
print(c * 2)  # 2_2_ (stringet szorozhatsz egésszel, ilyenkor megismétli)
c *= 2  # ez egy szorzás és egy változó-hozzárendelés egyben,
# tehát megszorzod 2-vel a c értékét, majd eltárolod c-ben az eredményt.
print(c)

# A művelettel egybekötött értékadást legtöbször egy számláló növelésére használjuk:
a = 1
a += 1  # növeli a értékét 1-gyel, 2-re.
a += 1
a += 1  # stb stb stb

# del kulcsszó változó(k) törlésére
# ennek nagy programoknál lehet jelentőssége, ha memóriát akarsz felszabadítani
del a, b, c, d

# többszörös értékadás
a = b = 1  # ilyet is lehet, bár én nem ajánlom, majd később meglátod, miért

# Valamicskét a kiíratásról:
# Pythonban a print() függvénnyel íratunk ki.
print("a:", a, "b:", b)


# többszörös párhuzamos értékadás
a, b, c, d = 1, 2, 3, 4
e, f, g, h = 4, 1, 2, 3
i, j, k, l = 3, 4, 1, 2
m, n, o, p = 2, 3, 4, 1

# string beolvasás és manipuláció \t -> tab, \n -> új sor (new line)
end = input("Wha? > ")
end += "\n"  # <end> végére konkatenáljuk az új sor karaktert
end = "\t" + end  # <end> elejére konkatenálunk egy tabot
# Ezt lehet egy sorban is. Hogyan?

# Paraméterezett print
print(a, b, c, d, sep="\t", end=end)
print(e, f, g, h, sep="\t", end=end)
print(i, j, k, l, sep="\t", end=end)
print(m, n, o, p, sep="\t", end=end)
