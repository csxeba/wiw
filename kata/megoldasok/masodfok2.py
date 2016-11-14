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
    D = b**2 - 4*a*c
    if D < 0:
        print("Negatív diszkrimináns, nincs valós gyök!")
        return [None, None]
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    return [x1, x2]


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

    for a, b, c in egyenletek:
        print(a, "x**2  + ", b, " x  + ", c, "megoldásai:")
        x1, x2 = megoldo(a, b, c)
        print("x1:", x1, "\tx2:", x2)


if __name__ == '__main__':
    main()
