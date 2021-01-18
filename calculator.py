import numpy as np


def calculate_cords(coords, m, v, delta_t, vis):
    calculate_second_row(coords, m, v, delta_t)

    for n in range(2, len(coords)):
        for i in range(len(coords[n - 1])):
            sums = calculate_sums(coords[n - 1], m, i)
            coords[n][i] = 2 * coords[n - 1][i] - coords[n - 2][i] + sums * (delta_t ** 2)
        vis.one_step(coords)


def calculate_r3(coords1, coords2):
    return ((coords1[0] - coords2[0]) ** 2 +
            (coords1[1] - coords2[1]) ** 2 +
            (coords1[2] - coords2[2]) ** 2) ** 1.5


def calculate_second_row(coords, m, v, delta_t):
    for i in range(len(coords[0])):
        sums = calculate_sums(coords[0], m, i)
        coords[1][i] = coords[0][i] + delta_t * v[i] + 0.5 * sums * (delta_t ** 2)


def calculate_sums(points, m, calculating_point_iterator):
    point = points[calculating_point_iterator]
    sums = np.zeros(3)
    for j in range(len(points)):
        if calculating_point_iterator != j:
            second_point = points[j]
            r3 = calculate_r3(point, second_point)
            sums += m[j] / r3 * (second_point - point)
    return sums
