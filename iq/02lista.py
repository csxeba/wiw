# Összetett adattípusok azok, amelyek elemekként tartalmazhatnak más típusokat.
# Ezek arra valók, hogy dolgokat gyűjtsünk bennük :)

# ------------------
# Lista és indexelés
# ------------------

lista = ["1. elem", "2. elem", "3. elem", "4. elem", "5. elem(!)"]
# A bennük tárolt elemek típusa akármi lehet és keveredhetnek is
# ezt azért fontos megjegyezni, mert típusos nyelvekben,
# mint a C, C++, Java általában csak egyféle típus gyűjthető ezekben

# Egy lista eleme lekérhető a sorszáma alapján:
print(lista[0])  # ezt indexelésnek hívjuk. Az index 0-tól indul.

# Indexelhetünk hátulról is:
print(lista[-1])  # ez az utolsó elemet adja vissza

# És indexelhetjük a lista egy szeletét is:
# Ez egy kicsit bonyolultabb.
# A start:end szintaxisnál a start indexű elemet a Python beleveszi a lekérdezésbe
# az end indexű elemet pedig már nem veszi bele, itt tehát magyarul a 2.-4. elemig
# bezárólag kértük le az elemeket. Pythonul az 1. elemtől a 3. elemig történt a lekérés.
print(lista[1:4])
# Itt listaként kapjuk meg a végeredményt! Akkor is, ha csak 1 elemet szeletelünk ki!

# Mind a start, mind az end index opcionális:
print(lista[:3])  # az első 3 elemet kérjük le (a pythonul 3 indexű elemet már nem!)
print(lista[3:])  # a pythonul 4 indexű elemtől a végéig kérjük le
print(lista[-2:])  # az utolsó 2 elemet kérjük le
print(lista[:])  # minden elemet lekérünk (ez lemásolja a listát)
# Ha túlindexelsz előre vagy hátra, nem figyelmeztet, visszaad annyit, amennyit tud:
print(lista[4:1000])

# Még egy indexelési trükk:
print(lista[::2])  # A harmadik megadható szám a lépésköz, most minden második elemet kapjuk meg
print(lista[1::3])  # A második elemtől kezdve a végéig, hármasával :)
print(lista[-1:0:-2])  # Az utolsó elemtől a másodikig
# (ugye a nulladik már NEM :D) és hátrafelé kettes lépésekben :D

# És ez semmi, a szeletet megváltoztathatod, ha hozzárendelsz egy, a szelet méretének megfelelő
# elemszámű listát:
lista[1:5] = [0, 0, 0, 0]
print(lista)
# Ez persze a lépésközös konstrukcióval is ugyanígy működik
lista[1:-1:2] = [None, None]  # A második elemtől az utolsó előttiig
# minden második elem értékék beállítjuk
print(lista)

# Megjegyzés
# Ezek a brutál nyelvi konstrukciók, mint ez a szelet-indexelés hátrafelé kettesével
# azok, amik a Pythont nagyon király nyelvvé teszik. C/C++-ban van a tömb, annál
# pl. nincs szeletelés, csak egyesével tudsz elemeket indexelni benne
# és csak egyféle típus mehet bele, amit előre meg kell adnod, sőt az elemek számát is.
# Nyilván egy Python lista a memóriában hússzor akkora, mint egy C/C++ tömb és sokkal lassabb
# az indexelése is, ezt bukjuk a funkciók miatt. Persze vannak módszerek, ha sebesség kell :)

# Listához elemet adni pl. konkatenációval lehet:
lista = lista + ["6. elem O.o"]
# vagy
lista += ["7. elem ááááá"]
# Ennél van egy sokkal elegánsabb megoldás, de arról majd később.

# -------------------
# Tuple avagy sokaság
# -------------------

# Érdekes Pythonos listaszerűség, más programnyelvben nincs is ilyen
# Olyan mint a lista, de az elemeit nem lehet megváltoztatni.
tup = ("1. elem", "2. elem", "3. elem", "4. elem", "5. elem :)")
# Amikor definiáljuk, akkor a zárójel elhagyható:
tup2 = 1, 3.0, "valami string", None, False
# Magyarul sokaságnak vagy rendezett n-esnek (ennes) lehet fordítani
# ugyanúgy indexeljük, mint a listát.
print(tup2[2:5])

# Az elemei nem megváltoztathatóak:
lista[0] = "Másik valami izé"
# tup[0] = "Másik valami izé"  # hibát fog dobni
tup += ("Hello",)  # Ilyet lehet, mert ez új tuple-t hoz létre és helyettesíti az eredetivel

