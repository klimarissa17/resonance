# WARNING: ЭТОТ ФАЙЛ ОТДЕЛЬНО ЗАПУСКАТЬ НЕ НУЖНО
# НУЖНО ЗАПУСКАТЬ ТОЛЬКО main.py

import re


def read_data(filename):
    with open(filename, 'r') as file:
        data = file.read()
    text_info = re.findall('[a-zA-Z.]+', data)
    data = re.sub(',', '.', data)
    text_info = list(text_info)
    columns = text_info[:2]
    units = text_info[2:4]
    data = re.split('[\s]', data)[4:]
    data_x = data[::2]
    data_y = data[1::2]
    return [data_x, data_y]

def write_data(filename, list1, list2):
    with open(filename, 'w+') as file:
        for i, j in zip(list1, list2):
            file.write('{}\t{:f}\n'.format(i, j))
