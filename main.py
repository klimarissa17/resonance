import numpy as np
import matplotlib.pyplot as plt
from easy import integrate, title, draw
from filereader import read_data
values = {
'start':6.5,
'end':7,
'step':0.005,
'm': 1, # амплитуда
'w':0.001, # ширина линии
'b0': 1, # внешнее поле
'y0': 0, # шум
'axx': 1, # компоненты тензора
'ayy': 0, # компоненты тензора
'azz': 0.5, # компоненты тензора
'discr': 200} # частота интегрирования по углам

file = 'data.dat'
experimental = read_data(file)
theoretical = integrate(**values)
title = title(values)
draw(experimental, theoretical, title)
