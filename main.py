from Algorathim import GridWorld
from Pencil import Pencil
import matplotlib.pyplot as plt


def main():
    i = 0
    n_iters =1
    world = GridWorld()

    while i < n_iters:
        world.calculate_v()
        i += 1

    for i in range(5):
        print('%.2f' % world.v_states[i], end=' | ')
    print()
    for i in range(5, 8):
        print('%.2f' % world.v_states[i], end=' | ')
        print('        ', end='')

    print()

    world.calculate_pi()
    for i in range(5):
        print(world.pi_star[i], end=' | ')
    print()
    for i in range(5, 8):
        print(world.pi_star[i], end=' | ')
        print('    ', end='')

    draw(world)


def draw(word):
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
    Pencil.stroke_cross(plt, grid_center[5], half_length=10, line_width=2, color='r')
    Pencil.stroke_cross(plt, grid_center[7], half_length=10, line_width=2, color='r')
    Pencil.fill_circle(plt, grid_center[6], R=9.5, color='y')

    Pencil.stroke_arrow(plt, grid_center[0], grid_center[1])

    plt.show()


if __name__ == '__main__':
    main()
