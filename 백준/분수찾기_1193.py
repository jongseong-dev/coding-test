# 1 -> (0,0) -> 1/1
# 2 -> (1,0) -> 1/2
# 3 -> (0,1) -> 2/1
# 4 -> (2,0) -> 1/3
# 5 -> (1,1) -> 2/2
# 6 -> (0,2) -> 3/1
# 7 -> (3,0) -> 1/4
# 8 -> (2,1) -> 2/3
# 9 -> (1,2) -> 3/3
# ..
# 13 -> (2,2) -> 3/3

# n의 제곱?
# [1/1, 1/2, 2/1, 1/3, 2/2, 3/1 ...]

# x축은 분모 (x + 1)
# y축은 분자 (y + 1)
# 주어진 N을 좌표값으로 어떻게 치환?
# 1, 2, 4, 7,  11 -> y축은 0 x 축은  0, 1, 2, 3, 4
# 1, 3, 6, 10, 15 -> x축은 0  y 축은  0, 1, 2, 3, 4
# 1, 5, 9, 13,  -> x == y 축
# 이전 N번째 인덱스  + N - 1 = x


N = 3
#
# idx = 1
# while True:
#     corner_x = sum(range(idx)) + 1  # 좌표계에서 끝 지점 x,0
#     corner_y = sum(range(idx + 1))   # 좌표곙에서 끝지점 0,y
#     while corner_x <= N <= corner_y:


# 내가 지금 못 푼이유
# N이 주어졌을 때 x, y 좌표를 구하는 방법을 모르겠다.

# N = 이전 N의 값 + index - 1
# 그러면 어떻게 이전 N의 값을 알 수 있을까?
print([[idx, sum(range(item + 1))] for idx, item in enumerate(range(1, 10))])  # -> y축
print([sum(range(idx)) + 1 for idx in range(1, 10)])  # -> x축
print([sum(range(idx)) + 1 for idx in range(1, 10)])  # -> x축 1, y축 1일때


# def solution(n: int):
