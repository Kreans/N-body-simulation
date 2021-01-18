from calculator import calculate_cords
from converter import convert_points_to_vectors
from point import Point
from visualization import Visualization

T_MAX = 0.85
N = 30
DELTA_T = T_MAX / N


def sample(points, n, d_t, frequency, x_lim, y_lim, z_lim):
    coords, m, v0 = convert_points_to_vectors(points, n)
    vis = Visualization(frequency, d_t, x_lim, y_lim, z_lim)
    calculate_cords(coords, m, v0, d_t, vis)
    vis.show(coords)
    vis.show_velocity(coords)
    vis.show_acceleration(coords)
    vis.show_energies(coords, m)


if __name__ == "__main__":
    # print(f"Simulation Parameters: Time={T_MAX} s, time step ={DELTA_T} s")
    # points = [Point([0, 0, 0], 1, [1, 0, 0]),
    #           Point([0, 0, 1], 1, [1, 0, 0]),
    #           Point([0, 0, 3], 1, [1, 0, 0]),
    #           Point([0, 0, 4], 1, [1, 0, 0])]
    # T_MAX = 0.85
    # N = 30
    # DELTA_T = T_MAX / N
    # sample(points, N, DELTA_T, 1, [-1, 1], [-1, 1], [0, 5])

    # points = [Point([0, 0, 0], 10 ** 3, [0, 0, 0]),
    #            Point([10, 0, 0], 1, [5, 5, 0]),
    #           Point([-10, 0, 10], 1, [-5, -5, 0])]

    # second sample
    # points = [Point([0, 0, 0], 10 ** 3, [0, 0, 0]),
    #           Point([10, 0, -10], 1, [5, 5, 0]),
    #           Point([-10, 0, 10], 1, [-5, -5, 0])]
    # T_MAX = 100.85
    # N = 300000
    # DELTA_T = T_MAX / N
    #   sample(points, N, DELTA_T, 1000, [-20, 20], [-20, 20], [-20, 20])

    # third sample
    points = [Point([0, 0, 0], 10 ** 10, [0.1, 0, 0]),
              Point([-5000, 0, 0], 1, [0, 1300, 0])]

    T_MAX = 100.85
    N = 300000
    DELTA_T = T_MAX / N
    sample(points, N, DELTA_T, 1000, [-5000, 5000], [-5000, 5000], [-5000, 50000])
