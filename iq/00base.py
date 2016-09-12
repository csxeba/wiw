# Ez komment

# Adattípusok, változó deklaráció
a = 2  # integer, vagy egész szám
b = 2.  # float, vagy lebegőpontos szám
# floatokról annyit kell tudni, hogy korlátozott a pontosságuk
# a 64 biten tárolt float 15-17 tizedesjegyig pontos, ezt
# double-nek is hívják pl. C/C++-ban (dupla pontosságú)
igaz = True  # bool, vagy igazság-érték, lehet True és False

# Kiíratás -> műveletek különböző adattípusokkal
print(a + b)  # 4.0  (mert <b> float)
print(a + a)  # 4    (mert <a> int)
print(a + igaz)  # 3    (ilyet is szabad)
print(b + igaz)  # 3.0  (sőt, ilyet is)

c = "2"  # ez string, vagy karakterlánc
c += "_"  # összeadás és változó-hozzárendelés egyben
print(c)  # c értéke itt "2_"
# Stringeknél két string összeadását konkatenációnak nevezzük

print(c * 2)  # 2_2_ (stringet szorozhatsz egésszel)
c *= 2  # ez konstrukció szorzással is működik
# tehát megszorzod 2-vel a c értékét, majd eltárolod c-ben az eredményt.
print(c)

# A művelettel egybekötött értékadást legtöbször egy számláló növelésére használjuk:
a = 1
a += 1  # növeli a értékét 1-gyel, 2-re.
a += 1
a += 1  # stb stb stb
# Ez a kiterjesztett értékadás minden művelettel használható.
b = 13
# a műveleti jeleket a programozásban operátoroknak nevezzük
# Pythonban az alábbi operátorok léteznek:
print(a + b)  # összeadás, blabla, ezek magától értődők
print(a - b)
print(a * b)
print(b / a)  # valódi osztás, mindig float-ot ad eredményül
# Egészrész-osztás, int-et ad eredményül.
print(b // a)  # Nem kerekít, hanem levágja a törtrészt
# Modulo operátor, elvégzi az osztást és nem az eredményt,
print(b % a)  # hanem a maradékot adja vissza

# del kulcsszó változó(k) törlésére
# ennek nagy programoknál lehet jelentőssége, ha memóriát akarsz felszabadítani
del a, b, c, igaz

# többszörös értékadás
a = b = 1  # ilyet is lehet, bár én nem ajánlom, majd később meglátod, miért

# Valamicskét a kiíratásról:
# Pythonban a print() függvénnyel íratunk ki.
print(a)
# A print függvénynek több (névtelen) argumentuma is lehet:
print("a:", a, "b:", b)
# Van két nevesített (vagy kulcsszó-) argumentuma is:
# sep a szeparátor karakter(lánc), amit a vesszők helyére betesz.
print("a:", a, "b:", b, sep="\t")  # tabot adtam meg (alapból szóköz " ")
# end a legvégéhez ad hozzá:
print("a:", a, end=" ")  # szóközt adtam meg (alapból újsor-karakter lenne "\n")
print("b:", b, end=" ")
print()  # üres print, hogy új sort kezdjünk
# Az üres print azért kezd új sort, mert az end kulcsszó-argumentum default értéke "\n"


# többszörös párhuzamos értékadás
a, b, c, d = 1, 2, 3, 4
e, f, g, h = 4, 1, 2, 3
i, j, k, l = 3, 4, 1, 2
m, n, o, p = 2, 3, 4, 1

# string beolvasás
end = input(prompt="Wha? > ")  # input függvénnyel kérhetsz a usertől bemenetet.
# Az input függvénynek egy argumentuma van, a prompt.
# Úgy működik, hogy kiírja a promptot, majd vár, míg be nem írsz valamit és entert
# nem ütsz. Utána visszaadja !stringként! azt, amit a user beírt. A számot is
# stringként adja vissza.

# Kis string manipuláció:
end += "\n"  # <end> végére konkatenáljuk az új sor karaktert
end = "\t" + end  # <end> elejére konkatenálunk egy tabot

# A fenti két utasítás egy sorban is felírható. Hogyan?

# A fenti három utasítás egy sorban is felírható :D Hogyan?

# Paraméterezett print, tabokkal elválasztott táblázatként
# kiíratjuk ezt a sok marhaságot. A végére kerül a user input.
print(a, b, c, d, sep="\t", end=end)
print(e, f, g, h, sep="\t", end=end)
print(i, j, k, l, sep="\t", end=end)
print(m, n, o, p, sep="\t", end=end)
