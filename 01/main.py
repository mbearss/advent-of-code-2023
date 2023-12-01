swap = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(l.strip() for l in f.readlines())
    s = 0
    for l in data:
        x = [c for c in l if c.isdigit()]
        s += int(x[0] + x[-1]) if len(x) > 0 else 0
    print('1:', s)

    s = 0
    for l in data:
        first, last = None, None
        for i in range(len(l)):
            for k, v in swap.items():
                if l[i].isdigit():
                    first = l[i]
                    break
                elif l[i:].startswith(k):
                    first = v
                    break
            if first:
                break
        for i in range(len(l) - 1, 0, -1):
            for k, v in swap.items():
                if l[i].isdigit():
                    last = l[i]
                    break
                elif l[i:].startswith(k):
                    last = v
                    break
            if last:
                break
        s += int(first + last) if last is not None else int(first + first)
    print('2:', s)

