# Akkor is írunk egy portscannert! Illetve annak az első lépését...
#
# Alább láthatsz egy üres listát és egy végtelen ciklust.
# Írj egy kódot a ciklusba, ami bekér egy IP címet.
#
# Ezután kérd be a szkennelendő portok alsó és felső határát (számokat).
# Ha nem ad meg semmit, akkor default minden portot scannelünk: 0-65535
# A bekért infókat tuple-ként tedd bele a <celpontok> listába:
# celpontok += [(ip cím, kezdő port, utolsó port)] valami ilyesmi
# (tehát a <celpontok> egy sokaságokat (tuple) tartalmazó lista lesz!)
# Ha nem ad meg a delikvens IP címet (üres stringet kapsz)
# akkor írd ki a célpontok listát, írd ki, hogy program vége,
# és szakítsd meg a futást! (quit() függvény)

# Az IP cím string legyen, de a portszámokat alakítsd int-re!

celpontok = []

while 1:
    ip = input("IP > ")
    startport = input("Startport > ")
    endport = input("Endport > ")
    if ip == "":
        quit()
    tpl = (ip, startport, endport)
    celpontok += [tpl]

celpontok = [tpl]
