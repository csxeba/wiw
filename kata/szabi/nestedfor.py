import socket


# Írunk egy normális portscannert.


def scan(ip, port):
    """
    Ez a függvény megvizsgálja, hogy az <ip> paraméterként kapott
    cím <port> paraméterben meghatározott portja nyitva van-e.
    Az ellenőrzés teljes TCP kézfogással történik (nem valami kifinomult)
    """

    # noinspection PyBroadException
    try:
        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sck.settimeout(0.1)

        result = sck.connect_ex((ip, port))
        if result == 0:
            print("{0}:{1} NYITVA!".format(ip, port))
            sck.close()
            return True
        else:
            print("{0}:{1} ZÁRVA!".format(ip, port))
            sck.close()
            return False
    except:
        print("Leállás!")
        quit()


# Két egymásba ágyazott for ciklust kell írnod.
# A külső for végigmegy az IP címeken 192.168.1.1 - 192.168.1.50-ig
# A belső for scanneli az első 1000 portot (rendszer-portokat)

cim_eleje = "192.168.1."

for i in range("192.168.1.", "192.168.1.50"):
    for a in range(0, 1000):
        print(i, a, sep=\t)