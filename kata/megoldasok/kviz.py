pontok = 0  # ide gyűjtjük majd a pontokat
suffix = ">\t"  # ezt itt definiálom, hogy ne kelljen mindig kiírni


def dekor(prompt):
    return input(prompt + " > ")


def ismetlodo_resz(kerdes, megoldas):
    valasz = input(kerdes + "\n> ")
    if valasz == megoldas:
        print("Yessssss")
        return True
    else:
        print(":(")
        return False


# Felépítem az első kérdés-stringet
kerdesek = ["1.kérdés:\tHogy hívják a vak akkumulátort?\n1) aksi\n2) kaksi\n3) vaksi",
            """2. kérdés\tMi a címe a hackeres sorozatnak, amit ajánlottam?
1) Walter Mitty különös élete
2) Mr. Robot
3) Pentatronix""",
"""3. kérdés (a mindent eldöntő)\tMikor kezdünk már programozni?
1) Majd
2) Ha betöltötted a 18-at, kisfiam
3) Már most is ezerrel azt csináljuk
"""]

megoldasok = ["3", "2", "3"]

for k, m in zip(kerdesek,megoldasok):
    ismetlodo_resz(kerdes=k, megoldas=m)
