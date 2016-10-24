# Definíciók

propmt = "\t> "  # HIBA: elírt a változónév
kerdesek = [
  "Hány tagja van az IP címnek?",
  "Mi a száma az utolsó portnak?",
  "Mi a száma az első portnak?",
  "Milyen színe van az égnek?
]
# HIBA FENT: utolsó elemnél lemaradt a záró <">

valaszok = []
pontok = 0

# 1. kérdés
ip = input(kerdesek[0] + prompt)  # HIBA: nincs int-re alakítva
valaszok += [ip]

if ip == 4:
  print("1. kérdés helyes!")
  pontok + 1  # HIBA: lemaradt az értékadás (+=)
else
  print("Ajj nem jó!")

# 2. kérdés
utolso_port = input(kerdesek[1] + prompt) # HIBA: nincs int-re alakítva (sehol)
valaszok += [utolso_port]

if utolso port == 65535:  # HIBA: utolso_port, alulvonás kimaradt
  print("2. kérdés helyes!")
  pontok += 1
else:
  print("Ajj, nem jó!")

# 3. kérdés
elso_port = input(kerdesek[2])  # HIBA: lemaradt a "+ prompt"
valaszok += [utolso_port]  # HIBA: nem az utolso_port-nál tartunk

if utolso_port == 0:  # HIBA: rossz változót tesztelünk
  print("3. kérdés helyes!")
  pontok += 1
else:
  print("Ajj, nem jó!")


# 4. kérdés
eg_szine = input(kerdesek[3] + prompt)
valaszok += [eg_szine]

if eg_szine == kék:  # HIBA: lemaradt a kékről az idézőjel
  print("3. kérdés helyes!")  # HIBA: kérdés száma el van írva
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

if pontok < 0:  # Rossz logikai feltétel (fordítva van a kacsacsőr)
  print("Ügyes vagy!")
else:
  print("Béna voltál!")
