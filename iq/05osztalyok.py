# Végre elértünk az osztályokig
# És újabb szemléletváltás következik, az eddigi
# procedurális/funkcionális paradigmáról átállunk
# az objektum-orientált paradigmára.

# <filozófiai rész>
# Mi a programozás? Végül is az információt reprezentáltuk
# eddig is: adatnak hívott konstrukciókon hajtottunk
# végre utasításokat, algoritmusokat.
# Az objektum-orientált (OO) szemlélet annyival viszi ezt
# tovább, hogy azt mondja:
# A világban objektumok vannak. Az objektumoknak vannak
# tulajdonságaik, amiket leírhatunk adatokként és
# csinálnak dolgokat, ezeket leírhatjuk függvényekként.

# A világ objektumait osztályohatjuk, ha pl. egy kalap alá
# vesszük a hasonlóakat:
# Tátog, beszél hülyeségeket, járkál össze-vissza: ez az
# Ember osztály egy objektuma, illetve az Ember osztály
# egy példánya (isintance(Szabi, Ember))
# Ezt az osztály-definiálást nevezzük általánosításnak, vagy
# absztrakciónak.

# Pythonban az osztályokat a következő szintaxissal definiáljuk:


class Osztaly:
    pass

# Ez a minimális szintaxis, ami egy osztály létrehozásához kell.
# A class kulcsszó jelzi, hogy osztályt fogunk definiálni.
# Az osztályok nevét konvencionálisan nagy betűvel kezdjük.
# A kettőspont, behúzásból már láthatod, hogy ez egy összetett utasítás.
# A pass helyére jön majd a kód.

# Elsőre úgy tűnhet, hogy az osztályok a függvényekhez hasonlítanak, de
# ne ess ebbe a tévképzetbe, anno nekem is nehéz volt különbséget tenni,
# de én egész másképp szeretném bemutatni az osztályokat, mint anno én
# ahogy találkoztam velük.
# Az osztályok arra valók, hogy beléjük csomagoljunk dolgokat, egészen
# pontosan adatokat (változókat) és függvényeket.

# Az adat-változókat osztályokban attribútumoknak hívjük, a függvényeket
# pedig metódusoknak.

# A fent definiált osztály semmire nem jó, nézzünk egy konkrétabb példát:


class Henger:
    def __init__(self, d, h):
        self.sarkok = 0
        self.alapkorok = 2
        self.atmero = d
        self.magassag = h

    def terfogat(self):
        return (self.atmero / 2) * self.magassag

# Az __init__ építi fel az objektumokat, amiket az osztályból csinálunk.
# Figyeld az absztrakciót:
# minden hengernek 0 sarka és 2 alapköre van, ez egy általános igazság.
# minden henger objektumnak van valamekkora átmérője és magassága is.
# A konkrét hengereknél ez egy adott szám, de a Henger osztálynak ez csak
# egy (absztrakt) attribútuma. Minden konkrét henger objektumnak
# van térfogata is, amit mindegyiknél ugyanúgy számítunk ki. Tehát van
# egy metódusunk, ami absztrahálható és osztályba emelhető.

# Az __init__-et mindjárt elmagyarázom, de most hozzunk létre egy
# konkrét henger objektumot az osztályból (példányosítjuk az osztályt)

hengerke = Henger(d=1, h=4)  # Nem kötelező kiírni az argumentumnevet

# Példányosításkor az __init__() metódus fut le, ezt hívjuk az osztály
# konstruktorának, ez vezényli le az "objektumépítést".
# A Henger() hívásakor igazából a konstruktort hívjuk és a konstruktornak
# az átadott argumentumokat is a konstruktor kapja.
# Az __init__() első argumentuma, a "self" speciális szereppel bír:
# visszamutat az éppen készülő objektumra (__init__ esetén).
# Amikor azt látod a konstruktorban, hogy self.sarkok = 0, az azt jelenti,
# hogy a készülő objektum kap egy sarkok nevű attribútumot, aminek az értékét
# 0-ra állítjuk.
# A self.atmero = d pedig azt jelenti, hogy az objektum kap egy atmero
# nevű attribútumot, aminek az értékét a paraméterként kapott d értékére
# állítjuk.
# Az __init__ végén, bár ez nincs odaírva, de gyakorlatilag van egy
# return self utasítás, az elkészült objektummal ugyanis visszatér, amit
# elkaphatunk egy változóba (hengerke)

# Az elkészült objektum attribútumaihoz hozzáférhetünk a következőképpen:

print("hengerke magassága:", hengerke.magassag)
print("hengerke alapkörei:", hengerke.alapkorok)

# Hengerkének definiáltunk egy metódust is, a terfogat()-ot
# A self itt is ugyanazt a szerepet tölti be, arra az objektumra
# hivatkozik vissza, amelyik hívja őt:

tf = hengerke.terfogat()
print(tf)

# Egy objektum metódusának hívásakor maga az objektum kerül be a
# self változóba. Pythonban ezt a visszahivatkozást konvencionálisan
# selfnek szoktuk nevezni, de amúgy bármit használhatsz, nem a neve
# a lényeges, hanem az, hogy ez az első helyen álló argumentum.
# Az objektum attribútumaihoz, illetve más metódusaihoz a self-en
# keresztül tudsz hozzáférni a metóduson belül.

# Nézzünk egy másik példát:


class Harcos:
    def __init__(self, nev, sebzes, tamadas, vedekezes):
        self.nev = nev
        self.sebzes = sebzes
        self.tamadas = tamadas
        self.vedekezes = vedekezes
        self.eletero = 100

    def tamad(self, masik):
        tamado_ertek = self.tamadas + 30
        if tamado_ertek > masik.vedekezes:
            masik.eletero -= self.sebzes
            print("Találat!")
            print(self.nev, "megsebezte", masik.nev + "-t")
        else:
            print(self.nev, "melléütött.")
        if masik.eletero <= 0:
            masik.eletero = 0
            print("Az ellenfél harcképtelen!")

# Harcosok nevei:
nevek = "Ork", "Amazon", "Elf"
# Sebzéseik:
sebz = 14, 12, 10
# Támadásuk:
tam = 30, 20, 40
# Védekezésük:
ved = 50, 65, 50

# 3 harcos objektumunk lesz:
ork, amazon, elf = [Harcos(n, s, t, v) for n, s, t, v in zip(nevek, sebz, tam, ved)]


def harc(harcos1, harcos2):
    kor = 1
    print(harcos1.nev, "vs.", harcos2.nev)
    while harcos1.eletero * harcos2.eletero != 0:
        print(str(kor) + ". harci kör!")
        harcos1.tamad(harcos2)
        harcos2.tamad(harcos1)
    harcos1.eletero = 100
    harcos2.eletero = 100


harc(ork, amazon)
harc(amazon, elf)
harc(ork, elf)

# Persze ha nagyon objektum-orientálódni akarnánk, akkor azt is mondhatnád, hogy
# ez a küzdelem végül is absztrahálható :D valahány harcos harcol egymás ellen egy
# harc() metódus szerint, ami mindig ugyanaz...
# Tehát a Kuzdelem osztálynak van egy harcosok attribútuma, ami harcos objektumok
# listája :D A harc() pedig a Kuzdelem osztály egy metódusa :D

# TODO: objektumok, mint osztályok attribútumai
# TODO: minden objektum!
# TODO: leszármazás? abc?
# TODO: katát írni!
