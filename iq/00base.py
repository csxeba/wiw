# Ez komment

# -------------------------------
# Adattípusok, változó deklaráció
# -------------------------------

a = 2  # integer, vagy egész szám
b = 2.  # float, vagy lebegőpontos szám
# floatokról annyit kell tudni, hogy korlátozott a pontosságuk
# a 64 biten tárolt float 15-17 tizedesjegyig pontos, ezt
# double-nek is hívják pl. C/C++-ban (dupla pontosságú)
igaz = True  # bool, vagy igazság-érték, lehet True és False

# -------------------
# Kiíratás, műveletek
# -------------------
print(a + b)  # 4.0  (<b> float, <a> is floattá konvertálódik, így elvégezhető a művelet)
print(a + a)  # 4    (<a> int, két inttel elvéhezhető a művelet)
print(a + igaz)  # 3    (A bool konvertálódik intté. A True intként 1, a False intként 0)
print(b + igaz)  # 3.0  (Hasonlóan az előzőhöz. A True floatként 1.0, a False 0.0)

c = "2"  # ez a string, vagy karakterlánc
c += "_"  # összeadás és változó-hozzárendelés egyben
print(c)  # c értéke itt "2_"
# Stringeknél két string "összeadását" konkatenációnak nevezzük

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
# a műveleti jeleket a programozásban operátoroknak nevezzük
# Pythonban az alábbi operátorok léteznek:
b = 13

# ----------
# Operátorok
# ----------

print(a + b)  # összeadás, blabla, ezek magától értődők
print(a - b)
print(a * b)
print(b / a)  # valódi osztás, mindig float-ot ad eredményül,
# akkor is, ha inteket osztasz egymással.

