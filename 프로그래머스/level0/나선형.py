# 출처: https://school.programmers.co.kr/learn/courses/30/lessons/181832
# 문제를 풀지 못함


def solution(n):
    answer = [[0] * n for _ in range(n)]
    moves = {
        0: (1, 0),  # 오른쪽
        1: (0, 1),  # 아래
        2: (-1, 0),  # 왼쪽
        3: (0, -1),  # 위
    }
    # 벽을 만나면 오른쪽 -> 아래 -> 왼쪽 -> 위 -> 오른쪽 -> 아래 -> 왼쪽 -> 위를 반복한다.
    idx = 1
    x, y = 0, 0
    move_type = 0
    answer[0][0] = idx
    while True:
        if idx == n * n:
            break
        move_type = move_type % 4
        move = moves[move_type]
        dx, dy = move
        nx, ny = x + dx, y + dy
        if nx >= n or nx < 0 or ny < 0 or ny >= n or answer[ny][nx] > 0:
            move_type += 1
            continue
        answer[ny][nx] = idx + 1
        x, y = nx, ny
        idx += 1

    return answer


assert solution(4) == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
