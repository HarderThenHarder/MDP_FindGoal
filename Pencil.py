import numpy as np


class Pencil:

    @staticmethod
    def set_width_height(plt, width, height):
        """
        put this method to the end of the draw operations.
        """
        plt.xlim(0, width)
        plt.ylim(0, height)

    @staticmethod
    def stroke_line(plt, point_A=[0, 0], point_B=[0, 0], line_style='-', marker='.', color='c', alpha=1):
        plt.axis('equal')
        plt.plot([point_A[0], point_B[0]], [point_A[1], point_B[1]], linestyle=line_style, marker=marker, color=color,
                 alpha=alpha)

    @staticmethod
    def stroke_circle(plt, O=[0, 0], R=1, color='c', alpha=1, marker='.'):
        plt.axis('equal')
        theta = np.linspace(0, np.pi * 2, 300)
        circle_point_x = O[0] + R * np.cos(theta)
        circle_point_y = O[1] + R * np.sin(theta)
        plt.scatter(circle_point_x, circle_point_y, color=color, alpha=alpha, marker=marker)

    @staticmethod
    def fill_circle(plt, O=[0, 0], R=1, color='c', alpha=1):
        plt.axis('equal')
        theta = np.linspace(0, np.pi * 2, 100)
        circle_point_x = O[0] + R * np.cos(theta)
        circle_point_y = O[1] + R * np.sin(theta)
        for i in range(len(theta)):
            plt.plot([O[0], circle_point_x[i]], [O[1], circle_point_y[i]], color=color, alpha=alpha, linewidth=10)

    @staticmethod
    def stroke_rect(plt, center=[0, 0], width=1, height=1, color='c', line_style='-', alpha=1):
        plt.axis('equal')
        horn_x = [center[0] - width / 2, center[0] + width / 2, center[0] + width / 2, center[0] - width / 2,
                  center[0] - width / 2]
        horn_y = [center[1] + height / 2, center[1] + height / 2, center[1] - height / 2, center[1] - height / 2,
                  center[1] + height / 2]
        plt.plot(horn_x, horn_y, color=color, linestyle=line_style, alpha=alpha)

    @staticmethod
    def fill_rect(plt, center=[0, 0], width=1, height=1, color='c', line_style='-', alpha=1):
        plt.axis('equal')
        integrate_y = np.arange(center[1] - height / 2, center[1] + height / 2, 0.01)
        for i in range(len(integrate_y)):
            plt.plot([center[0] - width / 2, center[0] + width / 2], [integrate_y[i], integrate_y[i]], color=color,
                     linestyle=line_style, alpha=alpha, linewidth=10)
