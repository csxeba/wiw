# Ehhez a részhez anyag a Swinnen könyvben: 30.-34. (3. fejezet)

# Egy pár szó a logikai elágazásról (if)
# A logikai elágazás a pythonban összetett utasítás, ami azt jelenti, hogy
# több soros is lehet. Ezt szerintem minden nyelvben így van (mármint hogy
# az IF több soros). Az ilyen összetett utasítások használatánál jelezni
# kell, hogy hol kezdődik és végződik egy kód-blokk.
# Ezt C/C++-ban, C#-ban, Java-ban, JavaScriptben pl. {} kapcsos zárójellel jelölik.
# Pythonban ezt a kezdő sor után kettősponttal, majd behúzással jelöljük (tab)
# Mivel az összetett utasítások egymásba is ágyazhatóak (tehát ifen belül
# if, azon belül újabb if, stb.), ez jó nagy káoszhoz tud vezetni és
# egytabos, kéttabos, stb. sok tabos behúzásokat fogsz majd látni.

egesz1 = 1
float1 = 1.
string1 = "1"

# (Figyeld a kettőspontot és a behúzást!)
if egesz1 == float1:
    print("egesz1 == float1:  az int implicit floattá konvertálódott")
    print("1. == 1. valóban")
# Behúzás vége, ez az alsó if már nem a fenti if része
if egesz1 == string1:
    print("Ez nem fog lefutni, az '1' string nem konvertálódik implicit")

# Összehasonlító operátorok:
# ==, <, <=, >, >=, magától értődőek.
# != a nem egyenlő
# Amit még fogsz használni: not kulcsszó:
if not False:
    print("A nem hamis az igaz :)")
# A not kulcsszó mindig egy logikai kifejezés elejére kerül.

# Adatok igazságértékéről pár szó:
# amikor valamit bool-lá castolsz, akkor azt mondjuk,
# hogy az adat igazságértékét kéred le.
# Konvenció alapján mindennek, ami nem 0, az igazságértéke True
# Ez minden programnyelven így van, nem csak Pythonban.
# Tehát ami nem igaz: 0, 0.0, "" (üres string) és majd még meglátod mik :)
# A speciális None érték igazságértéke is False
print(bool(None))

# Megjegyzendő, hogy az if implicit konvertál minden kifejezést bool-ra,
# amit átadsz neki.
# Pl. ezek teljesen érvényes konstrukciók:
if egesz1:
    print("Az <egesz1> True értékké konvertálódott implicit módon.")
elif not egesz1:
    print("Ez az ág nem fog futni, mert negáltuk az igazzá konvertálódott <egesz1>-et")


igaz = True

if egesz1 == igaz:
    print("egesz1 == igaz: <egesz1> bool-lá konvertálódik")
    print("True == True valóban")

# Az else ág akkor fut, ha az előtte lévő if nem futott le
# Melyik ág fut? MIÉRT?
if string1 == igaz:
    print("Fura. string1 == igaz értéke:", string1 == igaz)
    print("Miért van ez?")
else:
    print("Fura. string1 == igaz értéke:", string1 == igaz)
    print("Miért van ez?")

# Az elif ág akkor fut, ha az előtte lévő if (vagy elif) nem futott le.
# elif ágat akárhányat betehetsz, if és else csak 1-1 lehet.
egesz0 = 0
if egesz0 == igaz:
    print("Természetesen ez nem fut, mivel a 0 igazsságértéke False")
elif not egesz0:  # not kulcsszó a logikai kifejezés elejére kell, hogy kerüljön
    print("<egesz0> implicit konvertálódik False-ra")
    print("not False valóban True")
else:
    print("Ez az ág nem fut le, mivel feljebb beléptünk az elif ágba.")

if float1 > egesz0:
    print("float1 > egesz0: egészek és törtek összehasonlíthatóak")
    print("1. valóban nagyobb, mint 0")

message1 = "Aludni akarok"
message2 = "Zenét akarok hallgatni"

if message1 > message2:
    print("message1 > message2: a stringek abc rend szerint kerülnek összehasonlításra")

hacker = "Szabi"

# Melyik ág fut le?
if hacker == "Szabi" or hacker == "Csa":
    print("Most akkor ki a hacker?")
if hacker == "Szabi" and hacker == "Csa":
    print("Most akkor ki a hacker?")

# Az assert kulcsszó egy érdekes konstrukció. Önellenőrzésre használjuk, akkor,
# ha tudjuk, hogy egy adott változónak a programunk egy adott pontján egy bizonyos
# értéke kell, hogy legyen.
# Ha az assertnek átadott logikai feltétel False-ra értékelődik ki, akkor a program leáll
# hibával és kiírja a vessző utáni stringet üzenetként.
hacker = "Csa"
assert hacker == "Szabi", "Ember! Nem WiW a hacker!"
# FONTOS! Assertet mindig magadnak írsz. Pl. user inputot
# soha ne asserttel, hanem if-fel ellenőrizz!

ujszam = input("Add meg: 0 vagy 1? > ")

