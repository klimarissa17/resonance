from experiment_integrate.lib.drawing import draw_1D_file
from experiment_integrate.lib.readwrite import *
from experiment_integrate.lib.gui import button

path_to_file = r'C:\Users\Marika\PycharmProjects\resonance\experiment_integrate\test.txt'   #abcolute path to file
extra_file = 't1list.txt'       # file with extra parameters (must be located in the same directory)
file_to_draw = '1.txt'          # name of file which will be shown as a plot: default is 1.txt
dir_name = os.path.split(path_to_file)[0]
file_name = os.path.split(path_to_file)[1]
os.chdir(dir_name)
prepare_data(file_name)
draw_1D_file(file_to_draw)

button(file_name, extra_file)

