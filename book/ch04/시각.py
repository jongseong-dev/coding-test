import datetime


def solution(n):
    answer = 0
    for h in range(n + 1):
        for m in range(60):
            for s in range(60):
                dt = datetime.datetime(2022, 1, 1, h, m, s)
                dt = dt.strftime("%H:%M:%S")
                if "3" in dt:
                    answer += 1
    return answer


assert solution(5) == 11475
