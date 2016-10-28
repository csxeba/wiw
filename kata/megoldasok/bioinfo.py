
def beolvas(faj):
    if faj not in ("homo_sapiens", "bos_taurus", "drosophila_melanogaster"):
        raise RuntimeError("Szabi, a megadott {0} faj nincs a DNS adatbázisban..."
                           .format(faj))
    return open("../../data/seq/" + faj, "r").read()


fajok = ["homo_sapiens", "bos_taurus", "drosophila_melanogaster"]
dns = []
for faj in fajok:
    dns += [beolvas(faj)]

# 1. feladat:
# Ugye a DNS A, C, T, G szerves bázisokból áll. Fontos info egy DNS minta
# GC-tartalmának meghatározása, azaz a G és C bázisok aránya az összes
# bázishoz képest. Határozd meg a három DNS mintánk (homo_sapiens, bos_taurus
# és drosophila_melanogaster) GC-tartalmát és írasd ki!

for faj, minta in zip(fajok, dns):
    gc = 0
    for bazis in minta:
        if bazis in ("G", "C"):
            gc += 1
    print(faj, "minta GC-tartalma:", gc / len(minta))

# 2. feladat:
# Egy másik informatív mérőszám, hogy hány CpG sziget van egy DNS-en.
# A CpG sziget az egymást követő CG báziskettősből áll. Ezeket mindkét
# irányból értelmezzük (CG mellett a GC is számít)
# Tehát pl. az alábbi DNS szakaszban 3 CpG sziget van, kettő előrefelé
# olvasandó és egy visszafelé.

# ACAGACGTTATGCATGACGATC
#      ||    ||    ||

# Számold meg, hogy a mintákban hány CpG sziget van!

for faj, minta in zip(fajok, dns):
    cgp = 0
    for i in range(len(minta) - 1):
        if minta[i] + minta[i+1] in ("GC", "CG"):
            cgp += 1
    print(faj, "minta CpG szigeteinek száma:", cgp)
