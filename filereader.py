import numpy as np

x = np.fromfile('data.dat')
print(['{0:.20f}'.format(i) for i in x])
y = np.loadtxt('data.dat')