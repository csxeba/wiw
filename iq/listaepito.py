from math import sqrt

lista = ['2', '3', '1']
masolat = [elem for elem in lista]
atalakitott = [int(elem) for elem in lista]
negyzet = [szam*szam for szam in atalakitott]

eredmeny = sqrt(sum(negyzet))
print(eredmeny)  # 3.7416573867739413
