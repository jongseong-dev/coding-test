# 피보나치 수열 다이나믹 프로그래밍으로 구현하기

d = [0] * 100


def fibo(x):
    # 종료 조건 (1 혹은 2일때 1을 반환)
    if x == 1 or x == 2:
        return 1

    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]

    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


def fibo_bottom_up():
    d = [0] * 100
    d[1] = 1
    d[2] = 1

    n = 99

    # 피보나치 함수 반복문으로 구현(보텀업 다이나믹 프로그래밍)
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
