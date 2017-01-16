import string
import io

ROOT = "E:/PyCharm/wiw/data/otszaz/"

file=open(ROOT + "penztar.txt")
sorok=file.readlines()

aktualis_vasarlas=[]
osszes_vasarlas=[]
for sor in sorok:
    ssor=sor.strip()
    if ssor != "F":
        aktualis_vasarlas += [ssor]
    else:
        osszes_vasarlas+= [aktualis_vasarlas]
        aktualis_vasarlas=[]

#for vasarlas in vasarlasok:
#    print(vasarlas, len(vasarlas))


#def elso_feladat():
#   file=open("penztar.txt")
#  tartalom=file.read()
#   betuk=tartalom.count("F")
#    print("A pénztárnál:", betuk, "-szer fizettek")
#    file.close()


#elso_feladat()

#def egyes_feladat():
#   file=open("penztar.txt")
#  sorok=file.readlines()
#for sor in sorok:
#    simasor=sor.rstrip()
#    print(simasor)

#print(open("penztar.txt").readlines()[0].strip



def kettes_feladat():
#    vasarlasok_szama=0
#    for sor in sorok:
#        if sor.strip() == "F":
#            vasarlasok_szama += 1
    vasarlasok_szama=len(osszes_vasarlas)
    print("Kettes feladat :")
    print("A pénzátnál", vasarlasok_szama, "alkalommal fizettek")

kettes_feladat()

def harmas_feladat():
#    termekek_szama=0
#    for sor in sorok:
#        if sor.strip() == "F":
#            break
#        else:
#            termekek_szama+=1
    termekek_szama=len(osszes_vasarlas[0])
    print("Hármas feladat:")
    print("Az első vásárló", termekek_szama, "darab terméket vásárolt")

harmas_feladat()

#vasarlas_sorszama=input("Adja meg a vásárlás sorszámát:")
arucikk_neve=input("Adja meg az árucikk nevét:")
darabszam=input("Adja meg a darabszámot:")

def otos_feladat_a():
    elofordulas_szama = 1
    for vasarlas in osszes_vasarlas:
        if vasarlas.count(arucikk_neve) > 0:
            break
        elofordulas_szama += 1
    print("Ötös feladat:")
    print("A(z)", arucikk_neve, "árucikkből" ,elofordulas_szama, "számú vásárlásnál vettek először")
    elofordulas_vissza = len(osszes_vasarlas)
    for vasarlas in reversed(osszes_vasarlas):
        if vasarlas.count(arucikk_neve) > 0:
            break
        elofordulas_vissza -= 1
    print("A(z)", arucikk_neve, "árucikkből" , elofordulas_vissza, "számú vásárlásnál vettek utoljára")
    
    
otos_feladat_a()

def otos_feladat_b():
    osszes_alkalom = 0
    for vasarlas in osszes_vasarlas:
        if vasarlas.count(arucikk_neve) > 0:
            osszes_alkalom += 1
    print("A(z)", arucikk_neve, "árucikkből" , osszes_alkalom, "alkalommal vásároltak összesen")

otos_feladat_b()

def ertek(darab):
    osszeg = 0
    if int(darab) == 1:
        osszeg = 500
    if int(darab) == 2:
        osszeg = 500+450
    if int(darab) > 2:
        osszeg = 500+450+(int(darab)-2)*400
    return osszeg

print("Az összeg", ertek(darabszam) , "ft.")

def nyolcas_feladat():
    fajl=open("osszeg.txt", "w+")
    sorszam = 0
    for vasarlas in osszes_vasarlas:
        sorszam+=1
        fajl.write(str(sorszam)+": "+str(ertek(len(vasarlas)))+"\n")
    fajl.close()
    
nyolcas_feladat()
    
