import matplotlib.pyplot as plt
from collections import OrderedDict


def draw(first, second, title = '', size = (5, 3)):
    fig = plt.figure(figsize=size)
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(first[0], first[1], '.')
    ax.plot(second[0], second[1])
    ax.set_title(title)
    plt.show()

def title(dict):
    s = ''
    d = {'m': dict['m'], 'b0': dict['b0'], 'w': dict['w'], 'y0': dict['y0'], 'axx': dict['axx'], 'ayy': dict['ayy'], 'azz': dict['azz'], 'discr': dict['discr']}
    od = OrderedDict(sorted(d.items()))
    for i in od.items():
        s += (str(i[0]) + ' = ' + str(i[1]) + ', ')
    return s

