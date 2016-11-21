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
    megoldas = []
    for elem in vektor:
        megoldas = elem * skalar
    return ujvektor


def norma(vektor):
    """
    Egy vektor normája (mérete) az elemeinek összege a négyzetgyök alatt.
    Gyököt a beimportált sqrt() függvénnyel tudsz vonni.
    """


def vektor_plusz_vektor(vektor1, vektor2):
    """
    Két vektort úgy adunk össze, hogy minden
    elemüket összeadjuk.
    """
    megoldas = []
    for elsoelem, masodikelem in zip(vektor1, vektor2):
        megoldas = elem1 + elem2
    return megoldas


def vektor_egyenlo(vektor1, vektor2):
    """
    Két vektor akkor egyenlő, ha minden elemük rendre
    egyenlő.
    """
    megoldas = []
    for i in range(len(vektor1)):
        osszehasonlotott = vektor1[i] == vektor2[i]
        megoldas += [osszehasonlotott]
    return False in megoldas


def skalaris_szorzat(vektor1, vektor2):
    """
    Két vektor skaláris szorzatát a következőképpen kapjuk
    (pl. 3 elemű vektorok esetén:)

    vektor1 első eleme * vektor2 első eleme PLUSZ
    vektor1 második eleme * vektor2 második eleme PLUSZ
    vektor1 harmadik eleme * vektor2 harmadik eleme
    """
    pass


def main():
    v1 = [8.7, -15.1, 3.5]
    v2 = [5.3, 3.0, -10.0]
    s1 = 3.14
    # Végezd el a fenti műveleteket és írasd ki az eredményt
    print("v1 szorozva s1-el:", szorzas_skalarral(v1, skalar=s1))
    print("v1 vektor mérete:", norma(v1))
    print("v1 és v2 összege:", vektor_plusz_vektor(v1, v2))
    print("v1 és v2 egyenlő:", vektor_egyenlo(v1, v2))
    print("v1 és v2 skalaris szorzata:", skalaris_szorzat(v1, v2))


if __name__ == '__main__':
    main()
