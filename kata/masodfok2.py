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
    pass


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


if __name__ == '__main__':
    main()