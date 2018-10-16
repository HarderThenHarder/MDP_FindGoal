from Algorathim import GridWorld
from Pencil import Pencil
import matplotlib.pyplot as plt


def main():
    i = 0
    n_iters = 5
    world = GridWorld()
    draw_v(world)

    while i < n_iters:
        world.calculate_v()
        draw_v(world)
        world.calculate_pi()
        draw_pi(world)
        i += 1

    # for i in range(5):
    #     print('%.2f' % world.v_states[i], end=' | ')
    # print()
    # for i in range(5, 8):
    #     print('%.2f' % world.v_states[i], end=' | ')
    #     print('        ', end='')
    #
    # print()
    #
    # world.calculate_pi()
    # for i in range(5):
    #     print(world.pi_star[i], end=' | ')
    # print()
    # for i in range(5, 8):
    #     print(world.pi_star[i], end=' | ')
    #     print('    ', end='')


def draw_v(world):
    # write title
    plt.grid(True, alpha=0.1, color='k', linestyle='--', linewidth=2)
    Pencil.write_text(plt, "GridWorld-SearchGoal-v0", [18, 50], font_weight='bold', font_size=15)

    # draw grid word
    Pencil.stroke_line(plt, [0, 40], [100, 40], line_width=2, color='black')
    Pencil.stroke_line(plt, [0, 20], [100, 20], line_width=2, color='black')
    Pencil.stroke_line(plt, [0, 0], [0, 40], line_width=2, color='black')
    Pencil.stroke_line(plt, [20, 0], [20, 40], line_width=2, color='black')
    Pencil.stroke_line(plt, [0, 0], [20, 0], line_width=2, color='black')
    Pencil.stroke_line(plt, [40, 0], [40, 40], line_width=2, color='black')
    Pencil.stroke_line(plt, [60, 0], [60, 40], line_width=2, color='black')
    Pencil.stroke_line(plt, [40, 0], [60, 0], line_width=2, color='black')
    Pencil.stroke_line(plt, [80, 0], [80, 40], line_width=2, color='black')
    Pencil.stroke_line(plt, [100, 0], [100, 40], line_width=2, color='black')
    Pencil.stroke_line(plt, [80, 0], [100, 0], line_width=2, color='black')

    # calculate the center of grid
    grid_center = [[10, 30], [30, 30], [50, 30], [70, 30], [90, 30], [10, 10], [50, 10], [90, 10]]

    # draw end area
    Pencil.stroke_cross(plt, grid_center[5], half_length=10, line_width=4, color='r')
    Pencil.stroke_cross(plt, grid_center[7], half_length=10, line_width=4, color='r')
    Pencil.fill_circle(plt, grid_center[6], R=9.5, color='y')

    for i in range(len(grid_center)):
        Pencil.write_text(plt, "%.2f" % world.v_states[i], [grid_center[i][0] - 6, grid_center[i][1] - 1],
                          font_weight='normal', font_size=13, color='g')

    plt.show()


def draw_direction(center_pos, direction):
    if direction == 'n':
        Pencil.stroke_arrow(plt, center_pos, [center_pos[0], center_pos[1] + 10], arrow_width=3, head_width=6)
    elif direction == 'e':
        Pencil.stroke_arrow(plt, center_pos, [center_pos[0] + 10, center_pos[1]], arrow_width=3, head_width=6)
    elif direction == 's':
        Pencil.stroke_arrow(plt, center_pos, [center_pos[0], center_pos[1] - 10], arrow_width=3, head_width=6)
    elif direction == 'w':
        Pencil.stroke_arrow(plt, center_pos, [center_pos[0] - 10, center_pos[1]], arrow_width=3, head_width=6)


def draw_pi(world):
    # write title
    plt.grid(True, alpha=0.1, color='k', linestyle='--', linewidth=2)
    Pencil.write_text(plt, "GridWorld-SearchGoal-v0", [18, 50], font_weight='bold', font_size=15)

    # draw grid word
    Pencil.stroke_line(plt, [0, 40], [100, 40], line_width=2, color='black')
    Pencil.stroke_line(plt, [0, 20], [100, 20], line_width=2, color='black')
    Pencil.stroke_line(plt, [0, 0], [0, 40], line_width=2, color='black')
    Pencil.stroke_line(plt, [20, 0], [20, 40], line_width=2, color='black')
    Pencil.stroke_line(plt, [0, 0], [20, 0], line_width=2, color='black')
    Pencil.stroke_line(plt, [40, 0], [40, 40], line_width=2, color='black')
    Pencil.stroke_line(plt, [60, 0], [60, 40], line_width=2, color='black')
    Pencil.stroke_line(plt, [40, 0], [60, 0], line_width=2, color='black')
    Pencil.stroke_line(plt, [80, 0], [80, 40], line_width=2, color='black')
    Pencil.stroke_line(plt, [100, 0], [100, 40], line_width=2, color='black')
    Pencil.stroke_line(plt, [80, 0], [100, 0], line_width=2, color='black')

    # calculate the center of grid
    grid_center = [[10, 30], [30, 30], [50, 30], [70, 30], [90, 30], [10, 10], [50, 10], [90, 10]]

    # draw end area
    Pencil.stroke_cross(plt, grid_center[5], half_length=10, line_width=4, color='r')
    Pencil.stroke_cross(plt, grid_center[7], half_length=10, line_width=4, color='r')
    Pencil.fill_circle(plt, grid_center[6], R=9.5, color='y')

    for i in range(len(grid_center)):
        draw_direction(grid_center[i], world.pi_star[i])

    plt.show()


if __name__ == '__main__':
    main()
