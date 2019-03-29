import re
import os
import math
import matplotlib.pyplot as plt

def get_dir(filename):
    with open(filename, 'r') as file:
        line = file.readline()
        path_to_tnt = re.search(r'[A-Z]:\\.+\.tnt', line).group(0)
        dir = re.sub(r'\\.+\.tnt', '', path_to_tnt) + '\\1D_files\\'
        return dir


def my_dir():
    path = os.getcwd() + '/1D_files/'
    return path


def rms(a, b):
    return math.sqrt(a ** 2 + b ** 2)


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


def formatline(line):
    lst = line.split('\t')
    lst[0], lst[1], lst[2] = lst[2], lst[0], lst[1]
    lst[0] = lst[0][:-1]
    root_mean_square = rms(float(lst[1]), float(lst[2]))
    lst.append(str(root_mean_square))
    newline = '\t'.join(lst) + '\n'
    return newline


def get_x(line):
    lst = line.split('\t')
    return float(lst[2])


def separate(filename):
    with open(filename, 'r') as file:
        line = file.readline()
        dir_name = my_dir()
        try:
            os.mkdir(dir_name)
        except FileExistsError:
            pass
        while re.match(r'(?:-?\d+\.\d*[\t\n]){3}', line) is None:  # пропускаем строки, не содержащие данных
            line = file.readline()
        num = number_of_records(filename)
        os.chdir(os.getcwd() + '/1D_files')
        newline = formatline(line)
        for i in range(num):
            x = -1
            print(i)

            with open(str(i+1) + '.txt', 'w') as new_file:
                while(x != 0):
                    new_file.write(newline)
                    line = file.readline()
                    try:
                        newline = formatline(line)
                        x = get_x(line)
                    except IndexError:
                        x = 0


remove_last_blankline('test.txt')
separate('test.txt')

with open('1.txt', 'r') as file:
    lines = file.read().splitlines()
    data = [line.split(sep='\t') for line in lines]
    data = list(zip(*data))
    data = [list(map(float, elem)) for elem in data]
    extr = [min(data[i]) for i in range(4)]
    extr.extend([max(data[i]) for i in range(4)])
    y_max = max(extr)
    y_min = min(extr)
    rng = y_max - y_min
    yticks = [y_min + (rng/30) * i for i in range(31)]
    yticks.extend(extr)
    print(extr)
    yticks = list(set(yticks))

    fig = plt.figure(figsize=(60, 45))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(data[0], data[1])
    plt.xticks([data[0][i] for i in range(len(data[0])) if i % 20 == 0])
    plt.yticks(yticks, fontsize=6)
    ax.plot(data[0], data[2])
    ax.plot(data[0], data[3])
    ax.set_title('hohoho')
    plt.show()

