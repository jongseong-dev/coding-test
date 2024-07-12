# 미로 탈출
# 괴물이 있으면 0
# 없으면 1
# 출구는 (N, M)
# 최단 경로 구하기
# 노드를 방문할 때마다 +1 씩 증가시키고 만약 가로막혀있다면 -1 로 되돌아오게끔 하면 될듯
# stack에 담자
from collections import deque


def solution(graph: list[list], current_position: tuple = (0, 0)) -> int:
    move_direction = {
        0: (0, -1),  # 위로
        1: (0, 1),  # 아래로
        2: (-1, 0),  # 왼쪽
        3: (1, 0),  # 오른쪽
    }
    queue = deque()
    queue.append(current_position)
    while queue:
        x, y = queue.popleft()
        for direction in move_direction.values():
            nx = x + direction[0]
            ny = y + direction[1]
            if nx < 0 or ny < 0 or nx >= len(graph) or ny >= len(graph[0]):
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[len(graph) - 1][len(graph[-1]) - 1]


assert solution([[1, 1, 0], [0, 1, 0], [0, 1, 1]]) == 5
assert solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 5
graph = [
    [1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1],
]

assert solution(graph) == 11
