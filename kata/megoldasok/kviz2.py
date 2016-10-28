# Írj egy kvízt, amiben 5 kérdést teszel fel.
# (egyszerű választás stílusban például)
# A megszerzett pontokat kövesd nyomon.
# A végén szövegesen is értékeld a delikvenst.
# Bónusz pont, ha az input prompt jól néz ki :)

prompt = " > "

kerdesek = ["Hogy hívják a vak akkumulátort?",
            "Melyik porton kommunikál a telnet protokoll?",
            "Melyik nagyműszeren dolgozik Anya?",
            "Magas vagy alacsony szintű nyelv a Java?",
            "Hányasra értékeled magad?"]

helyesek = ["vaksi", "23", "NMR", "magas", "-1"]

jok = 0

for kerdes, helyes in zip(kerdesek, helyesek):
    valasz = input(kerdes + prompt)
    if valasz == helyes:
        print("Helyes válasz!")
        jok += 1
    else:
        print("NEM! Helyesen:", helyes)

ertekeles = ["Uramdzsíszösz", "Troll", "Ork", "Ember", "Elf"]
print("Kvízjáték vége. Pontjaid:", jok, "/", len(kerdesek))
print("Értékelésed:", ertekeles[jok], "szintű programozó vagy")
