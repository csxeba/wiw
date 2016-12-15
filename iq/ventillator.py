class Ventillator:
    """A ventillátorok osztálya!"""

    def __init__(self, azonosito):
        self.propellerek = 5
        self.sebesseg = 0
        self.max_sebesseg = 10
        self.azonosito = azonosito

    def gyorsabban(self):
        if self.sebesseg == self.max_sebesseg:
            raise RuntimeError("A ventillátort nem lehet tovább gyorsítani!")
        self.sebesseg += 1

    def lassabban(self):
        if self.sebesseg == 0:
            raise RuntimeError("A ventillátort nem lehet tovább lassítani!")
        self.sebesseg -= 1

    def legorveny(self):
        return self.sebesseg * self.propellerek

    def statusz(self):
        kimenet = "-"*25 + "\n"
        kimenet += "Ventillátor: " + self.azonosito + " státusza\n"
        if self.sebesseg == 0:
            kimenet += "Ez a ventillátor áll." + "\n"
        else:
            kimenet += "Ez a ventillátor megy." + "\n"
        kimenet += "sebesség:   " + str(self.sebesseg) + "/" + str(self.max_sebesseg) + "\n"
        kimenet += "légörvény:  " + str(self.legorveny())
        if self.propellerek == 0:
            kimenet += " (nincs propeller)"
        print(kimenet)


def egy_venti():
    venti = Ventillator("Oszkár")
    print("\nKezdeti státusz:")
    venti.statusz()
    for _ in range(5):
        venti.gyorsabban()
    print("\nGyorsítás után:")
    venti.statusz()

    venti.propellerek = 100
    print("\nPropellerek növelése 100-ra:")
    venti.statusz()

    venti.propellerek = 0
    print("\nPropellerek kiiktatása:")
    venti.statusz()


def sok_venti():
    venti_nevek = "Oszi", "Karesz", "Röpi", "Heli", "Sör"
    gyorsitasok = [3, 5, 2, 1, 6]
    venti_objektumok = [Ventillator(azonosito=nev) for nev in venti_nevek]
    for venti, gyorsitas in zip(venti_objektumok, gyorsitasok):
        for _ in range(gyorsitas):
            venti.gyorsabban()
    for venti in venti_objektumok:
        venti.statusz()


if __name__ == '__main__':
    egy_venti()
