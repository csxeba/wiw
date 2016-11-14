portok = ["21", "22", "80", "8080", "443"]
service = ["ftp", "tcp", "ez_es_tcp", "meg_egy_tcp", "s_egy_https"]

for portname, servicename in zip(portok, service):
    print(portname, servicename)
