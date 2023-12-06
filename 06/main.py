import math
from functools import reduce


def solve(time, dist):
    root1 = ((time + ((time ** 2 - 4 * dist) ** (1 / 2))) / 2)
    root2 = ((time - ((time ** 2 - 4 * dist) ** (1 / 2))) / 2)
    return math.floor(root1) - math.ceil(root2) + 1


if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(l.strip() for l in f.readlines())
    time = tuple(map(int, data[0].split()[1:]))
    dist = tuple(map(int, data[1].split()[1:]))

    counts = [solve(time[i], dist[i]) for i in range(len(time))]
    print('1:', reduce(lambda x, y: x * y, counts))

    time_2 = int(''.join(map(str, time)))
    dist_2 = int(''.join(map(str, dist)))

    print('2', solve(int(''.join(map(str, time))), int(''.join(map(str, dist)))))
