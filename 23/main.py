import networkx as nx


pmap = {'>': (-1, 0), '<': (1, 0), '^': (0, 1), 'v': (0, -1)}
if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(tuple(l.strip()) for l in f.readlines())

    M, N = len(data[0]), len(data)
    source = ([i for i, c in enumerate(data[0]) if c == '.'][0], 0)
    target = ([i for i, c in enumerate(data[N - 1]) if c == '.'][0], N - 1)

    g1 = nx.grid_2d_graph(M, N, create_using=nx.DiGraph)
    g2 = nx.grid_2d_graph(M, N)

    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == '#':
                g1.remove_node((x, y))
                g2.remove_node((x, y))
            elif c in pmap:
                i, j = pmap[c]
                g1.remove_edge((x, y), (x + i, y + j))

    print('1:', max(map(len, nx.all_simple_edge_paths(g1, source, target))))

    for u in [u for u in g2.nodes if len(g2.edges(u)) == 2]:
        v1, v2 = list(g2.neighbors(u))
        nw = sum(g2.edges[u, v].get("d", 1) for v in (v1, v2))
        g2.add_edge(v1, v2, d=nw)
        g2.remove_node(u)

    print('2:', max(nx.path_weight(g2, path, "d") for path in nx.all_simple_paths(g2, source, target)))

