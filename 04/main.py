import numpy as np

if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(l.strip() for l in f.readlines())
    wins = [0]
    for line in data:
        win, num = [set(map(int, x.split())) for x in line.split(':')[1].split('|')]
        wins.append(len(num.intersection(win)))

    print('1:', sum([int(2**(x-1)) for x in wins]))

    cards = list(range(1, len(wins)))
    i = 0
    while i < len(cards):
        c = cards[i]
        cards.extend(range(c+1, c+1+wins[c]))
        i += 1

    print('2:', len(cards))
