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


"""
문제를 풀 때 각 경로에서 최대값을 구한 뒤 그 값을 저장해놓고 다음 경로에서 그 값을 이용해 최대값을 구하는 방식으로 풀었다.
그리하여 경로마다 최대값을 저장하는 `d` 리스트를 만들었다.
"""