# Közbevágás:
# A stringek is indexelhetőek:
lanc = "Hello Szabi, mászol ki azonnal a routeremből?!"
print(lanc[5:10])
# Viszont a tuple-höz hasonlóan az elemei megváltoztathatatlanok:
# lanc[5] = "G"  # Ez hibát fog dobni

# tuple-t listává és vissza bármikor konvertálhatsz:
lista = list(tup)
tup2 = tuple(lista)
print(lista)
print(tup2)

# Stringet castolhatsz karakterek listájává:
karakterek = list(lanc)
print(karakterek)
# Ez vissza nem működik
vissza = str(karakterek)  # "szó szerint" lefordítja a listát egy stringgé
print(vissza)
# Ugyanez ugyanígy működik tuple-re is:
karakterek = tuple(lanc)
print(karakterek)

# Még annyi megjegyeznivaló van, hogy a listák, tuple-ök elemei lehetnek listák, tuple-ök is.
# Ezeket többdimenziós listáknak, tuple-öknek nevezzük.
# A tuple, bár nem megváltoztatható, de ha van benne lista, az a lista már megváltoztatható
mytup = (None, "asd", ["foo", "bar", "foobar"], ("hello", "bello"))
mytup[2][::2] = ["Sör", "Bor"]  # ez legális
mytup[3] += "mellow"  # ilyet is lehet

# -------
# Aliasok
# -------

# A változók kétféleképpen foghatóak fel:
# Egyszer olyanok, mint egy doboz, amibe beledobhatsz értékeket
# ugyanakkor a valóságban inkább egy mutatóhoz hasonlóak, amik a RAM
# egy területére mutatnak. Amikor létrehozol egy értéket és azt névhez
# (változóhoz) rendeled, akkor a változó rámutat arra a memóriaterületre,
# ahol az értéked van. Amikor mást "dobsz" a változóba, akkor átállításra
# kerül és onnantól másra mutat.
# Aliasnak azokat a változókat nevezzük, amik ugyanarra az értékre mutatnak:

lista1 = ["Hello", "Szabi", "te", "feketesapkás", "hacker"]
lista2 = lista1
print("lista1:", lista1)
print("lista2:", lista2)
lista1[3] = "rusnya"
print("lista1:", lista1)
print("lista2:", lista2)

# Ha lefuttatod ezt a kódrészt, nyilvánvaló lesz, mi az alias
# Megváltoztathatatlan típusoknál (int, float, bool, string, tuple)
# nincs aliasolás, ott lemásolódik az érték és újra létrejön a memóriában:

tup1 = ("Hello", "Ács", "Feri", "te", "pirosinges", "jampecológus")
tup2 = tup1
print("tup1:", tup1)
print("tup2:", tup2)
tup1 += ("hogy", "ennél", "kefét")
print("tup1:", tup1)
print("tup2:", tup2)

# Pár hasznos beépített függvény, amit használhatunk tuple és lista típusokon:

lista = [3, 4, 2, 1, 5]

print(sum(lista))  # szumma, inttel és floattal is működik (vegyesnél float lesz az eredmény)
print(sorted(lista))  # rendezi, visszatér egy rendezett másolattal
print(len(lista))  # mint length, azaz hossz, az elemek számával tér vissza
print(min(lista))
print(max(lista))  # minimum és maximum értékek

# Bemutatom az <in> kulcsszót:
print(2 in lista)  # nagyon hasznos, megvizsgálja, hogy egy adott érték eleme-e valaminek
# Természetesen működik tuple-re is, sőt stringre is (stringnél substringet is nézhetsz)
nagy_string = """A változók kétféleképpen foghatóak fel:
Egyszer olyanok, mint egy doboz, amibe beledobhatsz értékeket
ugyanakkor a valóságban inkább egy mutatóhoz hasonlóak, amik a RAM
egy területére mutatnak. Amikor létrehozol egy értéket és azt névhez
(változóhoz) rendeled, akkor a változó rámutat arra a memóriaterületre,
ahol az értéked van. Amikor mást "dobsz" a változóba, akkor átállításra
kerül és onnantól másra mutat.
Aliasnak azokat a változókat nevezzük, amik ugyanarra az értékre mutatnak"""
print("'RAM' in nagy_string:", "RAM" in nagy_string)
# csinálhatsz ilyesmikre if elágazásokat (érettségin tuti kell majd)
