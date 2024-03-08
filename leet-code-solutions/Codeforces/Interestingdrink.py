from bisect import bisect_right

t = int(input())
li = list(map(int, input().split()))
li.sort()
n = int(input())

for i in range(n):
    a = int(input())

    val = bisect_right(li,a)
    print(val)