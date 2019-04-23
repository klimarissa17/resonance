import numpy as np
from scipy.integrate import simps
import os
import math

def integrate(start, end, data_x, data_y, discr=200):  # defaults
    lower, higher = find_bounds(start, end, data_x)
    x = np.array(data_x[lower:higher+1])
    y = np.array(data_y[lower:higher+1])
    I1 = simps(y, x)
    return I1

def find_closest_value(data_x, value):
    return min(enumerate(data_x), key=lambda x: abs(x[1] - value))[0]

def find_bounds(x,y, data_x):
    lower = find_closest_value(data_x, x)
    higher = find_closest_value(data_x, y)
    return [lower, higher]

def rms(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def main_calculation(input_file, extra_file, start, end, param):
    from experiment_integrate.lib.readwrite import get_values_from_1D_file, number_of_records, write_integration_result
    os.chdir(os.getcwd() + '/..')
    num = number_of_records(input_file)
    os.chdir(os.getcwd() + '/1D_files')
    integration_results = []
    for i in range(num):
        data = get_values_from_1D_file(str(i+1) + '.txt')
        res = integrate(start, end, data[0], data[param])
        integration_results.append(res)
    os.chdir(os.getcwd() + '/..')
    from experiment_integrate.lib.readwrite import read_from_extra_file
    print(os.getcwd())
    data_x = read_from_extra_file(extra_file)
    print(os.getcwd())
    print(integration_results)
    write_integration_result(data_x, integration_results, lower=start, higher=end, name=input_file)
    from experiment_integrate.lib.drawing import draw_result

    draw_result(filename=extra_file, data_y=integration_results, dotted=True)
    return integration_results

def frequency_to_field(delta_v, gamma, v0, h_i, h0, roundation=1):
    x = 2 * (h0 + h_i) - (delta_v + (v0/gamma))
    x = (x // roundation) * roundation
    return x