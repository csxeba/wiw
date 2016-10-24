# Definíciók

prompt = "\t> "
kerdesek = [
  "Hány tagja van az IP címnek?",
  "Mi a száma az utolsó portnak?",
  "Mi a száma az első portnak?",
  "Milyen színe van az égnek?"
]


valaszok = []
pontok = 0

# 1. kérdés
ip = int(input(kerdesek[0] + prompt))
valaszok += [ip]

if ip == 4:
  print("1. kérdés helyes!")
  pontok += 1
else:
  print("Ajj nem jó!")

# 2. kérdés
utolso_port = int(input(kerdesek[1] + prompt))
valaszok += [utolso_port]

if utolso_port == 65535:
  print("2. kérdés helyes!")
  pontok += 1
else:
  print("Ajj, nem jó!")

# 3. kérdés
elso_port = int(input(kerdesek[2] + prompt))
valaszok += [elso_port]

if elso_port == 0:
  print("3. kérdés helyes!")
  pontok += 1
else:
  print("Ajj, nem jó!")


# 4. kérdés
eg_szine = input(kerdesek[3] + prompt)
valaszok += [eg_szine]

if eg_szine == "kék":
  print("4. kérdés helyes!")
  pontok += 1
else:
  print("Ajj, nem jó!")


# Értékelés
print("-"*50)
print("Pontjaid száma:", pontok, "/", 4)
print("-"*50)
print("Válaszok:", valaszok[0], valaszok[1],
      valaszok[2], valaszok[3], sep="\n")
print("-"*50)

if pontok > 0:
  print("Ügyes vagy!")
else:
  print("Béna voltál!")
