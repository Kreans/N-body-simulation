from calculator import calculate_cords
from converter import convert_points_to_vectors
from point import Point
from visualization import Visualization

T_MAX = 1
N = 1000
DELTA_T = T_MAX / N


def sample(points, n, d_t, frequency, x_lim, y_lim, z_lim):
    coords, m, v0 = convert_points_to_vectors(points, n)
    vis = Visualization(frequency, x_lim, y_lim, z_lim)
    calculate_cords(coords, m, v0, d_t, vis)
    vis.show(coords)


if __name__ == "__main__":
    print(f"Simulation Parameters: Time={T_MAX} s, time step ={DELTA_T} s")
    points = [Point([0, 0, 0], 1, [1, 0, 0]),
              Point([0, 0, 1], 1, [1, 0, 0]),
              Point([0, 0, 3], 1, [1, 0, 0]),
              Point([0, 0, 4], 1, [1, 0, 0])]

    sample(points, N, DELTA_T, 100, [-1, 1], [-1, 1], [0, 5])
