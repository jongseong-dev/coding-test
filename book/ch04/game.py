def solution(m, n, point: list[int, int, int], area: list[list[int]]):
    """

    :param m: 가로 크기
    :param n: 세로 크기
    :param point: 캐릭터가 위치한 곳과 방향을 알려줌
    :return:
    """
    map_ = [[1] * (n + 2) for _ in range(m + 2)]
    for i in range(m):
        for j in range(n):
            map_[i + 1][j + 1] = area[i][j]
    x, y, d = point
    x, y = x + 1, y + 1
    d = change_direction(d)  # 현재 방향을 기준으로 왼쪽으로 돌림
    move_type = {
        0: (0, -1),  # 북
        1: (-1, 0),  # 서
        2: (0, 1),  # 남
        3: (1, 0),  # 동
    }
    fail = 0  # 돌아간 방향 횟수
    answer = 1
    map_[y][x] = 1
    while True:
        dx, dy = move_type[d]
        nx, ny = x + dx, y + dy
        if fail == 4:
            x, y = x - dx, y - dy
            if map_[y][x] == 1:
                break
            d = change_direction(d)
            fail = 0
            continue
        if map_[ny][nx] == 1:  # 바다 혹은 이미 가본 곳
            # 만약 그렇다면 한칸 왼쪽으로 돌린다.
            d = change_direction(d)  # 방향을 돌림
            fail += 1
            continue
        else:  # 가보지 않은 곳
            x, y = nx, ny
            answer += 1
            map_[y][x] = 1
            fail = 0
            continue
    return answer


def change_direction(d):
    return (d + 1) % 4


assert (
    solution(
        4,
        4,
        [1, 1, 0],
        [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
        ],
    )
    == 3
)

assert (
    solution(
        4,
        4,
        [1, 1, 0],
        [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
        ],
    )
    == 4
)

assert (
    solution(
        4,
        4,
        [1, 1, 0],
        [
            [1, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
        ],
    )
    == 4
)
