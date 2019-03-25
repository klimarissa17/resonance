import numpy as np
import matplotlib.pyplot as plt
from math import *
from collections import OrderedDict


def euler(x, y, z):
    row1 = np.array([cos(x) * cos(y) * cos(z) - sin(x) * sin(z),
                     -sin(x) * cos(z) - cos(x) * cos(y) * sin(z),
                     cos(x) * sin(y)])

    row2 = np.array([sin(x) * cos(y) * cos(z) + cos(x) * sin(z),
                     cos(x) * cos(z) - sin(x) * cos(y) * sin(z),
                     sin(x) * sin(y)])

    row3 = np.array([-sin(x) * cos(z),
                     sin(y) * sin(z),
                     cos(y)])
    result = np.array([row1, row2, row3])
    return result


def azz_rotated(axx, ayy, azz, x, y, z):
    r = euler(x, y, z)
    return r[2][0] * axx * r[0][2] + r[2][1] * ayy * r[1][2] + r[2][2] * azz * r[2][2]


def gauss(m, b0, w, y0, b_ind, h):
    pow = -(((h - (b0 + b_ind)) ** 2) / (2 * (w ** 2)))
    res = y0 + m * exp(pow)
    return res


def integrate(num, foo, m = 1, b0 = 12, w = 0.1, y0 = 0, axx = 0, ayy = 0, azz = 0.3):
    res = []
    sum = 0
    pp = pi * 2
    discr = 40
    for h in range(num):
        for x in range(discr):
            for y in range(discr):
                for z in range(discr):
                    new_azz = azz_rotated(axx, ayy, azz, (x*pp)/discr, (y*pp)/discr, (z*pp)/discr)
                    b_ind = new_azz * b0
                    k = gauss(m, b0, w, y0, b_ind, foo(h))

                    sum += k
        print(h)
        res.append(sum)
        sum = 0

    s = ""
    d = {"m": m, "b0": b0, "w": w, "y0": y0, "axx": axx, "ayy": ayy, "azz": azz, "discr": discr}
    od = OrderedDict(sorted(d.items()))
    for i in od.items():
        s += (str(i[0]) + " = " + str(i[1]) + ", ")
    res.append(s)
    return res


def integrate2(num, foo, m = 1, b0 = 12, w = 0.5, y0 = 0, axx = 0, ayy = 0, azz = 1):
    res = []
    sum = 0
    pp = pi * 2
    discr = 160
    for h in range(num):
        for x in range(discr):
            for y in range(discr//2):
                for z in range(discr):
                    new_azz = azz_rotated(axx, ayy, azz, (x*pp)/discr, (y*pp/2)/(discr/2), (z*pp)/discr)
                    b_ind = new_azz * b0
                    k = gauss(m, b0, w, y0, b_ind, foo(h))

                    sum += k
                sum *= sin(y*pi/(discr/2))

            sum /= (8 * (pi **2))
        print(h)
        res.append(sum)
        sum = 0

    s = ""
    d = {"m": m, "b0": b0, "w": w, "y0": y0, "axx": axx, "ayy": ayy, "azz": azz, "discr": discr}
    od = OrderedDict(sorted(d.items()))
    for i in od.items():
        s += (str(i[0]) + " = " + str(i[1]) + ", ")
    res.append(s)
    return res



num = 50
def foo(x):
    return 16 + x/5

data_x = [foo(x) for x in range(num)]
data_y = integrate2(num, foo)
text = data_y.pop()
fig = plt.figure()
plt.plot(data_x, data_y)
plt.title(text, fontsize=10)
plt.show()





