import numpy as np
import matplotlib.pyplot as plt
from math import *
from collections import OrderedDict


def gauss(m=1, b0=10, w=0.25, y0=0, **d):
    pow = -(((d['h'] - (b0 + d['b_ind'])) ** 2) / (2 * (w ** 2)))
    res = y0 + m * exp(pow)
    return res

def integrate(num, foo, m = 1, w=1, b0 = 10, y0 = 0, axx = 0, ayy = 0, azz = 0, discr = 300):
    res = []
    sum = 0
    pp = pi * 2
    for h in range(num):
        for y in range(discr):
            for x in range(discr//2):
                b = axx * (sin(x * pp / discr) ** 2) * (cos(y * pp / discr) ** 2) + \
                    ayy * (sin(x * pp / discr) ** 2) * (sin(y * pp / discr) ** 2) + \
                    azz * (cos(x * pp / discr) ** 2)
                sum += (gauss(m, b0, w, y0, b_ind=(b * b0), h=(foo(h)) * sin(x * pp / discr)))
        res.append(sum)
        sum = 0
        print(h)

    s = ""
    d = {"m": m, "b0": b0, "w": w, "y0": y0, "axx": axx, "ayy": ayy, "azz": azz, "discr": discr}
    od = OrderedDict(sorted(d.items()))
    for i in od.items():
        s += (str(i[0]) + " = " + str(i[1]) + ", ")
    res.append(s)
    return res


def draw(num, foo, data_y):
    data_x = [foo(h) for h in range(num)]
    text = data_y.pop()
    fig = plt.figure()
    plt.plot(data_x, data_y)
    plt.title(text, fontsize=10, color='red')
    plt.show()

num = 100

def foo(x):
    return  x/10

# draw(foo, num)
