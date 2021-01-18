import matplotlib.pyplot as plt
import numpy as np

from analizer import calculate_acceleration
from analizer import calculate_energies
from analizer import calculate_velocity


class Visualization:

    def __init__(self, frequency, d_t, x_lim, y_lim, z_lim):
        self.frequency = frequency
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.d_t = d_t
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.z_lim = z_lim
        self.iterator = 0

    def one_step(self, coords):
        if self.iterator % self.frequency == 0:
            plt.cla()
            self.ax.set_xlim(self.x_lim)
            self.ax.set_ylim(self.y_lim)
            self.ax.set_zlim(self.z_lim)
            self.ax.set_title(f"n = {self.iterator}")
            for i in range(len(coords[self.iterator])):
                self.ax.scatter(coords[self.iterator][i][0], coords[self.iterator][i][1], coords[self.iterator][i][2])
            plt.pause(0.001)
        self.iterator += 1

    def show(self, coords, scaled=True):
        plt.cla()
        if scaled:
            self.ax.set_xlim(self.x_lim)
            self.ax.set_ylim(self.y_lim)
            self.ax.set_zlim(self.z_lim)

        self.ax.set_xlabel('X Label')
        self.ax.set_ylabel('Y Label')
        self.ax.set_zlabel('Z Label')

        iterator = 0
        for n in coords:
            if iterator % self.frequency == 0:
                xs = [coord[0] for coord in n]
                ys = [coord[1] for coord in n]
                zs = [coord[2] for coord in n]
                self.ax.scatter(xs, ys, zs)
            iterator += 1
        plt.show()

    def show_velocity(self, coords, points_indexes: list = None):
        d_v = calculate_velocity(coords, self.d_t)
        self.draw_many_plots(coords, d_v, "velocity", points_indexes)

    def show_acceleration(self, coords, points_indexes: list = None):
        d_a = calculate_acceleration(coords, self.d_t)
        self.draw_many_plots(coords, d_a, "acceleration", points_indexes)

    def show_energies(self, coords, mass):
        xx, y, z = calculate_energies(coords, self.d_t, mass)

        x = np.array(range(0, len(coords) - 1))

        plt.plot(x, xx)
        plt.plot(x, y)
        plt.plot(x, z)
        plt.title('title')
        plt.ylabel('ylabel')
        plt.xlabel('xlabel')
        plt.legend()
        plt.show()
        plt.show()

    def draw_many_plots(self, coords, data, title, points_indexes=None):
        if points_indexes is None:
            points_indexes = list(range(0, len(coords[0])))

        fig, axs = plt.subplots(len(points_indexes))
        fig.suptitle(title)
        counter = 0
        x = np.array(range(0, data.shape[1]))
        for point_index in points_indexes:
            y = data[point_index]
            axs[counter].plot(x, y)
            axs[counter].set_title(point_index)
            counter += 1
        plt.show()
