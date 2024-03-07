from collections import defaultdict;
t = int(input())
for _ in range(t):
    n = int(input())
    ss = input()
    pref = 0
    res = 0
    d = defaultdict(int)
    d[0] = 1
    for i in range(n):
        pref += int(ss[i])
        d[pref - i - 1] += 1
        res += d[pref - i - 1] - 1
    print(res)
