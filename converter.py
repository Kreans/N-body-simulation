import numpy as np


def convert_points_to_vectors(points: list, n: int):
    m = np.array([point.m for point in points])
    v0 = np.array([point.v for point in points])
    coords = np.zeros((n, len(points), 3))
    coords[0] = np.array([point.coords for point in points])
    return coords, m, v0
