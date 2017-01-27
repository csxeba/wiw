import sqlite3 as sql

# Így kezdünk neki a munkának:
# Kapcsolat létrehozása egy adatbázissal
conn = sql.connect("teszt.db")
# Első argumentumként az adatbázisfájl
# elérési útját várja. Ha nem adod meg neki,
# akkor az aktuális munkakönyvtárban keresi.
# Ha nem létezik a fájl, akkor létrehozza.

# Kurzort létrehozása a kapcsolaton belül
# A kurzoron keresztül tudunk parancsokat futtatni
# és a parancsok kimenetét is innen szedjük majd ki
cur = conn.cursor()
# Egy parancs futtatása a kurzoron keresztül
parancs = "SQL parancs ide stringként"
# cur.execute(parancs)  # kikommenteltem, mert hibát dobna

# Általános infók az SQL nyelvről:
# Először is ilyen nyelv nincs,
# különböző SQL implementációk vannak,
# mint az OracleSQL, MySQL, vagy az SQLite3
# Ezek mind eltérhetnek lehetnek, de nagy
# vonalakban azért hasonlítanak.
#
# Az SQL-ben a whitespace karaktereket (újsor,
# space, tab) figyelmen kívül hagyja a nyelv
# (nem úgy, mint a Python), így tetszőlegesen
# tördelhetőek a parancsok.
# Az SQL-ben a kisbetű-nagybetű közt
# nem teszünk különbséget (nem úgy, mint a Pythonban)
#
# Alapvetően gondolhatsz úgy az adatbázisokra, mint
# táblák gyűjteményére, amik között kapcsolatok lehetnek.
# A táblákban vannak oszlopok, ezeket attribútumoknak
# nevezzük. Ezek írják le a táblában lévő dolgok
# tulajdonságait.
# A sorokat rekordoknak nevezzük. Egy rekordot az
# attribútumokhoz rendelt értékek írnak le.
#
# Elméleti összefüggést fedezhetsz fel a Python osztályok
# és a táblák között. Egy tábla attribútumokat definiál.
# A Python osztályokban is attribútumokat definiálunk.
# (ezek lesznek az objektumok változói).
# Az osztályok metódusokat is definiálnak (ezek az
# objektumokhoz "kötött" függvények), ezeknek nincs
# SQL megfelelője. Az osztály példányai az objektumok.
# A tábla "példányai" a rekordok.
# Beszéltük, hogy az osztály olyan, mint egy tervrajz, ami
# alapján objektumokat hozunk létre.
# Hát a tábla definíció is egy tervrajz, ami alapján rekordokat
# tudunk felvenni.
# Az osztály definíció (attribútumok definíciója) gyakorlatilag
# megegyezik a tábla definícióval (oszlopfejléc definíciója)
#
# Az SQL három "alnyelvet" különböztet meg
# Kicsit szerencsétlen ezeket nyelvnek nevezni
# inkább parancsok három csoportjának hívnám
# őket.

#################################
#################################
# DDL, Data Definition Language #
#################################
#################################

# Az adatdefiníciós nyelv az adatbázis objektumok
# szintjén működik, táblákat hoz létre, módosítja
# a fejléceket, vagy egész táblákat töröl.
# Most csak táblákkal foglalkozunk, de táblákon
# kívül még vannak pl. INDEX, VIEW (nézet) objektumok is.

##############################################
# CREATE - ezzel a paranccsal létrehozhatunk #
# új adatbázis-objektumokat                  #
##############################################

create_parancs = """
CREATE TABLE felhasznalo (
    PRIMARY KEY azon INTEGER,
    nev VARCHAR(100) NOT NULL,
    kor INTEGER,
    regdatum DATE,
    aktiv BINARY DEFAULT TRUE);
"""

# Nézzük meg a parancs szerkezetét.
# Az SQL nyelv részeit, bár ez a futás szempontjából mindegy,
# de konvencionálisan csupa nagybetűvel írjuk.
# A "CREATE TABLE felhasznalo" azt jelenti, hogy egy táblát
# akarunk létrehozni "felhasznalo" néven, a felsorolt
# attribútumokkal. Látható, hogy az attribútum neve
# után meg kell adni az adattípust.
# A fenti SQL parancs hasonló, mint Pythonban a


class Felhasznalo:
    def __init__(self, azon, nev, kor=None, regdatum=None, aktiv=True):
        self.azon = azon
        self.nev = nev
        self.kor = kor
        self.regdatum = regdatum
        self.aktiv = aktiv

