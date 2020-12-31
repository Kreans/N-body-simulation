import matplotlib.pyplot as plt


class Visualization:

    def __init__(self, frequency, x_lim, y_lim, z_lim):
        self.frequency = frequency
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
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
