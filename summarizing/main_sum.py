import os
from experiment_integrate.lib.readwrite import  prepare_data, \
                                                read_from_extra_file,\
                                                number_of_records, \
                                                get_values_from_1D_file, \
                                                write_data, \
                                                get_table, \
                                                crop_file
from experiment_integrate.lib.drawing import draw_result
from experiment_integrate.lib.maths import frequency_to_field



path_to_file = r'C:\Users\NMR\Desktop\Example\17dec17-4_5K-79_36MHz_7_045T_2DF.txt'   # abcolute path to file
log_file = '17dec17-4_5K-79_36MHz_7_045T_2D.tnt_log.txt'                                   # name of log file
gamma = 16.546  * 1000000                                      # ПРОВЕРЬ ЕДИНИЦЫ ИЗМЕРЕНИЯ
h0 = 7.045
v0 = 79.36
roundation = 6                                          # параметр округления
left = -300000                                          # границы, по которым обрезаюттся 1D-файлы
right = 300000                                          # ПРОВЕРЬ ЕДИНИЦЫ ИЗМЕРЕНИЯсв зн    cd cd

IS_FIELD_SCANING = True                                 # True или False в зависимости от того, по полю ли измерения
                                                        # (и, соответственно, надо ли их пересчитывать в поле) или
                                                        # по частоте

output_file = 'result(sum).txt'


dir_name = os.path.split(path_to_file)[0]
file_name = os.path.split(path_to_file)[1]
os.chdir(dir_name)
prepare_data(file_name, two_sided=True)
os.chdir(dir_name)
log = read_from_extra_file(log_file)
os.chdir(dir_name)
num = number_of_records(file_name)
os.chdir(os.getcwd() + '/1D_files')

filenames = [str(i + 1) + '.txt' for i in range(num)]



for file in filenames:
    crop_file(file, left, right)
    file_count = 0
    for file in filenames:
        data = get_table(file)
        for row in data:
            if IS_FIELD_SCANING:
                row[0] = frequency_to_field(row[0], gamma, v0, log[file_count], h0, roundation)
            else:
                row[0] = (row[0] // roundation) * roundation
        write_data(file, data)
        file_count += 1

sum_dict = {}

for file in filenames:
    data = get_table(file)
    for row in data:
        key = row[0]
        if key in sum_dict:
            sum_dict[key] += row[3]
        else:
            sum_dict.update({row[0]: row[3]})

result = [[key, sum_dict[key]] for key in sum_dict]
os.chdir(dir_name)
result.sort(key=lambda item: item[0])
write_data(output_file, result)
result = list(map(list, list(zip(*result))))
draw_result(data_x=result[0], data_y=result[1])

