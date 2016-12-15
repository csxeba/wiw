"""
Írj egy hangya osztályt.
A hangyának legyen egy neve (string) és egy pozíciója (lista)
A hangya pozícióját X és Y koordinátákkal határozzuk meg.
A képzeletbeli pályánk 10x10-es.
A hangya osztálynak legyen egy mozgást vezérlő metódusa, ami
módosítja a hangya pozícióját. Kezeld le a pálya határait!
"""


class Hangya:

    def __init__(self, nev, startpoz=None):
        self.nev = nev
        if startpoz is None:
            self.poz = [5, 5]
        else:
            self.poz = list(startpoz)

    def fel(self):
        self.mozgas("fel")

    def le(self):
        self.mozgas("le")

    def balra(self):
        self.mozgas("balra")

    def jobbra(self):
        self.mozgas("jobbra")

    def mozgas(self, merre):
        if merre == "fel":
            self.poz[0] += 1
            if self.palya_szele():
                print("{} felül túlment!".format(self.nev))
        elif merre == "le":
            self.poz[0] -= 1
            if self.palya_szele():
                print("{} alul túlment!".format(self.nev))
        elif merre == "jobbra":
            self.poz[1] += 1
            if self.palya_szele():
                print("{} jobbra túlment!".format(self.nev))
        elif merre == "balra":
            self.poz[1] -= 1
            if self.palya_szele():
                print("{} balra túlment!".format(self.nev))
        else:
            raise RuntimeError("Ilyen irány nincs: {}".format(merre))
        print("{} {} mozdult. Új pozíció: X: {} Y: {}"
              .format(self.nev, merre, self.poz[1], self.poz[0]))

    def palya_szele(self):
        legfelul_voltam = True
        oldalt_voltam = True
        if self.poz[0] > 10:
            self.poz[0] = 10
        elif self.poz[0] < 0:
            self.poz[0] = 0
        else:
            legfelul_voltam = False

        if self.poz[1] > 10:
            self.poz[1] = 10
        elif self.poz[1] < 0:
            self.poz[1] = 0
        else:
            oldalt_voltam = False

        return oldalt_voltam or legfelul_voltam
