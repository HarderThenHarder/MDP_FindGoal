from Algorathim import GridWorld


def main():
    i = 0
    n_iters = 10
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


if __name__ == '__main__':
    main()
