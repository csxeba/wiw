# Azt már korábban megbeszéltük, hogy mik a függvények,
# de ím egy kis emlékeztető:
# Egy Python függvény felépítése:
# f(arg1, arg2, arg3) -> visszatérési érték
# f a függvény neve, zárójelek közt az argumentumok (vagy paraméterek)
# listája és a függvény visszatér valamilyen értékkel.
# Az olyan függvényt, ami nem tér vissza értékkel (vagy None-nal tér vissza)
# eljárásnak vagy metódusnak nevezzük.

# Pythonban definiálhatunk saját magunknak is függvényeket:


def f():
    pass

# A függvények az ifhez és a ciklusokhoz hasonlóan összetett utasítások
# (kettőspont, behúzás)

# Miért írna valaki függvényt? Ennek alapvetően két oka lehet:
# Egyrészt ismétlődő kódrészeket kiemelhetsz a kódodból
# Másrészt strukturálhatod a kódodat, hogy átláthatóbb legyen.

# Az f() függvény (illetve eljárás) pont azt a minimális mennyiségű
# információt tartalmazza, amennyit meg kell adni, hogy létrehozhass
# egy függvényt: függvénynév (f) argumentumlista () ami jelenleg üres és
# minimum 1 sornyi utasítás (pass)

# Lássuk milyen egyéb (opcionális) részei lehetnek egy függvénynek.
# Megpróbálom gyakorlatban is szemléltetni

# Pl. vegyük a <kviz.py> katát. Ott volt ismétlődő rész:

# kérdés string definiálása
# kérdés string átadása az input()-nak promptként, válasz bekérése
# pontszám meghatározása, kiíratás, egyéb sallangok

# Ez a blokk annyiszor megismétlődött, ahány kérdést feltettünk


def kerdes(prompt, helyes):
    valasz = int(input(prompt))
    if valasz == helyes:
        print("Helyes válasz!")
        return 1
    else:
        print("Helytelen válasz!")
        return 0


k1 = """\t1.kérdés:\tHogy hívják a vak akkumulátort?
1) aksi
2) kaksi
3) vaksi
"""
k2 = """\t2. kérdés\tMi a címe a hackeres sorozatnak, amit ajánlottam?
1) Walter Mitty különös élete
2) Mr. Robot
3) Pentatronix
"""
k3 = """\t3. kérdés (a mindent eldöntő)\tMikor kezdünk már programozni?
1) Majd
2) Ha betöltötted a 18-at, kisfiam
3) Már most is ezerrel azt csináljuk
"""
kerdesek = [k1, k2, k3]  # Definiáljuk a kérdések listáját
valaszok = [3, 2, 2]  # Definiáljuk a változók listáját
pontok = 0  # deklarálunk egy változót, ebbe gyűjtük a pontokat
for kerd, val in zip(kerdesek, valaszok):
    pontok += kerdes(prompt=kerd, helyes=val)

# Ez az info lehet, hogy sok volt egyszerre, de szedjük szét!
# Mi történik?
# 1. Definiáltunk egy függvényt és leírtuk, mit csinál
#    Ez önmagában semmit nem fog eredményezni, a függvényben lévő
#    kód nem fut le, csak akkor, ha mi hívjuk a függvényt a
#    függvénynév(argumentumok...) módszerrel
# 2. definiáltunk egy kérdéssort és a hozzá tartozó válaszokat
# 3. deklaráltunk egy pontok változót, amibe a pontokat gyűjtük
# 4. zippeljük a kérdéseket és a válaszokat, így minden kérdés
#    párba kerül a neki megfelelő válasszal
# 5. lefuttatunk egy for ciklust, minden kérdésen végigszaladunk
#    prompt argumentumként átadjuk a kérdés szövegét a függvénynek
#    helyes argumentumként átadjuk a helyes választ sorszámát
# 6. A függvény bekéri a választ, promptként kiírja a megadott
#    stringet, majd integerré alakítja a beírt választ.
# 7. Az itegerre alakított választ összehasonlítja a megadott
#    helyessel. Kiírunk dolgokat...
# 8. Visszatér a függvény egy értékkel (return utasítás)
#    helyes válasz esetén nyilván 1-essel, amúgy nullával.
# 9. A visszatérési értéket "elkapjuk" és megnöveljük vele a
#    pontok változó értékét.

