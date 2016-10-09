# Végeztem egy DNS analízist egy ismeretlen mintán.
# Adok neked egy DNS adatbázist, amiben különböző fajok DNS szekvenciáit tárolom.
# (kemény 3 faj van benne)
# Te vagy a bioinformatikusom és szeretném, ha megkeresnéd, melyik DNS szekvenciának
# felel meg a mintám. A mintám csak pár bázisnyi, azt kéne kimutatnod, hogy melyik
# adatbázisban tárolt szekvenciában szerepel az én mintám.


def beolvas(faj):
    if faj not in ("homo_sapiens", "bos_taurus", "drosophila_melanogaster"):
        print("Szabi, rossz fajnevet adtál meg!")
        quit()
    return open("../data/seq/" + faj, "r").read()


# A beolvas függvényt használhatod egy faj DNS-ének beolvasására.
# három faj van az adatbázisunkban:
#
# homo_sapiens
# bos_taurus
# drosophila_melanogaster
#
# a fenti szintaxissal kell átadnod a beolvas() függvénynek argumentumként, pl.:
# emberi_dns = beolvas(homo_sapiens)

# És íme a minta:

minta_dns = "ATTCGTCTCCATCACAGCTGAGCTCCATAAGGGGACTGGCCATAGAAGT"

# Milyen fajból vettem a mintámat?
