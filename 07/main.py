import functools

card_val = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def get_class(hand, part2=False):
    if part2:
        j = hand.count('J')
        hand = hand.replace('J', '')
    counts = sorted([hand.count(uc) for uc in set(hand)], reverse=True)
    counts.extend([0, 0])
    return (counts[0] + (j if part2 else 0)) * 2 + (1 if counts[1] == 2 else 0)


def handle_tie(hand1, hand2):
    for i in range(5):
        if hand1[i] != hand2[i]:
            return card_val[hand1[i]] - card_val[hand2[i]]
    return 0


def compare(hand1, hand2):
    c1, c2 = get_class(hand1), get_class(hand2)
    if c1 != c2:
        return c1 - c2
    return handle_tie(hand1, hand2)


def compare2(hand1, hand2):
    c1, c2 = get_class(hand1, part2=True), get_class(hand2, part2=True)
    if c1 != c2:
        return c1 - c2
    return handle_tie(hand1, hand2)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(l.strip().split() for l in f.readlines())

    hands, bids = zip(*data)
    bid_map = {hands[i]: int(bids[i]) for i in range(len(hands))}

    x = sorted(hands, key=functools.cmp_to_key(compare))
    score = sum([(i + 1) * bid_map[x[i]] for i in range(len(hands))])
    print('1:', score)

    card_val['J'] = 1
    x = sorted(hands, key=functools.cmp_to_key(compare2))
    score = sum([(i + 1) * bid_map[x[i]] for i in range(len(hands))])
    print('2:', score)
