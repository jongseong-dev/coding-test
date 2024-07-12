# 0으로 붙어있는 것들이 있으면 아이스크림이라고 판단
# 아이스크림 갯수를 구하라


def solution(graph: list[list]):
    answer = 0
    for y, li in enumerate(graph):
        for x, i in enumerate(li):
            if i == 0:
                answer += 1
                dfs(li, x)
                if y + 1 < len(graph):
                    dfs(graph[y + 1], x)

    return answer


def dfs(icecream: list, start):
    for idx in range(start, len(icecream)):
        if icecream[idx] == 1:
            break
        icecream[idx] = 1


# Test case 7: Single column
assert solution([[0], [1], [0], [0], [1], [0]]) == 3

assert solution([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) == 5

assert (
    solution([[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]) == 3
)
assert solution([[0, 0, 1], [0, 0, 1], [1, 1, 1]]) == 1


# Additional test cases
# Test case 1: Empty graph
assert solution([]) == 0

# Test case 2: Single element graph
assert solution([[0]]) == 1
assert solution([[1]]) == 0

# Test case 3: All zeros
assert solution([[0, 0], [0, 0]]) == 1

# Test case 4: All ones
assert solution([[1, 1], [1, 1]]) == 0

# Test case 5: Alternating pattern


# Test case 6: Single row
assert solution([[0, 1, 0, 0, 1, 0]]) == 3


# Test case 8: Diagonal ice creams
assert solution([[0, 1, 1], [1, 0, 1], [1, 1, 0]]) == 3
