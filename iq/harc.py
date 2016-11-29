from random import random


class Harcos:
    def __init__(self, nev, tamadas, vedekezes, sebzes):
        self.nev = nev
        self.elet = 100
        self.tamadas = tamadas
        self.vedekezes = vedekezes
        self.sebzes = sebzes

    def tamad(self, masik):
        if random() < 0.5:
            if self.tamadas > masik.vedekezes:
                masik.elet -= self.sebzes
                masik.update()

    def update(self):
        if self.elet <= 0:
            print(self.nev, "meghalt!")


def harc(harcos1: Harcos, harcos2: Harcos):
    kor = 1
    while harcos1.elet > 0 and harcos2.elet > 0:
        harcos1.tamad(harcos2)
        if harcos2.elet > 0:
            harcos2.tamad(harcos1)
        kor += 1

    print("Harc vége!")
    if harcos1.elet > 0:
        gyoztes = harcos1
        masik = harcos2
    else:
        gyoztes = harcos2
        masik = harcos1
    # gyoztes = harcos1 if harcos1.elet > 0 else harcos2
    # masik = harcos2 if harcos1.elet > 0 else harcos1

    print(gyoztes.nev, "harcos legyőzte", masik.nev, "harcost", kor, "környi harcban!")


if __name__ == '__main__':
    harc(
        Harcos("Szabi", tamadas=10, vedekezes=15, sebzes=20),
        Harcos("Csabi", tamadas=30, vedekezes=20, sebzes=30)
    )
