import numpy as np


def calculate_cords(coords, m, v, delta_t, vis):
    calculate_second_row(coords, m, v, delta_t)

    for n in range(2, len(coords)):
        for i in range(len(coords[n - 1])):
            sums = calculate_sums(coords, m, n, i)
            coords[n][i] = 2 * coords[n - 1][i] - coords[n - 2][i] + sums * (delta_t ** 2)
        vis.one_step(coords)


def calculate_r3(coords1, coords2):
    return ((coords1[0] - coords2[0]) ** 2 +
            (coords1[1] - coords2[1]) ** 2 +
            (coords1[2] - coords2[2]) ** 2) ** 1.5


def calculate_second_row(coords, m, v, delta_t):
    for i in range(len(coords[0])):
        sums = calculate_sums(coords, m, 1, i)
        coords[1][i] = coords[0][i] + delta_t * v[i] + 0.5 * sums * (delta_t ** 2)


def calculate_sums(coords, m, n, i):
    point = coords[n - 1][i]
    sum_x = 0
    sum_y = 0
    sum_z = 0
    for j in range(len(coords[n - 1])):
        if i != j:
            second_point = coords[n - 1][j]

            r3 = calculate_r3(point, second_point)
            sum_x += m[j] / r3 * (second_point[0] - point[0])
            sum_y += m[j] / r3 * (second_point[1] - point[1])
            sum_z += m[j] / r3 * (second_point[2] - point[2])

    return np.array([sum_x, sum_y, sum_z])
