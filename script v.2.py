import numpy as np
import matplotlib.pyplot as plt
from math import *
from collections import OrderedDict

def make_diagonal(a11, a22, a33):
    return np.array([[a11, 0, 0], [0, a22, 0], [0, 0, a33]])

def calculate_b_ind_2(tensor, b0):
    column = np.array([[0], [0], [b0]])
    result = np.matmul(tensor, column)
    return result


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

def euler_wiki(x, y, z):
    row1 = np.array([cos(x) * cos(z) - sin(x) * cos(y) * sin(z),
                     -cos(x) * sin(z) - sin(x) * cos(y) * cos(z),
                     sin(x) * sin(y)])

    row2 = np.array([sin(x) * cos(y) + cos(x) * cos(y) * sin(z),
                     -sin(x) * sin(z) + cos(x) * cos(y) * cos(z),
                     -cos(x) * sin(y)])

    row3 = np.array([sin(y) * sin(z),
                     sin(y) * cos(z),
                     cos(y)])

    result = np.array(row1, row2, row3)
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
    # pp = pi * 2
    pp = pi
    discr = 180
    for h in range(num):
        for x in range(discr):
            for y in range(discr):
                for z in range(discr):
                    new_azz = azz_rotated(axx, ayy, azz, (x*pp/2)/discr, (y*pp)/discr, (z*pp)/discr)
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

num = 60
def foo(x):
    return 10 + x/6

data_x = [foo(x) for x in range(num)]
data_y = integrate(num, foo)
text = data_y.pop()

print(data_y)
fig = plt.figure()
plt.plot(data_x, data_y)
plt.title(text, fontsize=10)
plt.show()


#h0 - это b0, hloc - это b_ind, s0 -- не нужен



