# 선물을 직접 전하기 힘들 때 카카오톡 선물하기 기능을 이용해 축하 선물을 보낼 수 있습니다.
# 당신의 친구들이 이번 달까지 선물을 주고받은 기록을 바탕으로 다음 달에 누가 선물을 많이 받을지 예측하려고 합니다.

# Case 1
# 두 사람이 선물을 주고받은 기록이 있다면, 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.
# 예를 들어 A가 B에게 선물을 5번 줬고, B가 A에게 선물을 3번 줬다면 다음 달엔 A가 B에게 선물을 하나 받습니다.
# 선물 준 횟수 A > B -> 다음달에 A가 B에게 선물 받음

# Case 2
# 두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면, 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.
# 선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값입니다.
# 예를 들어 A가 친구들에게 준 선물이 3개고 받은 선물이 10개라면 A의 선물 지수는 -7입니다.
# B가 친구들에게 준 선물이 3개고 받은 선물이 2개라면 B의 선물 지수는 1입니다.
# 만약 A와 B가 선물을 주고받은 적이 없거나 정확히 같은 수로 선물을 주고받았다면, 다음 달엔 B가 A에게 선물을 하나 받습니다.
# 이번달 A의 선물지수 = A가 준 선물 갯수 - A가 받은 선물 개수 -> -7
# 이번달 B의 선물지수 = B가 준 선물 갯수 - B가 받은 선물 개수 -> 1
# 다음달에 B가  A에게 받음
# 만약 이 마저도 같다면 선물을 받지 못함

# 위에서 설명한 규칙대로 다음 달에 선물을 주고받을 때, 당신은 선물을 가장 많이 받을 친구가 받을 선물의 수를 알고 싶습니다
#
from collections import defaultdict
from itertools import combinations


# 준 것과 받은 것은 list 의 역순이다.
def solution(friends, gifts):
    total = {}
    result = defaultdict(int)
    perm = list(combinations(friends, 2))

    for p in perm:
        str_p = " ".join(p)
        str_reversed_p = " ".join(reversed(p))
        give_count = gifts.count(str_p)
        receive_count = gifts.count(str_reversed_p)
        giver = p[0]
        receiver = p[1]
        if give_count > receive_count:
            if giver in result:
                result[giver] += 1
            else:
                result[giver] = 1
        if give_count < receive_count:
            if receiver in result:
                result[receiver] += 1
            else:
                result[receiver] = 1

        if giver not in total:
            giver_give_count = sum(1 for x in gifts if x.split()[0] == giver)
            giver_receive_count = sum(1 for x in gifts if x.split()[-1] == giver)
            giver_total_count = giver_give_count - giver_receive_count
            total[giver] = giver_give_count - giver_receive_count

        if receiver not in total:
            receiver_give_count = sum(1 for x in gifts if x.split()[0] == receiver)
            receiver_receive_count = sum(1 for x in gifts if x.split()[-1] == receiver)
            receiver_total_count = receiver_give_count - receiver_receive_count
            total[receiver] = receiver_give_count - receiver_receive_count

        if give_count == receive_count:
            if total[giver] > total[receiver]:
                result[giver] += 1
            if total[giver] < total[receiver]:
                result[receiver] += 1
        try:
            [gifts.remove(str_p) for _ in range(give_count)]
        except ValueError:
            pass
        try:
            [gifts.remove(str_reversed_p) for _ in range(receive_count)]
        except ValueError:
            pass

    answer = max(result.values() or [0])
    return answer


assert (
    solution(
        ["muzi", "ryan", "frodo", "neo"],
        [
            "muzi frodo",
            "muzi frodo",
            "ryan muzi",
            "ryan muzi",
            "ryan muzi",
            "frodo muzi",
            "frodo ryan",
            "neo muzi",
        ],
    )
    == 2
)
assert (
    solution(
        ["joy", "brad", "alessandro", "conan", "david"],
        [
            "alessandro brad",
            "alessandro joy",
            "alessandro conan",
            "david alessandro",
            "alessandro david",
        ],
    )
    == 4
)
assert solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]) == 0
assert solution(["a", "b", "c"], ["a b", "b a"]) == 0
assert solution(["a", "b", "c"], ["a b", "c a"]) == 2
