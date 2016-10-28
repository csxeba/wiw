# Definiáld egy táblázat fejlécét, 4 oszlopnevet
# kér be 5 rekordot! Mind a 4 oszlopba kérj be adatot!

# Legyen egyértelmű a bekéréskor, hogy mikor melyik
# oszlopba kell adat.
# Legyen egyértelmű, mikor hányadik rekordot írom.

# Ha megvan minden bevitt adat, írd ki a táblázatot!
# a rekordokat válaszd el így: ---------------------
# az oszlopokat pedig pipe | jellel.

# nem lesz szép, de vicces lesz :D

szeparator = "\t|\t"
fejlec = "id" + szeparator + "nevek" + szeparator + "varosok"
vonal = "-" * 50

rekord1nev = input("Add meg az 1. rekordhoz a nevet! > ")
rekord1varos = input("Add meg az 1. rekordhoz a várost! > ")

rekord2nev = input("Add meg az 2. rekordhoz a nevet! > ")
rekord2varos = input("Add meg az 2. rekordhoz a várost! > ")

print()
print(vonal)
print(fejlec)
print(vonal)
print(1, rekord1nev, rekord1varos, sep=szeparator)
print(vonal)
print(2, rekord2nev, rekord2varos, sep=szeparator)
print(vonal)
