class Allat:
    def __init__(self, nev, tipus):
        self.nev = nev
        self.tipus = tipus
        self.ehseg = 1

    def eves(self):
        if self.ehseg == 0:
            print("Nem vagyok éhes")
            return
        print("Ettem!")
        self.ehseg = 0


allatnevek = ["Blöki", "Morzsi", "Kutyu", "Mittomén"]
ehes = [True, False, False, True]
kutyaim = []
for neve, ehes_e in zip(allatnevek, ehes):
    uj_kutya = Allat(nev=neve, tipus="kutya")
    uj_kutya.ehseg = ehes_e
    kutyaim.append(uj_kutya)

for kutya in kutyaim:
    kutya.eves()
