import re
import os
import math
from experiment_integrate.lib.maths import rms
'''def rms(a, b):
    return math.sqrt(a ** 2 + b ** 2)
'''
'''def get_dir(filename):
    with open(filename, 'r') as file:
        line = file.readline()
        path_to_tnt = re.search(r'[A-Z]:\\.+\.tnt', line).group(0)
        dir = re.sub(r'\\.+\.tnt', '', path_to_tnt) + '\\1D_files\\'
        return dir
'''

def number_of_records(filename):
    with open(filename, 'r') as file:
        line = file.readline()
        line = file.readline()
        line = file.readline()
        match = re.search(r'Ending Record:\s*(\d+)', line)
        number_of_records = match.group(1)
    return int(number_of_records)


def remove_last_blankline(filename):
    with open(filename, 'r') as file:
        data = file.read()
    if (data[-1] == '\n'):
        with open(filename, 'w') as file:
            file.write(data[:-1])
    return


def format_line(line):
    lst = line.split('\t')
    lst[0], lst[1], lst[2] = lst[2], lst[0], lst[1]
    lst[0] = lst[0][:-1]
    root_mean_square = rms(float(lst[1]), float(lst[2]))
    # root_mean_square = round(root_mean_square)
    lst.append(str(root_mean_square))
    newline = '\t'.join(lst) + '\n'
    return newline


def get_x(line):
    lst = line.split('\t')
    return float(lst[2])


def separate_2D_file(filename):
    with open(filename, 'r') as input:
        line = input.readline()
        dir_name = os.getcwd() + '/1D_files/'
        try:
            os.mkdir(dir_name)
        except FileExistsError:
            pass
        while re.match(r'(?:-?\d+\.\d*[\t\n]){3}', line) is None:  # пропускаем строки, не содержащие данных
            line = input.readline()
        num = number_of_records(filename)
        os.chdir(os.getcwd() + '/1D_files')
        newline = format_line(line)
        for i in range(num):
            x = -1
            name = str(i+1) + '.txt'
            with open(name, 'w') as output:
                k = 0
                while(x != 0):
                    output.write(newline)
                    output.flush()
                    line = input.readline()
                    try:
                        newline = format_line(line)
                        x = get_x(line)
                    except IndexError:
                        x = 0
                    k += 1
                for cnt in range(k+1):
                    output.write(newline)
                    output.flush()
                    line = input.readline()
                    try:
                        newline = format_line(line)
                        x = get_x(line)
                    except IndexError:
                        x = 0


def get_values_from_1D_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        data = [line.split(sep='\t') for line in lines]
        data = list(zip(*data))
        data = [list(map(float, elem)) for elem in data]
        return data

def get_table(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        data = [line.split(sep='\t') for line in lines]
        data = [list(map(float, elem)) for elem in data]
        return data

def write_integration_result(data_x, data_y, lower='', higher=''):

    with open('integral ' + str(lower) + '-' + str(higher) + '.txt', 'w') as file:
        for x, y in zip(data_x, data_y):
            file.write(str(x) + '\t' + str(y) + '\n')
    return

def read_from_extra_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        data_x = data.split(sep='\n')
        # data_x = [float(i) for i in data_x]
        res = []
        for i in data_x:
            try:
                res.append(float(i))
            except ValueError:
                pass
    return res

def write_data(filename, data_x):
    with open(filename, 'w') as file:
        for row in data_x:
            k = ('\t'.join(map(str, row))) + '\n'
            file.write(k)
    return


def prepare_data(filename):
    remove_last_blankline(filename)
    separate_2D_file(filename)

def crop_file(filename, left, right):
    data = get_values_from_1D_file(filename)
    from experiment_integrate.lib.maths import find_closest_value
    min_ind = find_closest_value(data[0], left)
    max_ind = find_closest_value(data[0], right)
    if max_ind < min_ind:
        max_ind, min_ind = min_ind, max_ind

    for i in range(4):
        data[i] = data[i][min_ind:max_ind]

    with open(filename, 'w') as file:
        for x1, x2, x3, x4 in zip(data[0], data[1], data[2], data[3]):
            file.write(str(x1) + '\t' + str(x2) + '\t' + str(x3) + '\t' + str(x4) + '\n')
    return

