a = 1
b = 1.
c = "1"
d = True

# int, float és bool viszonya egymáshoz logikai kifejezésekben
print("-"*30)  # Dísznek
if a == b:
    print("a == b: <a> got implicitly casted to float")
    print("1. == 1. indeed")
    print("-"*30)

if a == c:
    print("This won't run")
    print("-"*30)

if a == d:
    print("a == d: This does work, <a> gets casted to bool")
    print("True == True indeed")
    print("-"*30)

# Melyik ág fut? Miért?
if c == d:
    print("Weird. c == d evaluates to:", c == d)
    print("Why is that?")
    print("-"*30)
else:
    print("Weird. c == d evaluates to:", c == d)
    print("Why is that?")
    print("-"*30)

z = 0

if z == d:
    print("This won't run of course")
elif not z:  # not kulcsszó a logikai kifejezés elejére kell, hogy kerüljön
    print("<z> implicitly gets casted to bool")
    print("not False is True indeed")
    print("-"*30)
else:
    print("This won't run because we entered the elif branch above")

if b > z:
    print("b > z: integers and floats can be compared")
    print("1. is greater than 0 indeed.")
    print("-"*30)

message = "I like beer. Mmmmm!!!"

if message > c:
    print("string > c: strings are compared alphabetically")
    print("Numbers are earlier in the alphabet than lettes")
    print("-"*30)

# Ez ekvivalens a következő (explicit) kifejezéssel:
# if bool(message):
# De a cast-olás implicit is megtörténik.
if message:
    print("<message> is implicitly converted to bool")
    print("The truth value of a non-empty string is True")
    print("-"*30)

dude = "WiW"

# Melyik ág fut le?
if dude == "WiW" or dude == "Csx":
    print("What's up with the dudes?")
    print("-" * 30)
elif dude == "WiW" and dude == "Csx":
    print("What's up with the dudes?")
    print("-" * 30)
