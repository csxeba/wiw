# Hozz létre egy listát, amiben eltárolod, a <portok> listában tárolt
# portszámokhoz tartozó protokollok nevét.
# A protokollok listában is 5 elem legyen és a <portok> lista sorrendjének
# megfelelő sorrendben legyenek a protokollok nevei.
# Ha kész, írasd ki egy ciklussal hogy melyik portszámhoz melyik protokoll
# tartozik.

portok = [21, 22, 80, 8080, 443]
service = ["FTP", "SSH", "HTTP", "HTTP", "HTTP/SSL"]

for port, serv in zip(portok, service):
    print(port, ":", serv)
