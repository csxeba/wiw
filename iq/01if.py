# Egy pár szó a logikai elágazásról (if)
# A logikai elágazás a pythonban összetett utasítás, ami azt jelenti, hogy
# több soros is lehet. Ezt szerintem minden nyelvben így van (mármint hogy
# az IF több soros). Az ilyen összetett utasítások használatánál jelezni
# kell, hogy hol kezdődik egy utasítás-blokk és hol végződik.
# Ezt C/C++-ban, C#-ban, Java-ban pl. {} kapcsos zárójellel jelölik.
# Pythonban ezt behúzással jelöljük (tab)
# Mivel az összetett utasítások egymásba is ágyazhatóak (tehát ifen belül
# if, azon belül újabb if, stb.), ez jó nagy káoszhoz tud vezetni.

a = 1
b = 1.
c = "1"

# int, float és bool viszonya egymáshoz logikai kifejezésekben
print("-"*30)  # Dísznek
# (Figyeld a behúzást!)
if a == b:
    print("a == b: <a> implicit floattá konvertálódott")
    print("1. == 1. valóban")
    print("-"*30)

if a == c:
    print("This won't run")
    print("-"*30)

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
    print("A igaz bool értékké konvertálódott implicit módon.")
elif not a:
    print("Ez az ág nem fog futni, mert negáltuk az igazzá konvertálódott <a>-t")


igaz = True

if a == igaz:
    print("a == igaz: <a> bool-lá konvertálódik")
    print("True == True valóban")
    print("-"*30)

# Melyik ág fut? Miért?
if c == igaz:
    print("Fura. c == igaz értéke:", c == igaz)
    print("Miért van ez?")
    print("-"*30)
else:
    print("Fura. c == igaz értéke:", c == igaz)
    print("Miért van ez?")
    print("-"*30)

z = 0

if z == igaz:
    print("Természetesen ez nem fut, mivel a 0 igazsságértéke False")
elif not z:  # not kulcsszó a logikai kifejezés elejére kell, hogy kerüljön
    print("<z> implicitly gets casted to bool")
    print("not False is True valóban")
    print("-"*30)
else:
    print("This won't run because we entered the elif branch above")

if b > z:
    print("b > z: integers and floats can be compared")
    print("1. is greater than 0 valóban.")
    print("-"*30)

message = "I like beer. Mmmmm!!!"

if message > c:
    print("string > c: strings are compared alphabetically")
    print("Numbers are earlier in the alphabet than lettes")
    print("-"*30)

# Ez ekvivalens a következő (explicit) kifejezéssel:
# if bool(message):
# De a cast-olás implicit is megtörténik (a háttérben):
if message:
    print("<message> is implicitly converted to bool")
    print("The truth value of a non-empty string is True")
    print("-"*30)

dude = "WiW"

# Melyik ág fut le?
if dude == "WiW" or dude == "Csx":
    print("What's up with the dudes?")
    print("-" * 30)
if dude == "WiW" and dude == "Csx":
    print("What's up with the dudes?")
    print("-" * 30)

# FONTOS! Assertet mindig magadnak írsz. User inputot
# soha ne asserttel, hanem if-fel ellenőrizz!
dude = "Csx"
assert dude == "WiW", "Dude! <dude> is not WiW!"
