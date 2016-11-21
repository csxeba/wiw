"""
Ez a program vektor-operációkat definiál.
A vektorokat listák fogják képviselni.
"""

from math import sqrt


def szorzas_skalarral(vektor, skalar):
    """
    Vektort úgy szorzunk skalárral (számmal),
    hogy minden elemét megszorozzuk.
    """
    ujvektor = []
    for elem in vektor:
        ujvektor.append(elem * skalar)
    return ujvektor


def norma(vektor):
    """
    Egy vektor normája (mérete) az elemeinek négyzetösszege
    a négyzetgyök alatt.
    Gyököt a beimportált sqrt() függvénnyel tudsz vonni.
    """
    gyujto = 0
    for elem in vektor:
        gyujto += elem ** 2
    return sqrt(gyujto)


def vektor_plusz_vektor(vektor1, vektor2):
    """
    Két vektort úgy adunk össze, hogy minden
    elemüket összeadjuk.
    """
    ujvektor = []
    for elem1, elem2 in zip(vektor1, vektor2):
        ujvektor.append(elem1 + elem2)
    return ujvektor


def vektor_egyenlo(vektor1, vektor2):
    """
    Két vektor akkor egyenlő, ha minden elemük rendre
    egyenlő.
    """
    egyenlo = True
    for elem1, elem2 in zip(vektor1, vektor2):
        if elem1 != elem2:
            egyenlo = False
    return egyenlo


def skalaris_szorzat(vektor1, vektor2):
    """
    Két vektor skaláris szorzatát a következőképpen kapjuk
    (pl. 3 elemű vektorok esetén:)

    vektor1 első eleme * vektor2 első eleme PLUSZ
    vektor1 második eleme * vektor2 második eleme PLUSZ
    vektor1 harmadik eleme * vektor2 harmadik eleme
    """
    # megoldas = 0.0
    # for e1, e2 in zip(vektor1, vektor2):
    #     megoldas += e1 * e2
    # return megoldas
    return sum([e1 * e2 for e1, e2 in zip(vektor1, vektor2)])


def main():
    v1 = [8.7, -15.1, 3.5]
    v2 = [5.3, 3.0, -10.0]
    s1 = 3.14

    print("v1 vektor szorozva s1 skalárral:", szorzas_skalarral(v1, skalar=s1))
    print("v1 vektor normája (mérete):", norma(v1))
    print("v1 és v2 vektorok összege:", vektor_plusz_vektor(v1, v2))
    print("v1 és v1 vektorok egyenlők:", vektor_egyenlo(v1, v1))
    print("v1 és v2 vektorok skaláris szorzata:", skalaris_szorzat(v1, v2))


if __name__ == '__main__':
    main()
