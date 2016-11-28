"""
Pythonban minden objektum.

Itt fel fogom sorolni pár beépített típusnak néhány
metódusát, ezeket valószínűleg fogod majd használni.
Illetve bemutatom majd a szótár adattípust.
"""

# STRING

# A stringek .split() metódusával feldarabolhatod a stringet
# az alábbi módon:

nagy_string = """Ez egy nagy string. Ennek a segítségével fogom
bemutatni a split() működését."""
# A splitnek átadhatsz egy argumentumot. A nagy stringet
# kisebb stringek listájává fogja alakítani, amiket a
# splitnek átadott argumentumban szereplő motívum
# mentén darabol fel.
szavak = nagy_string.split(" ")  # space mentén darabolunk
mondatok = nagy_string.split(". ")  # pont + space

# A .lower(), .upper() metódusokkal kisbetűsség, ill. nagybetűssé
# tehetsze egy stringet. A .capitalize minden kezdőbetűt
# nagybetűre alakít.
helytelen = nagy_string.lower()
orditva = nagy_string.upper()
furi = nagy_string.capitalize()
# Ne felejtsd el, hogy a lower, upper, capitalize és a split
# metódusok is VISSZATÉRNEK a módosított stringel, nem az
# eredetit alakítják át. Ha az eredetit akarod átalakítani,
# akkor felül kell definiálni a metódus kimenetével, például:
karomkodas = "AZT AZ ORGONASÍP MELLETT NEVELKEDETT KAJLAKUCSMÁS\n"
karomkodas += "DARUTOLLAS KUTYAÚRISTENIT A VILÁGNAK!"

# Felüldefiniálom
karomkodas = karomkodas.lower()

# A .format() nagyon hasznos metódusa a függvénynek, én rengeteget
# használom. A következőképpen működik:
nyers_mondat = "Ez egy {} metódus!"
print("Szabi mondja:", nyers_mondat.format("szar"))
print("Csabi mondja:", nyers_mondat.format("király"))
# A stringben lévő {} helyére beilleszti a megadott stringet vagy
# akár számot, komplett listát vagy tuple-t, stb.
# {}-ből több is szerepelhet egy stringben, ekkor mindegyikhez rendelni
# kell a .format-ban egy paramétert:
print("Szabi pontjai: {}/{}".format("tíz", 10))

# LISTA

lista = "Itt a farsang, áll a bál".split(" ")
lista.index("bál")  # megadja, hányadik elem a "bál"
lista.append("keringőzik")  # hozzáfűz egy elemet
lista.sort()  # helyben rendezés: nem tér vissza semmivel!

# A következő a join(), ami igazából a string metódusa, de
# mindig listával vagy tuple-lel használjuk:
ujra_string = " ".join(lista)

# ez összekapcsolja a paraméterként átadott lista vagy tuple
# vagy bármilyen iterálható adattípus elemeit az előtte
# megadott stringgel.
# Pl. a " ".join() space-ekkel választja el a lista elemeit.
# ";" pontosvesszővel, "\n" újsor-karakterrel, "\t" tabbal, stb.
# "" az üres string, ez simán összekapcsol mindent közvetlenül.

# TUPLE: lásd lista, de tuple-nél nincs append()! A tuple nem
# megváltoztatható.

# SZÓTÁR
# A szótár egy új adattípus, amivel még nem találkoztál.
# Ez kulcs - érték párokat tartalmaz rendezetlenül, például:
gyumolcsok_szinei = {"citrom": "sárga",
                     "alma": "piros",
                     "eper": "piros"}
# Bal oldalon a kulcsok, jobb oldalon az értékek vannak.
# Egy értéket lekérdezhetünk egy kulcs alapján:
print("A citrom {}.".format(gyumolcsok_szinei["citrom"], "színű"))

# A szótárat is be lehet járni, többféleképpen.
# A sima for + szótárnév a kulcsneveket járja be:
for kulcs in gyumolcsok_szinei:
    print("Kulcs: {}".format(kulcs))

# Ez nagyon fontos: a szótárak rendezetlenül tárolják az adatokat.
# ez azt jelenti, hogy hiába adod meg valamilyen sorrendben a kulcsokat,
# bejáráskor nem sorrendben jönnek vissza.

# Viszont több metódus is van, amivel másféleképpen is bejárhatóak:
# .keys() végeredmény szempontjából ugyanaz, mint a sima for.
# Igazából egy iterátort kapsz a kulcsokra.
# Az iterátor, ha nem emlékeznél:
# olyan, mint egy lista, de csak egyszer lehet bejárni.
for kulcs in gyumolcsok_szinei.keys():
    print("Kulcs iterátorral: {}".format(kulcs))

kulcsok_iterator = gyumolcsok_szinei.keys()
for kulcs in kulcsok_iterator:
    print("Kulcs iterátorral újra: {}".format(kulcs))

# A .values() az értékekre ad egy iterátort
for ertek in gyumolcsok_szinei.values():
    print("Érték: {}".format(ertek))

# Az .items() együtt kéri le a kulcsokat és az értékeket.
# Olyasmi, mintha zippelted volna őket:
for kulcs, ertek in gyumolcsok_szinei.items():
    print("Kulcs: érték -> {}: {}".format(kulcs, ertek))

# Új érték szótárhoz adása:
gyumolcsok_szinei["körte"] = "sárga"
print("A körte {}.".format(gyumolcsok_szinei["körte"]))

# Kulcsnak csak megváltoztathatatlan adattípust használhatsz:
# stringet, intet, floatot.
# használhatsz tuple-t is, de csak akkor, ha a tuple-ben csak
# megváltoztathatatlan adatok vannak.

# Üres szótárak:
ures1 = {}
ures2 = dict()

# Szótár létrehozása zip() objektumból:
emberek = ["Szabi", "Csabi", "Anyu", "Apu"]
iq = [-5, 220, 320, 420]
szotar = dict(zip(emberek, iq))
for nev in szotar:
    print("{} IQ-ja: {}".format(nev, szotar[nev]))
