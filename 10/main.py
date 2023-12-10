import networkx as nx


def can_connect(sx, sy, dx, dy):
    if 0 <= dy < h:
        if 0 <= dx < w:
            s, d = data[sy][sx], data[dy][dx]
            if sy == dy:
                if sx == dx - 1 and s in ('-', 'L', 'F', 'S') and d in ('-', 'J', '7', 'S'):
                    return True
                if sx == dx + 1 and s in ('-', 'J', '7', 'S') and d in ('-', 'L', 'F', 'S'):
                    return True
            if sx == dx:
                if sy == dy - 1 and s in ('|', '7', 'F', 'S') and d in ('|', 'L', 'J', 'S'):
                    return True
                if sy == dy + 1 and s in ('|', 'L', 'J', 'S') and d in ('|', '7', 'F', 'S'):
                    return True


if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(l.strip() for l in f.readlines())

    G = nx.Graph()
    w, h = len(data[0]), len(data)

    source = None
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == 'S':
                source = (x, y)
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if can_connect(*(x, y), *(x + i, y + j)):
                    G.add_edge((x, y), (x + i, y + j))

    paths = nx.single_source_dijkstra(G, source)[0]
    max_node, max_len = None, 0
    for n, l in paths.items():
        if l > max_len:
            max_node, max_len = n, l

    print('1:', max_len)

    enclosed = 0
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if (x, y) in paths:
                continue
            cross = 0
            dx, dy = x, y
            while dx < w and dy < h:
                c2 = data[dy][dx]
                if (dx, dy) in paths and c2 != "L" and c2 != "7":
                    cross += 1
                dx += 1
                dy += 1
            if cross % 2 == 1:
                enclosed += 1

    print('2:', enclosed)
