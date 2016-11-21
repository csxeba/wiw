def rendez(*szamok):
    """
    Írj egy függvényt, amely sorba rendezi a neki átadott
    számokat és visszatér a rendezett számokkal!
    """
    return sorted(szamok)  # :)


def legnagyobb(*szamok, hanyadik):
    """
    Írj egy függvényt, amely visszaadja a neki átadott
    számok közül a "hányadik" legnagyobbat.
    """
    sorba = sorted(szamok)
    return sorba[-hanyadik]


def egyseg_matrix(meret):
    """
    Írj egy függvényt, amely adott méretű egységmátrixszal
    tér vissza!

    A mátrix ebben az esetben egy tuple, amelynek az elemei
    is tuple-ök.
    Az egységmátrix egy NxN-es számnégyzet, melynek minden
    eleme nulla, kivéve a bal felső sarokból a jobb alsó
    sarokba futó átlóját.
    Például, ha meret=3,

    ((1, 0, 0),
     (0, 1, 0),
     (0, 0, 1))

    az egységmátrix.
    """
    matrix = []
    for sor in range(meret):
        vektor = []
        for oszlop in range(meret):
            ertek = 1 if sor == oszlop else 0
            vektor += [ertek]
        matrix += [vektor]
    return matrix


def main():
    for vektor in egyseg_matrix(5):
        print(vektor)
    print(legnagyobb(10, 2, 5, 3, 6, 2, 8, hanyadik=3))
    print(rendez(10, 3, 5, 23, 4, 6, 3, 2))


if __name__ == '__main__':
    main()
