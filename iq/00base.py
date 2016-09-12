# Ez komment

# Adattípusok, változó deklaráció
a = 2
b = 2.
c = "2_"
c *= 2
d = True

# Kiíratás -> műveletek különböző adattípusokkal
print(a + b)  # 4.0  (mert <b> float)
print(a + a)  # 4    (mert <a> int)
print(c * a)  # 2_2_ (mert ilyet szabad)
print(a + d)  # 3    (ilyet is szabad)
print(b + d)  # 3.0  (sőt, ilyet is)

# del kulcsszó változó(k) törlésére
del a, b, d

# többszörös értékadás
a, b, c, d = 1, 2, 3, 4
e, f, g, h = 4, 1, 2, 3
i, j, k, l = 3, 4, 1, 2
m, n, o, p = 2, 3, 4, 1

# string beolvasás és manipuláció \t -> tab, \n -> új sor (new line)
end = input("Wha? > ")
end += "\n"  # <end> végére konkatenáljuk az új sor karaktert
end = "\t" + end  # <end> elejére konkatenálunk egy tabot
# Ezt lehet egy sorban is. Hogyan?

# Paraméterezett print
print(a, b, c, d, sep="\t", end=end)
print(e, f, g, h, sep="\t", end=end)
print(i, j, k, l, sep="\t", end=end)
print(m, n, o, p, sep="\t", end=end)
