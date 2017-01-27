
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

az azon egész szám, a programnyelv szöveg,
a verzió szöveg, a paradigma is szöveg.

Töltsd fel adatokkal:
(Python, Java, Haskell, C++ legyen benne)
A paradigma o (objektumorientált),
f (funkcionális) vagy p (procedurális) lehet.
A verzio az aktuális legfrissebb verziója a programnak.
Van olyan nyelv, ahol nem egyértelmű, ott csak
válassz egyet. A verio és paradigma oszlopoknak
valószínűleg utána kell nézned.
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
        print("HIBA: Helytelen vagy hiányzó tábla?")
    else:
        print("OK: Tábla definiálva!")
    res = cur.fetchall()
    if len(res) < 4:
        print("HIBA: Túl kevés rekord!")
    elif len(res[0]) != 4:
        print("HIBA: Rosszul definiált tábla fejléc!")
    else:
        print("OK: Helyes implementáció!")
    conn.close()


def main():
    """Ide dolgozz!"""
    db = "hf01.db"
    resetdb(db)

    # Ide jön a kódod
    # DML parancsok után ne felejts el commit-olni!

    checkdb(db)

if __name__ == '__main__':
    main()
