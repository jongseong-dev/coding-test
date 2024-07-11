# 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다.
# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다.
# 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.


baby_can_babbling = ["aya", "ye", "woo", "ma"]


def solution(babbling):
    answer = 0
    for ba in babbling:
        if ba:
            is_can_speak = True
            while is_can_speak:
                for can_ba in baby_can_babbling:
                    if ba.startswith(can_ba) or ba.endswith(can_ba):
                        ba = ba.replace(can_ba, "")
                    if not ba:
                        break
                is_can_speak = ba in baby_can_babbling
            if not ba:
                answer += 1
    return answer


assert solution(["aya", "yee", "u", "maa", "wyeoo"]) == 1
assert solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]) == 3
assert (
    solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa", "ayayemawoo", "umau", ""]) == 4
)
