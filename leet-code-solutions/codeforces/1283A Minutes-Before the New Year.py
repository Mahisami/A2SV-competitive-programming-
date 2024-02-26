t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    res = 0
    print((24 * 60) - ((a * 60) + b))
