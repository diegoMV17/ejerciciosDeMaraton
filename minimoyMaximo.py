def find_lcm_pairs(t, test_cases):
    results = []
    for l, r in test_cases:
        if 2 * l <= r:
            results.append((l, 2 * l))
        else:
            results.append((-1, -1))
    return results

t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

results = find_lcm_pairs(t, test_cases)
for x, y in results:
    print(x, y)