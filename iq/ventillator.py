class Ventillator:
    def __init__(self, nev):
        self.propellerek = 5
        self.sebesseg = 0
        self.max_sebesseg = 10
        self.nev = nev

    def gyorsabban(self):
        if self.sebesseg == self.max_sebesseg:
            raise RuntimeError("Nem lehet gyorsabban menni!")
        self.sebesseg += 1

    def lassabban(self):
        if self.sebesseg == 0:
            raise RuntimeError("Nem lehet lassabban menni!")
        self.sebesseg -= 1

    def statusz(self):
        print("-"*25)
        print("Ventillátor:", self.nev)
        print("Ez a ventillátor ", end="")
        if self.sebesseg:
            print("fut.")
        else:
            print("áll.")
        print("Sebesség: ", self.sebesseg, "|", self.max_sebesseg)
        print("Légörvény:", self.sebesseg / self.propellerek)


def egy_venti():
    venti = Ventillator("Oszkár")
    print("\nKezdeti státusz:")
    venti.statusz()

    for _ in range(5):
        venti.gyorsabban()
    print("\nGyorsítás után:")
    venti.statusz()


