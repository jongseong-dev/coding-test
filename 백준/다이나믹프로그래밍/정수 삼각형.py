import sys

N = int(sys.stdin.readline())
T = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

d = [[0] for _ in range(N)]

d[0][0] = T[0][0]

for i in range(1, N):
    length = len(T[i])
    d[i][0] = d[i - 1][0] + T[i][0]
    for idx in range(1, length - 1):
        d[i].append(max(d[i - 1][idx - 1], d[i - 1][idx]) + T[i][idx])
    d[i].append(d[i - 1][-1] + T[i][-1])

print(max(d[N - 1]))
