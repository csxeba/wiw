def dehun(fajl, kimenet=None):
    if isinstance(fajl, str):
        fajl = open(fajl, "r")
    txt = fajl.read()
    fajl.close()

    mitmire = {"á": "a", "é": "e", "í": "i",
               "ó": "o", "ö": "o", "ő": "o",
               "ú": "u", "ü": "u", "ű": "u",
               "Á": "A", "É": "E", "Í": "I",
               "Ó": "O", "Ö": "O", "Ő": "O",
               "Ú": "U", "Ü": "U", "Ű": "U"}

    ujtxt = ""
    for char in txt:
        if char in mitmire:
            ujtxt += mitmire[char]
        else:
            ujtxt += char

    if kimenet is None:
        return ujtxt
    else:
        kimenetfajl = open(kimenet, "w")
        kimenetfajl.write(ujtxt)
        kimenetfajl.close()
