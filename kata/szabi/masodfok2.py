"""
Ez egy dokumentációs string a programunk elején.
Ide szokták beírni, hogy mit csinál a program.

Ez a program definiál egy másodfokú egyenlet megoldó
függvényt és megold néhány másodfokú egyenletet.

Írj egy függvényt, ami paraméterként a másodfokú
egyenlet a, b és c együtthatóit várja:
ax**2 + bx + c = 0 forma esetén.

-b +- gyök(b**2 - 4ac)
----------------------
          2a

négyzetgyököt az importált sqrt() függvénnyel tudsz vonni.
"""

from math import sqrt


def megoldo(a, b, c):
    """Másodfokú egyenlet megoldó.

    Visszatér a másodfokú egyenlet listába rendezett két gyökével."""
    Diszkriminans = b**2-4*a*c
    if diszkriminans < 0:
        print("nem jó valami, negatív a diszkrimináns")
        return
    x1 = (-b + sqrt(diszkriminans)) / (2*a)
    x2 = (-b - sqrt(diszkriminans)) / (2*a)
    return [x1,x2]

def main():
    """Megoldandó másodfokú egyenletek"""

    egyenletek = [
        [1, -3, -10],
        [2, -9, 4],
        [1, -3, -4],
        [1, -7, 0],
        [1, -2, 3],
        [1, -3, 2],
        [4, -11, 6]
    ]

    # Oldd meg és írasd ki ciklussal!

        for a,b,c in egyenletek:
            x1,x2 = megoldo(a,b,c)
            print("x1:", x1, "x2", x2)

if __name__ == '__main__':
    main()
