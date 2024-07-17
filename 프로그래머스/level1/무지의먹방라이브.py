# https://school.programmers.co.kr/learn/courses/30/lessons/42891
# 해당 문제는 못풀어서 하나씩 코드를 돞아보기 함
# 일단 원리는 이렇다. 먹는 시간이 가장 적은 음식부터 먹도록 코드를 짜는데, 이 원리는 어차피 한 사이클을 돌면 하나씩 다 빠진다.
# 즉 가장 적게 먹는 시간으로 정렬을 해서 계산을 하더라도 나중에 정답을 구할 때만 이 부분을 계산에 넣어서 다음 음식을 구하면 된다.
# 나는 이 부분이 선뜻 이해가 안갔는데 코드를 보다보니 이해가 되는 것 같기도하다.
# 마지막에 구하누ㅡ
import heapq  # 우선순위 큐를 사용하기 위한 heapq 모듈을 임포트합니다.


def solution(food_times, k):
    # 전체 음식을 먹는 시간의 합이 k 이하면 모든 음식을 다 먹은 후이므로 -1을 반환합니다.
    if sum(food_times) <= k:
        return -1

    # 우선순위 큐를 초기화합니다.
    q = []
    # 각 음식에 대해 (먹는데 필요한 시간, 음식 번호)의 형태로 우선순위 큐에 추가합니다.
    for i, food in enumerate(food_times):
        heapq.heappush(q, (food, i + 1))

    sum_value = 0  # 현재까지 먹는데 사용한 총 시간을 저장합니다.
    previous = 0  # 이전에 다 먹은 음식의 시간을 저장합니다.
    length = len(food_times)  # 남은 음식의 개수를 저장합니다.

    # 현재 음식을 다 먹는데 필요한 시간을 계산하고, 이 시간이 k를 초과하는지 확인합니다.
    # 결국엔 이런식으로 정렬을 하더라도 사이클로 계산이 되므로 선형적으로 계산할 필요가 없다.
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]  # 현재 음식을 다 먹는데 필요한 시간을 가져옵니다.
        sum_value += (now - previous) * length  # 현재 단계에서 사용한 시간을 더합니다.
        length -= 1  # 다 먹은 음식을 제외하므로 남은 음식의 개수를 줄입니다.
        previous = now  # 이전 음식 시간을 현재 음식 시간으로 업데이트합니다.

    # 남은 음식들을 음식 번호 순으로 정렬합니다.
    result = sorted(q, key=lambda x: x[1])
    # k에서 지금까지 사용한 시간을 뺀 후, 남은 음식 수로 나눈 나머지를 계산하여
    # 다음에 먹어야 할 음식의 번호를 찾습니다.
    return result[(k - sum_value) % length][1]


solution([3, 1, 2, 1], 1)
