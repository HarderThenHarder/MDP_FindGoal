import numpy as np
from math import sin, cos, radians


class Pencil:

    @staticmethod
    def set_width_height(plt, width, height):
        """
        put this method to the end of the draw operations.
        """
        plt.xlim(0, width)
        plt.ylim(0, height)

    @staticmethod
    def stroke_line(plt, point_A=[0., 0.], point_B=[0., 0.], line_width=1, line_style='-', marker='.', color='c', alpha=1):
        plt.axis('equal')
        plt.plot([point_A[0], point_B[0]], [point_A[1], point_B[1]], linewidth=line_width, linestyle=line_style, marker=marker, color=color,
                 alpha=alpha)

    @staticmethod
    def stroke_circle(plt, O=[0., 0.], R=1, color='c', alpha=1, marker='.'):
        plt.axis('equal')
        theta = np.linspace(0, np.pi * 2, 300)
        circle_point_x = O[0] + R * np.cos(theta)
        circle_point_y = O[1] + R * np.sin(theta)
        plt.scatter(circle_point_x, circle_point_y, color=color, alpha=alpha, marker=marker)

    @staticmethod
    def fill_circle(plt, O=[0., 0.], R=1, color='c', alpha=1):
        plt.axis('equal')
        theta = np.linspace(0, np.pi * 2, 300)
        circle_point_x = O[0] + R * np.cos(theta)
        circle_point_y = O[1] + R * np.sin(theta)
        for i in range(len(theta)):
            plt.plot([O[0], circle_point_x[i]], [O[1], circle_point_y[i]], color=color, alpha=alpha, linewidth=1)

    @staticmethod
    def stroke_rect(plt, center=[0., 0.], width=1, height=1, line_width=1, color='c', line_style='-', alpha=1):
        plt.axis('equal')
        horn_x = [center[0] - width / 2, center[0] + width / 2, center[0] + width / 2, center[0] - width / 2,
                  center[0] - width / 2]
        horn_y = [center[1] + height / 2, center[1] + height / 2, center[1] - height / 2, center[1] - height / 2,
                  center[1] + height / 2]
        plt.plot(horn_x, horn_y, color=color, linestyle=line_style, alpha=alpha, linewidth=line_width)

    @staticmethod
    def fill_rect(plt, center=[0., 0.], width=1, height=1, color='c', line_style='-', alpha=1):
        plt.axis('equal')
        integrate_y = np.arange(center[1] - height / 2, center[1] + height / 2, 0.01)
        for i in range(len(integrate_y)):
            plt.plot([center[0] - width / 2, center[0] + width / 2], [integrate_y[i], integrate_y[i]], color=color,
                     linestyle=line_style, alpha=alpha, linewidth=10)

    @staticmethod
    def stroke_cross(plt, center=[0., 0.], half_length=1, line_width=1, color='c', line_style='-', alpha=1):
        plt.axis('equal')
        point_a = [center[0] + half_length * cos(radians(45)), center[1] + half_length * sin(radians(45))]
        point_b = [center[0] - half_length * cos(radians(45)), center[1] - half_length * sin(radians(45))]
        point_c = [center[0] + half_length * cos(radians(135)), center[1] + half_length * sin(radians(135))]
        point_d = [center[0] - half_length * cos(radians(135)), center[1] - half_length * sin(radians(135))]
        Pencil.stroke_line(plt, center, point_a, line_style=line_style, color=color, alpha=alpha, line_width=line_width)
        Pencil.stroke_line(plt, center, point_b, line_style=line_style, color=color, alpha=alpha, line_width=line_width)
        Pencil.stroke_line(plt, center, point_c, line_style=line_style, color=color, alpha=alpha, line_width=line_width)
        Pencil.stroke_line(plt, center, point_d, line_style=line_style, color=color, alpha=alpha, line_width=line_width)

    @staticmethod
    def stroke_arrow(plt, start_pos=[0, 0], end_pos=[1, 1], color='black', head_length=10, head_width=10, arrow_width=5):
        plt.annotate('', xy=end_pos, xytext=start_pos, arrowprops=dict(facecolor=color, headlength=head_length, headwidth=head_width, width=arrow_width))

    @staticmethod
    def write_text(plt, content='text', text_pos=[0, 0], font_size=10, color='k', font_weight='normal', font_style='normal'):
        """
        fontweight: ['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']
        fontstyle: ['normal' | 'italic' | 'oblique']
        math-term: u'$\mu-\delta$', use $...$ to express the math term like: μ, δ
        """
        plt.annotate(content, xy=text_pos, xytext=text_pos, fontsize=font_size, color=color, fontweight=font_weight, fontstyle=font_style)
