import numpy as np


def calculate_velocity(coords, d_time):
    d_x = calculate_d_x(coords)
    d_v = d_x / d_time
    return d_v


def calculate_acceleration(coords, d_time):
    d_x = calculate_d_x(coords)
    d_a = d_x / (d_time ** 2)
    return d_a


def calculate_d_x(coords):
    epochs = len(coords)
    points = len(coords[0])
    d_x = np.zeros((points, epochs - 1))

    for n in range(epochs - 1):
        for i in range(points):
            point_a = coords[n][i]
            point_b = coords[n + 1][i]
            d_x[i][n] = np.linalg.norm(point_b - point_a)

    return d_x


def calculate_energies(coords, d_time, m):
    epochs = len(coords) - 1
    N = coords.shape[1]
    velocity = calculate_velocity(coords, d_time)
    kinetic_energy = np.zeros((epochs, 1))
    potential_energy = np.zeros((epochs, 1))

    print(epochs)
    print(kinetic_energy)
    print(kinetic_energy.shape)

    for i in range(epochs):
        kinetic_energy[i] = 1 / 2 * np.sum((velocity[:, i] ** 2 * m))

    for epoch in range(epochs):
        sum = 0
        for i in range(N):
            for j in range(i + 1, N):
                sum += m[i] * m[j] / np.linalg.norm(coords[epoch][i] - coords[epoch][j])
        potential_energy[epoch] = -sum

    total_energy = potential_energy + kinetic_energy

    return kinetic_energy, potential_energy, total_energy
