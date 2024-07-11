# N X M 의 여행하기
# 시뮬레이션


def solution(n: int, plans: list[str]):
    x, y = 1, 1
    move_types = {
        "U": (-1, 0),
        "D": (1, 0),
        "R": (0, 1),
        "L": (0, -1),
    }
    for plan in plans:
        dx, dy = move_types[plan]
        nx, ny = x + dx, y + dy
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
    return x, y


assert solution(5, ["R", "R", "R", "U", "D", "D"]) == (3, 4)