assert ujszam == "0" or ujszam == "1"  # Ilyet ne csinálj, az assert nem erre való
# A Python programokat le lehet fordítani byte-kódra, hogy gyorsabban fussanak
# Fordításkor átadhatsz egy -O paramétert, aminek hatására egy "optimalizált"
# byte-kódot kapsz. Ekkor kikerülnek pl. az assertek is a programodból!
# User inputot mindig egy if-fel ellenőrizz, esetleg ha rossz az input, akkor
# szakítsd meg a programot a quit() függvény hívásával és printelj valami hibaüzenetet.
# Ennek a procedúrának lesz majd egy elegáns megoldása, amit kivétel dobásnak hívnak,
# erről majd beszélünk. Egyébként így néz ki helyesen az ujszam ellenőrzése:
if ujszam != "0" or ujszam != "1":
    raise RuntimeError("Mondom NULLA vagy EGY, te szerencsétlen!")

# Ezt pótolhatod a következővel, ha nem akarod a raise-t használni még:
if ujszam != "0" or ujszam != "1":
    print("Mondom NULLA vagy EGY, te szerencsétlen!")
    quit()

# Néhány jó kis beépített függvény, amit if-eknél tutira használni kell majd:
print("<hacker> a str példánya?", isinstance(hacker, str))
# Az isinstance (példánya-e) azt ellenőrzi, hogy az átadott érték adott típusú-e.
# Mivel a Python dinamikusan típusos nyelv, sokszor kell ellenőrzini pl. változók
# típusát.

x = None

# Ezt élesben pl így használjuk majd:
if isinstance(x, str):
    x = int(x)
elif isinstance(x, float):
    x = round(x, 2)
elif isinstance(x, bool):
    x = float(x)
else:  # Ha a fentiek közül egyik sem:
    print("Nem támogatott típus!")
    quit()  # Leállunk, lehalasztjuk a programot
    # elegánsan: raise TypeError("Nem támogatott típus")

# (a None típusa egyébként NoneType)

# Másik hasznos függvény: type()
# az adott érték típusát adja vissza

e, pi = 2.7182, 3.1415

if type(e) == type(pi):
    print("A két típus megegyezik")
    print("Az értékük nem, csak a típusuk!")
    print("e == pi:", e == pi)
else:
    print("Ez nem fut le, mert <e> és <pi> is float :)")


# Még egy hasznos függvény, a len()
# az átadott érték hosszát adja vissza, ennek egyelőre stringeknél van értelme
szoveg = "Hello World"

if len(szoveg) < 200:
    print("Ez egy rövid szöveg")
elif 200 <= len(szoveg) < 1000:  # ilyet lehet :)
    print("Ez egy közepes szöveg")
elif len(szoveg) > 1000:
    print("Na ez egy hosszú szöveg")
else:
    print("Ez az ág sohasem fut le :) MIÉRT?")


# Logikai műveletek:
egesz1 = 2
szoveg = "Sajt"

if egesz1 < 4 and szoveg == "Sajt":
    print("Az <and> a logikai és. Két feltétel közé írjuk.")
    print("Csak akkor értékelődik igazra, ha mindkét logikai feltétel igaz")

float1 = 0

if float1 or egesz1:
    print("Ez megint implicit castolás boolra")
    print("Az <or> a logikai vagy")
    print("Akkor értékelődik igazra, ha egyik VAGY másik VAGY mindkét feltétel igaz")

if (0 < egesz1 < 10 and isinstance(egesz1, int)) or (not float1 and szoveg == "Sajt"):
    print("Lehet ezt kombinálni szépen :)")
    print("Látható, hogy zárójelezni lehet. Érdemes is, mert")
    print("hamar megbonyolódhat a dolog.")

# Pythonban nagyon fontos, hogy átlásd a programodat, amit írsz.
# A nyelv egyik legnagyobb előnye pont az olvashatóság
# Csak képzelj el egy, az előzőhöz hasonló feltételrendszert.
# Utána képzeld el, hogy még van hozzá egy else ág is...
# Az else-nél ki sem írod a feltételt, az megy oda, ami nem az if-be ment.
# Hosszú feltételsornál szinte átláthatatlan, hogy mi megy az else ágba...
# Ha nagyon bonyás, kiveheted a feltételrendszer elemeit változókba:
egesz1_integer_es_0_10_kozott_van = (0 < egesz1 < 10) and isinstance(egesz1, int)
float1_hamis_es_szoveg_sajtot_tartalmaz = not float1 and szoveg == "Sajt"
# Itt nyilván bool értékek kerülnek a változókba.

# újraírva a fenti szörnyeteg:
if egesz1_integer_es_0_10_kozott_van or float1_hamis_es_szoveg_sajtot_tartalmaz:
    pass  # ez nyelvi kulcsszó, azt jelenti, "ne csinálj semmit" :)

# Egy másik megközelítés egymásba ágyazni az ifeket:
if isinstance(egesz1, int):
    if 0 < egesz1 < 10:
        pass
elif not float1:
    if szoveg == "Sajt":
        pass

# Ez (ha minden igaz :D) ekvivalens a szörnyeteggel
# Feltételeknél elengedhetetlen a logikus gondolkodás,
# hogy mindig tudd, melyik változóban éppen mi van,
# ha azt "összeéseled" egy másikkal, akkor mi lesz,
# mi kerül az elifbe, mi kerül az else-be, stb stb.

# Ha idáig eljutottál az anyagban, akkor mostmár megcsinálhatod
# a <gondolatolvaso.py> és a <quiz.py> katákat.
