import os
from experiment_integrate.lib.readwrite import  prepare_data, \
                                                read_from_extra_file,\
                                                number_of_records, \
                                                get_values_from_1D_file, \
                                                write_data
from experiment_integrate.lib.drawing import draw_result


def calc(delta_v, gamma, v0, h_i):
    x = 2 * h_i - (delta_v + (v0/gamma))
    return x

path_to_file = r'C:\Users\Marika\PycharmProjects\resonance\experiment_integrate\test.txt'   #abcolute path to file
log_file = 't1list.txt'
gamma = 1
h0 = 1
v0 = 1

dir_name = os.path.split(path_to_file)[0]
file_name = os.path.split(path_to_file)[1]
os.chdir(dir_name)

prepare_data(file_name)
log = read_from_extra_file(file_name)

os.chdir(os.getcwd() + '/..')
num = number_of_records(file_name)
os.chdir(os.getcwd() + '/1D_files')

for i in range(num):
    # with open (str(i + 1) + '.txt', 'r+'):
    data = get_values_from_1D_file(file_name)
    for row in data:
        row[0] = calc(delta_v=row[0], gamma=gamma, v0=v0, h_i=log[i])
    write_data(str(i+1) + '.txt', data)

sum_dict = {}

for i in range(num):
    data = get_values_from_1D_file(file_name)
    for row in data:
        key = row[0]
        if key in sum_dict:
            sum_dict[key] += row[3]
        else:
            sum_dict.update({row[0]:row[3]})

result = [[key, sum_dict[key]] for key in sum_dict]

write_data('result', result)
result = list(map(list, list(zip(*result))))

draw_result(data_x=result[0], data_y=result[1])



'''считаем синюю штуку
в логфайле стоит поле h_i
перевест иксы из частот в поля

'''