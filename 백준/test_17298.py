# 문제
# 크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.
#
# 예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

n = int(input())
args = list(map(int, input().split(" ")))

n = 4
args = [3, 5, 2, 7]
search_index_stack = []
answer = [-1] * n


def solution(n: int, text_list: list[str]) -> int:
    for i in range(n):
        while search_index_stack and text_list[i] > text_list[search_index_stack[-1]]:
            index = search_index_stack.pop()
            answer[index] = text_list[i]

        search_index_stack.append(i)

    return answer


print(*solution(n, args))
