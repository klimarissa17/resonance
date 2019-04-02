# WARNING: ЭТОТ ФАЙЛ ОТДЕЛЬНО ЗАПУСКАТЬ НЕ НУЖНО
# НУЖНО ЗАПУСКАТЬ ТОЛЬКО main.py

from math import *


def gauss(b_ind, h, m=1, b0=10, w=0.25, y0=0):
    pow = -(((h - (b0 + b_ind)) ** 2) / (2 * (w ** 2)))
    res = y0 + m * exp(pow)
    return res

def normalize(list):
    mx = max(list)
    return [elem / mx for elem in list]



# ПАРАМЕТРЫ В СТРОКЕ НИЖЕ -- НЕ ТРОГАТЬ,
# РЕДАКТИРОВАТЬ ЗНАЧЕНИЯ НУЖНО В ФАЙЛЕ main.py
def powder_integration(start=0, end=10, step=0.1,
              m=1, w=1, b0=10, y0=0,
              axx=0, ayy=0, azz=0,
              discr=200): #defaults
    data_y = []
    sum = 0
    pp = pi * 2
    ran = end - start
    num = int(ran//step)
    next_x = lambda x: start + x * step
    data_x = [next_x(h) for h in range(num)]
    for h in range(num):
        for y in range(int(discr)):
            for x in range(discr//2):
                b = axx * (sin(x * pp / discr) ** 2) * (cos(y * pp / discr) ** 2) + \
                    ayy * (sin(x * pp / discr) ** 2) * (sin(y * pp / discr) ** 2) + \
                    azz * (cos(x * pp / discr) ** 2)
                res = gauss(b * b0, next_x(h), m, b0, w, y0) * sin(x * pp / discr)
        data_y.append(sum)
        sum = 0
        print(h)
    data_y = normalize(data_y)
    return [data_x, data_y]


