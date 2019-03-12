# ЭТО -- ОСНОВНОЙ СКРИПТ,
# ЗАПУСКАТЬ НАДО ИМЕННО И ТОЛЬКО ЕГО

from maths import integrate
from drawing import title, draw
from readwrite import read_data, write_data
values = {
'start':0.5,
'end':1.5,
'step':0.005,
'm': 1,         # амплитуда
'w':0.02,       # ширина линии
'b0': 0.9,      # внешнее поле
'y0': 0,        # шум
'axx': 0.07,    # компоненты тензора
'ayy': 0.22,    # компоненты тензора
'azz': -0.15,   # компоненты тензора
'discr': 250}   # частота интегрирования по углам

# в строке ниже задаётся имя файла с данными.
# файл должен лежать В ТОМ ЖЕ КАТАЛОГЕ, что и main.py

file = 'data.txt'   # имя файла
experimental = read_data(file)
theoretical = integrate(**values)
title = title(values)
draw(experimental, theoretical, title)

write_data('result.txt', theoretical[0], theoretical[1])