# A create-ben látható PRIMARY KEY (elsődleges kulcs)
# rész beállítja az "azon" INTEGER típusú változót,
# mint elsődleges kulcsot.
# Az elsődleges kulcs egy olyan oszlop, amiben csak egyedi
# értékek szerepelhetnek és kötelező megadni. Ilyet nem
# muszáj használni, de meggyorsítja a lekérdezéseket, ha
# kapcsolgatni kell a táblákat egymáshoz.
# Egyébként konvencionálisan mindig megadunk valamit
# elsődleges kulcsnak.
# A "nev VARCHAR(100) NOT NULL" sor annyit jelent, hogy
# a "nev", változó hosszúságú karakter (max 100)
# attribútum megadása új rekord hozzáadásakor kötelező.
# A "aktiv BINARY DEFAULT TRUE" rész az "aktiv" bináris (igen/nem)
# típusú változót apapértelmezetten TRUE értéknek állítja be.
# Ez annyit jelent, hogy ha később rekordot adunk a táblához,
# de nem adunk értéket az "aktiv" attribútumnak, az alapból TRUE
# értékkel kerül a táblába.
# A "kor", "regdatum" attribútumok megadása nem kötelező. Ha
# rekord hozzáadásakor nem adsz meg rájuk értéket, akkor az SQL
# speciális "NULL" értéket rendeli hozzájuk.
# A Python osztálynál ezt a None alapértelmezett érték megadásával
# állítjuk be.

############################################
# ALTER - ezzel a paranccsal módosíthatunk #
# meglévő adatbázis-objektumokat           #
############################################

alter_parancs = """
ALTER TABLE felhasznalo
    ALTER COLUMN nev VARCHAR(200);
"""

# Módosítjuk a "felhasznalo" tábla
# "nev" attribútumát.
# A régi VARCHAR(100) helyett most
# VARCHAR(200) a típusa.

#########################################
# DROP - ezzel a paranccsal törölhetünk #
# meglévő adatbázis-objektumokat        #
#########################################

drop_parancs = """
DROP TABLE felhasznalo;
"""

# Python-rész: futtassuk a fenti parancsokat
cur.execute(create_parancs)  # létrejön a tábla
cur.execute(alter_parancs)  # módosítjuk
# cur.execute(drop_parancs)  # majd törölhetjük

################################
# Itt a vége a DDL alnyelvnek. #
################################

###################################
###################################
# DML, Data Manipulation Language #
###################################
###################################

# Az adatmanipulációs nyelv segítségével rekordok szintjén
# végezhetünk műveleteket, beszúrhatunk táblába, törölhetünk
# rekordokat vagy módosíthatjuk őket.
# Fontos!
# A DML parancsokat nem elég kiadni. A módosítás, amit végzel,
# ideiglenesen tárolásra kerül és még egyszer jóvá kell hagynod,
# hogy bele is írodjon a fájlba.
# Ezt az SQL
# COMMIT parancsával lehet kivitelezni.
# Ez SQLite3 (Pythonos SQL) esetén SQL parancs helyett
# a Connection egy metódusa:

conn.commit()

# MS Access SQL-ben nincs COMMIT parancs egyáltalán.

##########################################
# INSERT - ezzel a paranccsal rekordokat #
# szúrhatunk egy táblába.                #
##########################################

insert_szabi_parancs = """
INSERT INTO felhasznalo
(azon, nev, kor) VALUES
(1, 'Szabi', 17);
"""

# SQL-ben a stringeket egyszeres aposztróffal jelöljük.

# Az "INSERT INTO felhasznalo" rész
# kijelöli, hogy melyik táblába szúrunk.
# Ezután zárójelben megadjuk, melyik attribútumokat
# állítjuk be és milyen sorrendben.
# A VALUES után pedig az előző sorrendnek megfelelően
# felsoroljuk az értékeket.
# Ezután létre fog jönni egy rekord a felhasznalo
# táblában a következő értékekkel:
# +----+-----+---+--------+-----+
# |azon|nev  |kor|regdatum|aktiv|
# +----+-----+---+--------+-----+
# |   1|Szabi| 17|    NULL| TRUE|
# +----+-----+---+--------+-----+

# Ha minden attribútumot feltöltünk és a CREATE során
# beállított sorrendben adjuk meg őket, akkor az első
# zárójeles része a kifejezésnek elhagyható:

insert_csabi_parancs = """
INSERT INTO felhasznalo VALUES
(2, 'Csabi', 27, '2017-01-01', FALSE);
"""

# A dátumokat a fenti formátumban beviheted.
# 'ÉÉÉÉ-HH-NN'

# +----+-----+---+--------+-----+
# |azon| nev |kor|regdatum|aktiv|
# +----+-----+---+--------+-----+
# |   1|Szabi| 17|    NULL| TRUE|
# |   2|Csabi| 27|20170101|FALSE|
# +----+-----+---+--------+-----+

# Első lecke vége :)
# Házi feladat:
# sql_01.py kata
