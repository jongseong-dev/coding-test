def solution(start_point):
    """
    나이트의 이동 수단은 수직 2칸 수평 1칸 혹은 수평 1칸 수직 2칸
    :param start_point:
    :return:
    """
    knight_move = {
        "UR": (-2, 1),
        "UL": (-2, -1),
        "RU": (-1, 2),
        "RD": (1, 2),
        "DR": (2, 1),
        "DL": (2, -1),
        "LD": (1, -2),
        "LU": (-1, -2),
    }
    convert_x = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
    }[start_point[0]]
    answer = 0
    for move in knight_move:
        x = convert_x
        y = int(start_point[1])
        dx, dy = knight_move[move]
        x += dx
        y += dy
        if x < 1 or y < 1 or x > 8 or y > 8:
            continue
        answer += 1

    return answer


assert solution("a1") == 2
assert solution("c2") == 6