# Egészrész-osztás, mindig int-et ad eredményül.
print(b // a)  # Nem kerekít, hanem levágja a törtrészt
# Modulo operátor, elvégzi az osztást és nem az eredményt,
print(b % a)  # hanem a maradékot adja vissza
# Ezeket általában együtt használjuk:
egeszresz = b // a
maradek = b % a

# ------------
# del kulcsszó
# ------------

del a, b, c, igaz, maradek, egeszresz
# törli a megadott változó(ka)t
# ennek nagy programoknál lehet jelentőssége,
# ha memóriát akarsz felszabadítani

# -------------
# Függvényhívás
# -------------

# Írok pár szót a függvényekről, mert most már fogunk olyanokat használni.
# Matematikai szempontból a függvény valami, aminek átadsz egy vagy több
# valamit és visszaad egy valamit.
# Így jelöljük: függvény(valami1, valami2, ...) -> vissza_valami
# A "vissza_valami"-t elkaphatod egy változóval:
# változó = függvény(valami1, valami2, ...)

# Amiket átadunk, azokat argumentumoknak vagy paramétereknek nevezzük.
# Ami kijön, az a visszatérési érték.

# Programozásban még olyan függvényekkel is találkozunk, amiknek nincs
# visszatérési értéke, csak átadsz neki argumentumokat (vagy nem adsz neki semmit)
# valamit csinál, és nem tér vissza semmivel.
# A valódi visszatérési értékkel rendelkező függvényeket nevezzük függvényeknek,
# azokat, amiknek nincs visszatérési értéke, metódusoknak vagy eljárásoknak.

# A print() egy eljárás, nem tér vissza semmivel (illetve visszatér egy None értékkel)
# A következőképpen néz ki az argumentumlistája:
# print(*objects, sep=" ", end="\n", file=None, flush=None)
# Mit jelent ez?
# Huh bonyolult. Nézzünk meg egy egyszerűbbet :D
# A printre majd visszatérünk.

# Az input() egy valódi függvény, a usertől lehet bemenetet kérni vele.
# Így néz ki az argumentumlistája:
# input(prompt)
# Úgy működik, hogy kiírja a promptot, majd vár, míg be nem írsz valamit és entert
# nem ütsz. Utána !stringként! visszatér azzal, amit a user beírt. (A számot is
# stringként adja vissza.)

# Egy függvény hívásakor az argumentumokat sorban átadhatjuk, vagy nevesíthetjük is
# input("> ") ugyanaz, mint
# input(prompt="> ")
# A nevesíthető argumentumokat kulcsszó-argumentumnak is hívjuk. Gyakran rövidítik
# kw vagy kwargként, az anonim argumentumokat arg/args-nak szokták rövidíteni.

# Na vissza a printhez, elsőre egyszerűbb megközelítéssel:
print(a)
# A print eljárásnak több (névtelen) argumentuma is lehet:
print("a:", a, "b:", b)
# Van pár nevesített (vagy kulcsszó-) argumentuma is:
# sep a szeparátor karakter(lánc), amit a vesszők helyére betesz.
print("a:", a, "b:", b, sep="\t")  # tabot adtam meg (alapból szóköz " ")
# end a legvégéhez ad hozzá:
print("a:", a, end=" ")  # szóközt adtam meg (alapból újsor-karakter lenne "\n")
print("b:", b, end=" ")
print()  # üres print, hogy új sort kezdjünk
# Az üres print azért kezd új sort, mert az end kulcsszó-argumentum default értéke "\n"

# Látható, hogy az inputtal ellentétben a kulcsszó-argumentumok csak explicit megnevezés
# útján érhetőek el, mivel


# --------------------
# Többszörös értékadás
# --------------------

a = b = 1  # ilyet is lehet, bár én nem ajánlom, majd később meglátod, miért
del a, b

# Ez a forma jobb, ha már tömöríteni akar az ember
a, b, c, d = 1, 2, 3, 4
e, f, g, h = 4, 1, 2, 3
i, j, k, l = 3, 4, 1, 2
m, n, o, p = 2, 3, 4, 1

# --------------------
# String beolvasás
# --------------------
end = input(prompt="Mi van? > ")  # input függvénnyel kérhetsz a usertől bemenetet.

# String manipuláció:
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

# --------------------------
# Castolás avagy konvertálás
# --------------------------

# ez sokszor implicit megtörténik (pl felül a print automatikusan konvertálja
# a számokat stringekké és azokat írja ki.
# intet probléma nélkül castolhatsz float-ra:
a = 1
float_a = float(a)
print(float_a)
# ha float-ot castolsz int-re, akkor kerekítés történik:
a = 1.5
int_a = int(a)
print(int_a)

# stringre castolni bármit lehet probléma nélkül, simán megkapod a string reprezentációt:
print(str(float_a))
print(str(int_a))
# De ugye azt írtam feljebb, hogy a print() implicit (automatikusan) is elvégzi ezt a
# konverziót, így ugyanazt az eredményt kapod, mintha simán átadtán neki nyersen a számokat.

# Ez is érdekes:
igaz = True
print(igaz)  # történik implicit konverzió
print(str(igaz))  # itt explicit konvertálunk
# A True-t is implicit konvertálja a print() és kapsz egy "True" stringet

# --------------
# Round függvény
# --------------

# Egyébként float-ot tudsz tetszőleges tizedesjegyre kerekíteni a round() függvénnyel, ekkor
# nem intet kapsz vissza, hanem kerekítve kapod meg a floatodat.
# A roundnak két argumentuma van: number és ndigits. A numbert kötelező megadni,
# az ndigits-nek van default értéke, ami None. Ha defaulton hagyod, akkor egészre kerekít,
# de akkot is float-ot kapsz vissza és nem intet.
a = 3.33333
a = round(number=a, ndigits=2)
print(a, end=" Hello Szabi\n")
# A fenti 3 utasítás egy sorban :)
print(round(3.33333, 2), end=" Hello Szabi\n")

# Stringeket is lehet számokká konvertálni, ez főleg akkor hasznos, ha
# input()-tal bekérsz valamit. Az input() mindig stringet ad vissza,
# azt pedig vissza kell alakítani számmá.
# Ha a konverzió elvégezhető, akkor semmi probléma, viszont egyes eseteket
# (pl. Troll Szabolcs szöveget ír be számok helyett) szükséges lehet kezelni
# Próbáld ki, törd el az inputot:
szabi_mond_egy_szamot = input("Na milyen számot mond Szabi?\n> ")
x = float(szabi_mond_egy_szamot)

# A trollok kikerülését majd megtanítom.
