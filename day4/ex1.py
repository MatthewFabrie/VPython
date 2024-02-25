import numpy as np

def factorial(nb):
    res = 0
    i = 1

    if (nb % 1 == 0):
        res = 1
        while (i <= nb):
            if (nb == 1):
                res = 1
                return (res)
            res = res * i
            i += 1
        return (res)
    else:
        whole_nb = nb * 2 + 1
        res = 1
        arr = np.array([])
        for i in range(int(whole_nb)):
            arr = np.append(arr, i)
        arr = arr[::-2]
        for i in (arr):
            if (int(i) == 0):
                break
            if (int(i) != 1):
                res = res * int(i)/2
            else:
                res *= (np.sqrt(np.pi))/2
        return res

def calculate_sphere_volume(nb_dim):
    volume = (np.pi ** (nb_dim / 2)) / factorial(nb_dim / 2)
    return volume

def randpoints(num_points, j):
    rand_x = np.random.uniform(-1, 1, num_points)
    rand_y = np.random.uniform(-1, 1, num_points)
    rand_1 = 0
    rand_2 = 0
    rand_3 = 0
    rand_4 = 0
    rand_5 = 0
    rand_6 = 0
    rand_7 = 0
    rand_8 = 0
    rand_9 = 0
    rand_10 = 0
    rand_11 = 0
    rand_12 = 0
    rand_13 = 0
    rand_14 = 0
    rand_15 = 0
    rand_16 = 0
    rand_17 = 0
    rand_18 = 0
    if (j >= 3):
        rand_1 = np.random.uniform(-1, 1, num_points)
    if (j >= 4):
        rand_2 = np.random.uniform(-1, 1, num_points)
    if (j >= 5):
        rand_3 = np.random.uniform(-1, 1, num_points)
    if (j >= 6):
        rand_4 = np.random.uniform(-1, 1, num_points)
    if (j >= 7):
        rand_5 = np.random.uniform(-1, 1, num_points)
    if (j >= 8):
        rand_6 = np.random.uniform(-1, 1, num_points)
    if (j >= 9):
        rand_7 = np.random.uniform(-1, 1, num_points)
    if (j >= 10):
        rand_8 = np.random.uniform(-1, 1, num_points)
    if (j >= 11):
        rand_9 = np.random.uniform(-1, 1, num_points)
    if (j >= 12):
        rand_10 = np.random.uniform(-1, 1, num_points)
    if (j >= 13):
        rand_11 = np.random.uniform(-1, 1, num_points)
    if (j >= 14):
        rand_12 = np.random.uniform(-1, 1, num_points)
    if (j >= 15):
        rand_13 = np.random.uniform(-1, 1, num_points)
    if (j >= 16):
        rand_14 = np.random.uniform(-1, 1, num_points)
    if (j >= 17):
        rand_15 = np.random.uniform(-1, 1, num_points)
    if (j >= 18):
        rand_16 = np.random.uniform(-1, 1, num_points)
    if (j >= 19):
        rand_17 = np.random.uniform(-1, 1, num_points)
    if (j >= 20):
        rand_18 = np.random.uniform(-1, 1, num_points)

    distances = 0
    distances = np.sqrt(rand_x**2 + rand_y**2 + rand_1**2 + rand_2**2 + rand_3**2 + rand_4**2 + rand_5**2 + rand_6**2 + rand_7**2 + rand_8**2 + rand_9**2 + rand_10**2 + rand_11**2 + rand_12**2 + rand_13**2 + rand_14**2 + rand_15**2 + rand_16**2 + rand_17**2 + rand_18**2)
    return np.sum(distances <= 1)

file = open("ex1.txt", "w")

for j in range(2, 21):
    num_points_inside = randpoints(10**6, j)
    rslt = (2**j) * (num_points_inside / 10**6)
    file.write(f"{j}) {rslt}, {rslt/calculate_sphere_volume(j)}, {num_points_inside}\n")

file.close()