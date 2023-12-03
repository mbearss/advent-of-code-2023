import re
import numpy as np

if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(l.strip() for l in f.readlines())

    parts = []
    parts_map = np.zeros((len(data[0]), len(data)))
    num_pattern = re.compile(r'\d+')
    symbol_pattern = re.compile(r'[^\.\d]')
    
    for i, line in enumerate(data):
        for p in re.finditer(num_pattern, line):
            found = False
            for y in (i-1, i, i+1):
                if y < 0 or y > len(data) - 1:
                    continue
                for x in range(p.start()-1, p.end()+1):
                    if x < 0 or x > len(line) - 1:
                        continue
                    if symbol_pattern.match(data[y][x]):
                        found = True
            if found:
                num = int(line[p.start():p.end()])
                parts.append(num)
                parts_map[i, p.start():p.end()] = num
    print('1:', sum(parts))

    gears = []
    for i, line in enumerate(data):
        for j, sym in enumerate(line):
            if sym == '*':
                adj = set()
                for y in (i-1, i, i+1):
                    if y < 0 or y > len(data) - 1:
                        continue
                    for x in (j-1, j, j+1):
                        if x < 0 or x > len(line) - 1:
                            continue
                        if parts_map[y, x] != 0:
                            adj.add(parts_map[y, x])
                if len(adj) == 2:
                    gears.append(int(adj.pop() * adj.pop()))
    print('2:', sum(gears))


