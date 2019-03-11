# WARNING: ЭТОТ ФАЙЛ ОТДЕЛЬНО ЗАПУСКАТЬ НЕ НУЖНО
# НУЖНО ЗАПУСКАТЬ ТОЛЬКО main.py

from math import *


def gauss(m=1, b0=10, w=0.25, y0=0, **d):
    pow = -(((d['h'] - (b0 + d['b_ind'])) ** 2) / (2 * (w ** 2)))
    res = y0 + m * exp(pow)
    return res

# ПАРАМЕТРЫ В СТРОКЕ НИЖЕ -- НЕ ТРОГАТЬ,
# РЕДАКТИРОВАТЬ ЗНАЧЕНИЯ НУЖНО В ФАЙЛЕ main.py
def integrate(start=0, end=10, step=0.1, m=1, w=1, b0=10, y0=0, axx=0, ayy=0, azz=0, discr=200): #defaults
    data_y = []
    sum = 0
    pp = pi * 2
    ran = end - start
    num = int(ran//step)
    foo = lambda x: start + x * step
    data_x = [foo(h) for h in range(num)]
    for h in range(num):
        for y in range(int(discr)):
            for x in range(discr//2):
                b = axx * (sin(x * pp / discr) ** 2) * (cos(y * pp / discr) ** 2) + \
                    ayy * (sin(x * pp / discr) ** 2) * (sin(y * pp / discr) ** 2) + \
                    azz * (cos(x * pp / discr) ** 2)
                sum += (gauss(m, b0, w, y0, b_ind=(b * b0), h=(foo(h)) * sin(x * pp / discr)))
        data_y.append(sum)
        sum = 0
        print(h)
    return [data_x, data_y]


