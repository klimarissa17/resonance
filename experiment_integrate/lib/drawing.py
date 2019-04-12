import matplotlib.pyplot as plt
from experiment_integrate.lib.readwrite import get_values_from_1D_file, read_from_extra_file

def draw_1D_file(filename):
    data = get_values_from_1D_file(filename)
    extremums = [min(data[i]) for i in range(4)]
    extremums.extend([max(data[i]) for i in range(4)])
    y_max = max(extremums)
    y_min = min(extremums)
    rng = y_max - y_min
    yticks = [y_min + (rng / 30) * i for i in range(31)]
    yticks.extend(extremums)
    yticks = list(set(yticks))
    xticks = [data[0][i] for i in range(len(data[0])) if i % 20 == 0]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(data[0], data[1], color='red')
    plt.xticks(xticks)
    plt.yticks(yticks, fontsize=6)
    ax.plot(data[0], data[2], color='green')
    ax.plot(data[0], data[3], color='blue')
    ax.set_title('measurements')
    plt.show()

def draw_result(filename='', data_x=[], data_y=[]):
        if not data_x:
            data_x = read_from_extra_file(filename)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(data_x, data_y)
        plt.show()