import networkx as nx
from matplotlib import pyplot as plt

if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(tuple(l.strip().split(':')) for l in f.readlines())

    g = nx.Graph()
    for source, target in data:
        [g.add_edge(source, t) for t in target.split()]

    '''
    Found edges by inspection
    #pos = nx.spring_layout(g)
    #nx.draw(g, pos=pos, with_labels=True)
    #plt.show()
    '''
    edges = (('dlv', 'tqh'), ('bmd', 'ngp'), ('grd', 'tqr'))

    for s, t in edges:
        g.remove_edge(s, t)

    a = len(nx.single_source_shortest_path(g, edges[0][0]))
    b = len(nx.single_source_shortest_path(g, edges[0][1]))
    print('1:', a*b)
    print('2: 🔥')


