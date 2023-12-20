from collections import defaultdict
from math import lcm

import networkx as nx
import numpy as np


class Gate():
    def handle(self, x, _):
        return x


class FF(Gate):
    def __init__(self):
        self.mem = 0

    def handle(self, x, _):
        if x == 0:
            self.mem = 0 if self.mem == 1 else 1
            return self.mem
        return None


class Con(Gate):
    def __init__(self):
        self.mem = defaultdict(lambda: 0)
        self.n = 0

    def handle(self, x, n):
        self.mem[n] = x
        return 0 if sum(self.mem.values()) == self.n else 1


def run(i):
    p = [1, 0]
    q = [('broadcaster', 0, 'button')]
    while q:
        (n, x, s) = q.pop(0)
        if n in g:
            x = g[n].handle(x, s)
            if x is not None:
                for ne in G.neighbors(n):
                    q.append((ne, x, n))
                    p[x] += 1
                if n in rx_in:
                    if x == 1 and n not in rx_conj_p:
                        rx_conj_p[n] = i + 1
    return tuple(p)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(l.strip() for l in f.readlines())
    G = nx.DiGraph()
    g = {'broadcaster': Gate()}
    for line in data:
        s, d = [n.strip() for n in line.split('->')]
        if s == 'broadcaster':
            for n in d.split(','):
                G.add_edge(s, n.strip())
        else:
            for n in d.split(','):
                G.add_edge(s[1:], n.strip())
            if s[0] == '%':
                g[s[1:]] = FF()
            elif s[0] == '&':
                g[s[1:]] = Con()

    for n, c in G.in_degree():
        if n in g and isinstance(g[n], Con):
            g[n].n = c

    rx_conj_p = {}
    rx_in = [n[0] for n in G.in_edges(list(G.in_edges('rx'))[0][0])]

    p = np.zeros(2, dtype=int)
    for i in range(1000):
        p += run(i)
    print('1:', p[0] * p[1])

    while len(rx_conj_p) < 4:
        i += 1
        run(i)

    print('2:', lcm(*rx_conj_p.values()))
