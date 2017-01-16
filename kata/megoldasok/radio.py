class Vetel:
    def __init__(self, sorpar):
        elsosor = sorpar[0].split(" ")
        self.nap = int(elsosor[0])
        self.radios = int(elsosor[1])

        masodiksor = sorpar[1]
        if szame(masodiksor[0]):
            self.kifejlett = int(masodiksor[0])
            self.kolyok = int(masodiksor[2])
            self.uzenet = masodiksor[4:]
        else:
            self.kifejlett = 0
            self.kolyok = 0
            self.uzenet = masodiksor


def fajl_beolvasas(utvonal):
    sorok = open(utvonal).readlines()
    vetel_objektumok = []
    for i in range(len(sorok) // 2):
        sorpar = sorok[i].strip(), sorok[i+1].strip()
        vetel_objektumok.append(Vetel(sorpar))
    return vetel_objektumok


def elso_utolso_amator(vetelek):
    print("\n2. feladat")
    print("Az első üzenet készítője:", vetelek[0].radios)
    print("Az utolsó üzenet készítője:", vetelek[-1].radios)


def farkas_szerepel(vetelek):
    print("\n3. feladat")
    szerepel = [vetel for vetel in vetelek if "farkas" in vetel.uzenet]
    for vetel in szerepel:
        print("{}. nap {}. rádióamatőr".format(vetel.nap, vetel.radios))


def naponkenti_stat(vetelek):
    print("\n4.feladat")
    for ma in range(1, 12):
        makeszitett = [vetel for vetel in vetelek if vetel.nap == ma]
        print("A {}. napon {} amatőr készített feljegyzést!".format(ma, len(makeszitett)))


def helyreallitas(vetelek):
    outchain = ""
    for ma in range(1, 12):
        helyreallitott = ["#"] * 44
        maiak = [vetel for vetel in vetelek if vetel.nap == ma]
        if len(maiak) == 0:
            outchain += "#\n"
        for vetel in maiak:
            outchain += str(vetel.nap) + " " + vetel.radios + "\n"
            outchain += vetel.uzenet + "\n"
            for i, kar in enumerate(vetel.uzenet):
                if helyreallitott[i] != "#":
                    assert helyreallitott[i] == kar
                    continue
                if kar != "#":
                    helyreallitott[i] = kar


def szame(szo):
    valasz = True
    for i in range(len(szo)):
        if szo[i] < "0" or szo[i] > "9":
            valasz = False
    return valasz


def beolvas():
    print("\n7. feladat")
    nap = int(input("Kérem adja meg egy nap számát! ")),
    radios = int(input("Kérem adja meg egy rádióamatőr számát! "))



