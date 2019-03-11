# ЭТО -- ОСНОВНОЙ СКРИПТ,
# ЗАПУСКАТЬ НАДО ИМЕННО И ТОЛЬКО ЕГО

from maths import integrate, title, draw
from readwrite import read_data, write_data
values = {
'start':6.5,
'end':7,
'step':0.005,
'm': 1,       # амплитуда
'w':0.001,    # ширина линии
'b0': 1,      # внешнее поле
'y0': 0,      # шум
'axx': 1,     # компоненты тензора
'ayy': 0,     # компоненты тензора
'azz': 0.5,   # компоненты тензора
'discr': 200} # частота интегрирования по углам

# в строке ниже задаётся имя файла с данными.
# файл должен лежать В ТОМ ЖЕ КАТАЛОГЕ, что и main.py
file = 'data.dat'
experimental = read_data(file)
print(experimental[0])
print("\n\n")
print(experimental[1])
theoretical = integrate(**values)
title = title(values)
draw(experimental, theoretical, title)

write_data('res.dat', theoretical[0], theoretical[1])