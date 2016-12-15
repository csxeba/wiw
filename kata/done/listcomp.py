from math import exp

import time

ETA = 1e-0
AND = [[[0, 0], 0],
       [[0, 1], 0],
       [[1, 0], 0],
       [[1, 1], 1]]


def mse(a, y):
    """
    A kvadratikus veszteségfüggvény
    (átlagos négyzetes eltérés)
    """
    return (a - y)**2


def sigmoid(z):
    """
    A logisztikus (szigmoid) függvény:

         1
    -----------
     1 + e^(-z)

    """
    return 1. / (1. + exp(-z))


def sprime(a):
    return a * (1 - a)


def elore(X, W, b):
    z = sum(x * w + b for x, w in zip(X, W))
    return sigmoid(z)


def main():
    W = [-0.2, .1]  # súlyvektor
    b = 0.  # eltolósúly

    for epoch in range(1, 1001):
        cst = 0
        for (x1, x2), y in AND:
            z = x1 * W[0] + x2 * W[1] + b
            a = sigmoid(z)

            cst += mse(a, y)

            hiba = (a - y) * sprime(a)
            W[0] -= x1 * hiba * ETA
            W[1] -= x2 * hiba * ETA
            b -= hiba * ETA
        print("Veszteség {}. korszakban: {}".format(epoch, cst))
        print("0 ÉS 0 szerintem", elore([0, 0], W, b))
        print("1 ÉS 0 szerintem", elore([1, 0], W, b))
        print("0 ÉS 1 szerintem", elore([0, 1], W, b))
        print("1 ÉS 1 szerintem", elore([1, 1], W, b))
        print("-"*50)
        time.sleep(0.1)

if __name__ == '__main__':
    main()
