ROOT = "E:/PyCharm/wiw/data/otszaz/"


def pull_data(path):
    lines = open(path).readlines()
    vasarlasok = [[]]
    for cikk in lines[:-1]:
        cikk = cikk.strip()

        if not cikk:
            continue

        if cikk == "F":
            vasarlasok.append([])
        else:
            vasarlasok[-1].append(cikk)

    return vasarlasok


def hanyszor_fizettek(vasarlasok):
    print("\n2. feladat")
    print("Fizetések száma:", len(vasarlasok))


def elso_vasarlo_arucikkei(vasarlasok):
    print("\n3. feladat")
    print("Az első vásárló", len(vasarlasok[0]), "darab árucikket vásárolt.")


def bekero():
    print("\n4. feladat")
    adatok = (
        int(input("Kérem adja meg egy vásárlás sorszámát! ")) - 1,
        input("Kérem adja meg egy árucikk nevét! "),
        int(input("Kérem adjon meg egy darabszámot! "))
    )
    return adatok


def eloszor_utoljara(vasarlasok, arucikk):
    print("\n5. feladat")
    for i, vasar in enumerate(vasarlasok, start=1):
        if arucikk in vasar:
            print("Az első vásárlás sorszáma:", i)
            break
    for i, vasar in zip(range(len(vasarlasok), -1, -1), reversed(vasarlasok)):
        if arucikk in vasar:
            print("Az utolsó vásárlás sorszáma:", i)
            break


def ertek(darab):
    if darab == 1:
        return 500
    elif darab == 2:
        return 500 + 450
    else:
        return 500 + 450 + (400 * (darab-2))


def darab_mennyi(darab):
    print("\n6. feladat")
    print(darab, "darab vételekor fizetendő:", ertek(darab))


def kosar_listazas(kosar, verbose=1):
    if verbose:
        print("\n7. feladat")
    termekek = set(kosar)
    darabszamok = []
    for termek in termekek:
        darabszamok.append(kosar.count(termek))
        if verbose:
            print(darabszamok[-1], termek)
    if not verbose:
        return darabszamok


def osszeg(vasarlasok, outpath):
    chain = ""
    for i, kosar in enumerate(vasarlasok, start=1):
        darabszamok = kosar_listazas(kosar, 0)
        fiz = 0
        for darab in darabszamok:
            fiz += ertek(darab)
        chain += "{}: {}\n".format(i, fiz)
    osszegfl = open(outpath + "osszeg.txt", "w")
    osszegfl.write(chain)
    osszegfl.close()


def main():
    vasarlasok = pull_data(ROOT + "penztar.txt")
    hanyszor_fizettek(vasarlasok)
    elso_vasarlo_arucikkei(vasarlasok)
    sorszam, arucikk, darab = bekero()
    eloszor_utoljara(vasarlasok, arucikk)
    darab_mennyi(darab)
    kosar_listazas(vasarlasok[sorszam], verbose=1)
    osszeg(vasarlasok, ROOT)


if __name__ == '__main__':
    main()
