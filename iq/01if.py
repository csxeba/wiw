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

a = 1
b = 1.
c = "1"

# (Figyeld a kettőspontot és a behúzást!)
if a == b:
    print("a == b: <a> implicit floattá konvertálódott")
    print("1. == 1. valóban")

if a == c:
    print("This won't run")

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
if a:
    print("Az <a> True értékké konvertálódott implicit módon.")
elif not a:
    print("Ez az ág nem fog futni, mert negáltuk az igazzá konvertálódott <a>-t")


igaz = True

if a == igaz:
    print("a == igaz: <a> bool-lá konvertálódik")
    print("True == True valóban")

# Az else ág akkor fut, ha az előtte lévő if nem futott le
# Melyik ág fut? MIÉRT?
if c == igaz:
    print("Fura. c == igaz értéke:", c == igaz)
    print("Miért van ez?")
else:
    print("Fura. c == igaz értéke:", c == igaz)
    print("Miért van ez?")

# Az elif ág akkor fut, ha az előtte lévő if (vagy elif) nem futott le.
# elif ágat akárhányat betehetsz, if és else csak 1-1 lehet.
z = 0
if z == igaz:
    print("Természetesen ez nem fut, mivel a 0 igazsságértéke False")
elif not z:  # not kulcsszó a logikai kifejezés elejére kell, hogy kerüljön
    print("<z> implicit konvertálódik False-ra")
    print("not False valóban True")
else:
    print("This won't run because we entered the elif branch above")

if b > z:
    print("b > z: egészek és törtek összehasonlíthatóak")
    print("1. valóban nagyobb, mint 0")

message = "Szeretem a sört. Mmmmm!!!"

if message > c:
    print("string > c: a stringek abc rend szerint kerülnek összehasonlításra")
    print("A számok konvencionálisan (és az ASCII és UTF-8 karaktertáblákban)")
    print("Előbb jönnek az abc-ben, mint a betűk.")

dude = "WiW"

# Melyik ág fut le?
if dude == "WiW" or dude == "Csx":
    print("What's up with the dudes?")
if dude == "WiW" and dude == "Csx":
    print("What's up with the dudes?")

# Az assert kulcsszó egy érdekes konstrukció. Önellenőrzésre használjuk, akkor,
# ha tudjuk, hogy egy adott változónak a programunk egy adott pontján egy bizonyos
# értéke kell, hogy legyen.
# Ha az assertnek átadott logikai feltétel False-ra értékelődik ki, akkor a program leáll
# hibával és kiírja a vessző utáni stringet üzenetként.
dude = "Csx"
assert dude == "WiW", "Dude! <dude> is not WiW!"
# FONTOS! Assertet mindig magadnak írsz. Pl. user inputot
# soha ne asserttel, hanem if-fel ellenőrizz!

# Néhány jó kis beépített függvény, amit if-eknél tutira használni kell majd:

print("<dude> a str példánya?", isinstance(dude, str))
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

# (a None típusa egyébként NoneType)

# Másik hasznos függvény: type()
# az adott érték típusát adja vissza

a, b = 2.7182, 3.1415

if type(a) == type(b):
    print("A két típus megegyezik")
    print("Az értékük nem, csak a típusuk!")
    print("a == b:", a == b)
else:
    print("Ez nem fut le, mert <a> és <b> is float :)")


# Egy utolsó hasznos függvény, a len()
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
    quit()  # leállunk, mert marhaság van


# Logikai műveletek:
a = 2
szoveg = "Sajt"

if a < 4 and szoveg == "Sajt":
    print("Az <and> a logikai és. Két feltétel közé írjuk.")
    print("Csak akkor értékelődik igazra, ha mindkét logikai feltétel igaz")

b = 0

if b or a:
    print("Ez megint implicit castolás boolra")
    print("Az <or> a logikai vagy")
    print("Akkor értékelődik igazra, ha egyik VAGY másik VAGY mindkét feltétel igaz")

if (0 < a < 10 and isinstance(a, int)) or (not b and szoveg == "Sajt"):
    print("Lehet ezt kombinálni szépen :)")
    print("Látható, hogy zárójelezni lehet. Érdemes is, mert")
    print("hamar megbonyolódhat a dolog.")

# Pythonban nagyon fontos, hogy átlásd a programodat, amit írsz.
# A nyelv egyik legnagyobb előnye pont az olvashatóság
# Csak képzelj el egy, az előzőhöz hasonló feltételrendszert.
# Utána képzeld el, hogy még van hozzá egy else: ág is...
# Az else-nél ki sem írod a feltételt, az megy oda, ami nem az if-be megy.
# Hosszú feltételsornál szinte átláthatatlan, hogy mi megy az else ágba...
# Ha nagyon bonyás, kiveheted a feltételrendszer elemeit változókba:
a_integer_es_0_10_kozott_van = (0 < a < 10) and isinstance(a, int)
b_hamis_es_szoveg_sajtot_tartalmaz = not b and szoveg == "Sajt"
# Itt nyilván bool értékek kerülnek a változókba.

# újraírva a fenti szörnyeteg:
if a_integer_es_0_10_kozott_van or b_hamis_es_szoveg_sajtot_tartalmaz:
    pass  # ez nyelvi kulcsszó, azt jelenti, "ne csinálj semmit" :)
