import numpy as np


def solve(root, part2=False):
    count = 0
    while part2 and not root[-1] == 'Z' or not part2 and root != 'ZZZ':
        d = route[count % len(route)]
        root = graph[root][0 if d == 'L' else 1]
        count += 1
    return count


if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(l.strip().split() for l in f.readlines())

    route = data[0][0]
    graph = {line[0]: (line[2][1:-1], line[3][:-1]) for line in data[2:]}

    print('1:', solve('AAA'))
    print('2:', np.lcm.reduce([solve(r, part2=True) for r in [n for n in graph if n[-1] == 'A']]))
