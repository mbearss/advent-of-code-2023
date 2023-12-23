from collections import defaultdict


def drop(brick):
    return (brick[0][0], brick[0][1], brick[0][2] - 1), (brick[1][0], brick[1][1], brick[1][2] - 1)


def positions(brick):
    for x, y, z in [(x, y, z) for z in range(brick[0][2], brick[1][2] + 1)
                    for y in range(brick[0][1], brick[1][1] + 1)
                    for x in range(brick[0][0], brick[1][0] + 1)]:
        yield (x, y, z)


def disintegrate(brick):
    falling = set()

    def falls(brick):
        if brick in falling:
            return
        falling.add(brick)
        for parent in above[brick]:
            if not len(below[parent] - falling):
                falls(parent)

    falls(brick)
    return len(falling)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(tuple([tuple(map(int, x.split(','))) for x in l.strip().split('~')]) for l in f.readlines())

    occupied = {}
    fallen = []
    for brick in sorted(data, key=lambda brick: brick[0][2]):
        while brick[0][2] > 0 and all(pos not in occupied for pos in positions(drop(brick))):
            brick = drop(brick)
        for pos in positions(brick):
            occupied[pos] = brick
        fallen.append(brick)

    above = defaultdict(set)
    below = defaultdict(set)
    for brick in fallen:
        bpos = set(positions(brick))
        for pos in positions(drop(brick)):
            if pos in occupied and pos not in bpos:
                above[occupied[pos]].add(brick)
                below[brick].add(occupied[pos])

    p1, p2 = 0, 0
    for brick in fallen:
        count = disintegrate(brick)
        p1 += count == 1
        p2 += count - 1

    print('1:', p1)
    print('2:', p2)
