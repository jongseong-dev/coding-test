def solution(n: int, lost: list, reserve: list):
    """
    체육 수업을 들을 수 있는 학생의 최댓값을 return 해야 함
    :param n: 전체 학생수 (2<= n <= 30)
    :param lost: 체육복을 도난당한 학생 번호가 담긴 배열 (1<= len(lost) <= n, 1<= lost <= n)
    :param reserve: 여벌 체육복을 가져온 학생 번호가 담긴 배열
    :return: 체육 수업을 들을 수 있는 학생의 최댓값
    """
    lost = set(lost)
    reserve = set(reserve)
    lost_ = lost - reserve
    reserve_ = reserve - lost
    answer = n - len(lost_)
    for i in lost_:
        if i in reserve_:
            reserve_.remove(i)
            answer += 1
            continue

        pre_student = i - 1
        if pre_student in reserve_:
            reserve_.remove(pre_student)
            answer += 1
            continue

        after_student = i + 1
        if after_student in reserve_:
            reserve_.remove(after_student)
            answer += 1
            continue

    return answer


assert solution(5, [2, 4], [1, 3, 5]) == 5
assert solution(5, [2, 3], [1, 2]) == 4
assert solution(5, [2, 3], [1, 4]) == 5
assert solution(5, [1, 2, 3, 4, 5], [2, 5]) == 2
assert solution(5, [4, 5], [3, 4]) == 4
assert solution(5, [1, 2, 3], [2, 3, 4]) == 4
