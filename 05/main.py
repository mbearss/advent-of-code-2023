import math


def apply_maps(maps, seed):
    for m in maps:
        for (s, e), r in m.items():
            if s <= seed <= e:
                seed += r - s
                break
    return seed

if __name__ == '__main__':
    with open('input.txt') as f:
        data = tuple(l.strip() for l in f.readlines())
    seeds = list(map(int, data[0].split(':')[1].split()))

    maps = []
    for line in data[1:]:
        if 'map' in line:
            maps.append({})
            continue
        if len(line) == 0:
            continue
        dst, src, length = map(int, line.split())
        maps[-1][(src, src + length - 1)] = dst

    min_seed = max(seeds)
    for seed in seeds:
        min_seed = min(min_seed, apply_maps(maps, seed))
    print('1:', min_seed)

    seeds = tuple((seeds[2 * i], seeds[2 * i + 1]) for i in range(len(seeds) // 2))
    step_size = int(pow(10, math.ceil(math.log10(max(s[1] for s in seeds) // 100))))
    search_vals = {(ss, ss + sl, s): apply_maps(maps, s) for ss, sl in seeds for s in range(ss, ss + sl, step_size)}

    seed_range_start, seed_range_end, min_est = min(search_vals.items(), key=lambda x: x[1])[0]

    while step_size > 1:
        left = max(min_est - step_size, seed_range_start)
        right = min(min_est + step_size, seed_range_end)

        step_size = step_size // 10
        search_vals = {s: apply_maps(maps, s) for s in range(left, right, step_size)}
        min_est, min_seed = min(search_vals.items(), key=lambda x: x[1])

    print('2:', min_seed)

