from experiment_integrate.lib.drawing import draw_1D_file
from experiment_integrate.lib.readwrite import *
from experiment_integrate.lib.gui import button

path_to_file = r'C:\Users\NMR\Desktop\Example\T1_Li_stim_echo.txt'   #abcolute path to file
extra_file = 't.txt'       # file with extra parameters (must be located in the same directory)
file_to_draw = '1.txt'          # name of file which will be shown as a plot: default is 1.txt
dir_name = os.path.split(path_to_file)[0]
file_name = os.path.split(path_to_file)[1]
os.chdir(dir_name)
prepare_data(file_name)
draw_1D_file(file_to_draw)

button(file_name, extra_file)

