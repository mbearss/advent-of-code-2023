from functools import cache


@cache
def solve(springs, counts, val=0):
    if not counts:
        return '#' not in springs
    first, counts = counts[0], counts[1:]
    for i in range(len(springs) - len(counts) - sum(counts) - first + 1):
        if '#' in springs[:i]:
            return val
        n = i + first
        if n <= len(springs) and '.' not in springs[i:n] and (n == len(springs) or springs[n] != '#'):
            val += solve(springs[n + 1:], counts)
    return val


if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(map(str, l.strip().split()) for l in f.readlines())

    springs, counts = zip(*data)
    counts = tuple(tuple(map(int, c.split(','))) for c in counts)

    p1, p2 = 0, 0
    for i in range(len(counts)):
        p1 += solve(springs[i], counts[i])
        p2 += solve('?'.join([springs[i]] * 5), counts[i] * 5)
    print('p1:', p1)
    print('p2:', p2)