# Hogy gyakoroljuk a listaépítést (list comp), ezt értelmezd :D
besuvasztva = sum([kerdes(kerd, val) for kerd, val in zip(kerdesek, valaszok)])
assert besuvasztva == pontok, "Hopsz :S"


# Szóval adhatunk meg argumentumokat is függvényeknél
# Argumentumok lehetnek opcionálisak is, ha adunk nekik
# default értéket:

def bekero(prompt="> "):
    return input(prompt)

val = bekero()
val2 = bekero("Simon mondja: ")
# Az, hogy nevesíted-e az argumentumot, a második esetben mindegy
# A függvényhívás így is működik: bekero(prompt="Simon mondja: ")

# Van viszont egy fontos szabály:
# Az opcionális argumentumok mindig a kötelezőek mögött kell, hogy elhelyezkedjenek
# Tehát ez pl. illegális:
# def kerdes(prompt="> ", helyes):

# másik fontos dolog, hogy ha egy függvényen belül deklarálsz egy nevet (változót),
# akkor az a változó a függvényen kívül nem fog létezni.
# Az ilyeneket lokális változóknak hívjuk.
# Azonban a függvényen kívül deklarált változókra a függvényen belül hivatkozhatsz,
# de csak olvashatsz belőlük, írni nem írhatod őket.
# a "külső" változókat globális változóknak nevezzük, a "külsőt" és a "belsőt" pedig
# globális és lokális névtérnek.

# globális és lokális változónak lehet ugyanaz a neve, de nem ajánlott, mert
# káoszhoz vezethet...
# Ha mégis ugyanaz lenne egy globális és egy lokális név, akkor függvényen belül
# mindig a lokális változó lesz használatba véve. Ha nincs lokálisan definiálva
# egy név, akkor a program körülnéz a külső névtérben

x = "Globális string"


def local_hacker():
    x = "Lokális string"
    print(x)


def global_hacker():
    print(x)


local_hacker()
global_hacker()

# Van egy olyan része a Python függvényeknek, hogy docstring vagy dokumentációs
# string, amiben leírhatod, hogy egy függvény mit csinál:


def kt(r):
    """Kiszámolja adott sugarú kör területét"""
    return r * 3.1415

# Van egy programozó barátom, aki a "tiszta kód" vezérelv szerint programozik.
# Ő azt mondja, ha már docstringet és kommentet kell írnod arról, hogy mit
# csinál egy függvény, akkor szarul programozol.
# Azt mondja, nevezd el úgy a függvényt, hogy érthető legyen, mit csinál :)
# tehát a fenti újra:

del kt  # ne is lássam


def kor_terulete(sugar):
    pi = 3.1415
    return sugar * pi

# Persze az ilyeneket nem kell nagyon komolyan venni, úgy programozz, ahogy
# neked a legkényelmesebb, leghatékonyabb, mert azért ha gyakran használsz
# egy függvényt, akkor az ötkilométer hosszú függvénynevet begépelni nem
# túl kellemes minden alkalommal.
# Bár függvénynevet is lehet aliasolni, de az rontja a program olvashatóságát

kt = kor_terulete  # itt nincs függvényhívás jel ()
# Csak a nevet kötjük egy másik névhez

assert kt(10) == kor_terulete(10)
assert kt is kor_terulete  # azonosságot ellenőrzünk

# Függvény hívhat másik függvényt:


def henger_terfogata(atmero, magassag):
    alapkor_terulete = kor_terulete(atmero / 2)
    return alapkor_terulete * magassag


# Na most viszont, hogy tudsz függvényeket írni, szemléletet váltunk:
# Többet ne írj semmilyen utasítást függvényen kívülre.
# Két dolog lehet függvényen kívül (most):
# globális változó deklarációja, ha szükséges (de ez általában kiváltható
# paraméterek passzolgatásával)
# a fő függvényed hívása :D
