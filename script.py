import matplotlib
import math
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt


def rotate_around_x(matrix, ang):
    m = np.array([[1, 0, 0], [0, math.cos(ang), - math.sin(ang)], [0, math.sin(ang), math.cos(ang)]])
    return np.matmul(m, matrix)


def rotate_around_y(matrix, ang):
    m = np.array([[math.cos(ang), 0, math.sin(ang)], [0, 1, 0], [-math.sin(ang), 0, math.cos(ang)]])
    return np.matmul(m, matrix)

def rotate_around_z(matrix, ang):
    m = np.array([[math.cos(ang), - math.sin(ang), 0], [math.sin(ang),  math.cos(ang), 0], [0, 0, 1]])
    return np.matmul(m, matrix)

def gauss(m, h0, w, y0, hlocz, h):
    delta_h = h - (h0 + hlocz)
    print(hlocz)
    power = -((delta_h ** 2) / (2 * (w ** 2)))
    y = y0 + m * math.e ** power
    print ("power", power)
    return y

def get_rotation_matrix(x, y, z): # Из книжки
    return  np.array([[math.cos(x) * math.cos(y) * math.cos(z) - math.sin(x) * math.sin(z),
                     -math.sin(x) * math.cos(z) - math.cos(x) * math.cos(y) * math.sin(z),
                     math.cos(x) * math.sin(y)],

                    [math.sin(x) * math.cos(y) * math.cos(z) + math.cos(x) * math.sin(z),
                     math.cos(x) * math.cos(z) - math.sin(x) * math.cos(y) * math.sin(z),
                     math.sin(x) * math.sin(y)],

                    [-math.sin(y) * math.cos(z),
                     math.sin(y) * math.sin(z),
                     math.cos(y)]])

def euler (matrix, x, y, z):
    rot = get_rotation_matrix(x, y, z)
    # rot_inv = get_rotation_matrix(-z, -y, -x)
    res = np.matmul(rot, matrix)
    rot_inv = rot.transpose()
    # if (rot_inv == get_rotation_matrix(-z, -y, -x)):
    # print ("TRANSPOSED:\n", rot_inv, "\n")
    # print("INVERSED:\n", get_rotation_matrix(-z, -y, -x), "\n")

    res = np.matmul(res, rot_inv)
    return res



def rotate(matrix, x, y, z):
    matrix = rotate_around_x(matrix, x)
    matrix = rotate_around_y(matrix, y)
    matrix = rotate_around_z(matrix, z)
    return matrix

def rotate_diag(axx, ayy, azz, x, y, z):
    return euler(diagonal(axx, ayy, azz), x, y, z)

def calculate_hlocz(s0, b):
    # res = np.matmul(np.array([0, 0, s0]), np.asarray(b)) на бумажке
    # res = np.matmul(np.asarray(b), np.array([0, 0, s0])) # в книге
    res = np.matmul(np.asarray(b), np.array([[0], [0], [s0]]))
    # print (res)
    res = res[2]
    return res


def diagonal(ax, ay, az):
    return np.array([[ax, 0, 0], [0, ay, 0], [0, 0, az]])

# m, h0, w, y0, axx, ayy, azz, s0, x, y, z,
def super(x, y, z, h, param):
    m = param[0]
    h0 = param[1]
    w = param[2]
    y0 = param[3]
    axx = param[4]
    ayy = param[5]
    azz = param[6]
    s0 = param[7]

    b = rotate_diag(axx, ayy, azz, x, y, z)
    hlocz = calculate_hlocz(s0, b)
    res = gauss(m, h0, w, y0, hlocz, h)
    return res


def integr(data_x, param):
    res = []
    sum = 0
    pp = math.pi * 2
    for h in data_x:
        for x in range(40):
            for y in range(40):
                for z in range(40):
                    sum += super(x * (pp/40), y * (pp/40), z * (pp/40), h, param)
        res.append(sum)
        sum = 0
    return res


# m, h0, w, y0, axx, ayy, azz, s0
#param = (1, 50, 1, 0, 20, 20, -30, 1)
param = (1, 50, 8, 0, 20, 20, -30, 1)

fig = plt.figure()

data_x = [x*5 for x in range(21)]
data_y = integr(data_x, param)

# print(data_y)

# data_y = [integrate.tplquad(super, 0.0, pp, 0.0, pp, 0.0, pp, args=(h, param))[0] for h in data_x]
# data_y = [gauss(1, 50, 15, 0, hlocz, x) for x in data_x]


plt.plot(data_x, data_y)

plt.show()