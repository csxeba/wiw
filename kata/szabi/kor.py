# Drága Szabi!
#
# Így néz ki egy valamire való Python script.
# Vannak (függvény) definíciók és a legalján van az a furcsa if rész.
# A furcsa rész csak annyit jelent, hogy ha közvetlenül futtatják ezt
# a scriptet, akkor a main() függvény fusson.
# (egy scriptet nem csak közvetlenül lehet futtatni, lehet importálni is)
#
# Jószerencsét!
# Üdv:
# GCs.

PI = 3.14


def main():
    """
    Ez egy dokumentációs string, ide írjuk le, hogy mit
    csinál a függvényünk.
    """
    # Írj a main()-be egy programot, ami a beker() függvénnyel
    # bekéri egy kör sugarát.
    # Kiírja a bekért sugarat, majd kiírja a megadott sugarú kör
    # területét és kerületét.
    sugar = bekero("Írd be a kör sugarát")
    print(sugar, "sugarú kör kerülete", kor_kerulete(sugar))
    print(sugar, "sugarú kör területe", kor_terulete(sugar))


def kor_kerulete(sugar):
    """Ez a függvény VISSZATÉR a megadott sugarú kör kerületével"""
    return sugar * 2 * PI


def kor_terulete(sugar):
    """Ez a függvény VISSZATÉR a megadott sugarú kör területével"""
    return sugar ** 2 * PI


def bekero(prompt):
    """
    Ez a függvény FELDÍSZÍTI a megadott promptot
    és bekéri a kör sugarát.
    VISSZATÉR a megadott sugárral (előtte float-ra alakítja!)
    """
    sugar = input(prompt + "=")
    return float(sugar)


if __name__ == '__main__':
    main()