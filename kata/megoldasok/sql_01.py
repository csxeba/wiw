
"""
Csinálj egy adatbázis-fájlt hf01.db néven!
Csinálj egy táblát "nyelvek" néven
az alábbi formában SQL-ben:

+--------+
|nyelvek:|
+----+---+--------+------+---------+
|azon|programnyelv|verzio|paradigma|
+----+------------+------+---------+
|   1|      Python|   3.6|        p|
+----+------------+------+---------+

az azon egész szám és elsődleges kulcs,
a programnyelv szöveg, a verzió szöveg,
a paradigma is szöveg.

Töltsd fel adatokkal:
(Python, Java, Haskell, C++ legyen benne)
A paradigma o (objektumorientált),
f (funkcionális) vagy p (procedurális) lehet.
A verzio az aktuális legfrissebb verziója a programnak.
(Haskell esetén a GHC legújabb verziója)
Van olyan nyelv, ahol nem egyértelmű, ott csak
válassz egyet. A verio és paradigma oszlopoknak
valószínűleg utána kell nézned.

Ha kész vagy, küldd át az adatbázis-fájlt.
"""

import sqlite3 as sql


def resetdb(dbpath):
    """
    Kitörli a táblát.
    Ha ezt nem csinálod meg, akkor a script újrafuttatásakor
    hibát fog jelezni, hogy már létezik a <nyelvek> tábla.
    """
    conn = sql.connect(dbpath)
    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE nyelvek;")
    except:
        pass
    finally:
        conn.close()


def checkdb(dbpath):
    """
    Ha ez a függvény nem száll el, akkor jól csináltad.
    Argumentumként az adatbázisfájl elérési útját várja.
    """
    conn = sql.connect(dbpath)
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM nyelvek")
    except sql.OperationalError:
        print("HIBA: Hiányzó tábla!")
    else:
        print("OK: Tábla definiálva!")
    try:
        cur.execute("SELECT azon, programnyelv, verzio, paradigma FROM nyelvek")
    except:
        print("HIBA: Helytelen vtábla!")
    else:
        print("OK: Tábla fejléce jó!")
    res = cur.fetchall()
    if len(res) < 4:
        print("HIBA: Túl kevés rekord! ({})".format(len(res)))
    else:
        print("OK: Helyes implementáció!")
    conn.close()


def main():
    """Ide dolgozz!"""
    db = "hf01.db"
    resetdb(db)

    conn = sql.connect(db)
    cur = conn.cursor()

    cur.execute(
        "CREATE TABLE nyelvek (" +
        "azon INTEGER, " +
        "programnyelv VARCHAR(20), "
        "verzio VARCHAR(10), "
        "paradigma CHAR(1));")

    # Ronda megoldás:
    cur.execute("INSERT INTO nyelvek VALUES (1, 'Python', '3.6', 'p')")
    cur.execute("INSERT INTO nyelvek VALUES (1, 'Java', '8', 'o')")
    cur.execute("INSERT INTO nyelvek VALUES (1, 'Haskell', '8.0.2', 'f')")
    cur.execute("INSERT INTO nyelvek VALUES (1, 'C++', 'C++14', 'o')")
    conn.commit()

    # # Szebb megoldás (de nem tanultuk még):
    # data = ((1, "Python", "3.6", "p"),
    #         (2, "Java", "8", "o"),
    #         (3, "Haskell", "8.0.2", "f"),
    #         (4, "C++", "C++14", "o"))
    # for parameterek in data:
    #     cur.execute("INSERT INTO nyelvek VALUES (%, %, %, %)",
    #                 parameters=parameterek)

    checkdb(db)

if __name__ == '__main__':
    main()
