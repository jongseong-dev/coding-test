"""
N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다. 예를 들어
2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수이다.

comment:
주어진 동전으로 배열의 index에 해당하는 동전의 최소값을 value로 가지고, 그 최소값을 더한다면 결국 그 값도 최소값이 된다는 원리로 푸는 문제
"""

n, m = map(int, input().split())

wallet = []  # 동전이 저장한 지갑 - 이해를 위해 변수 이름 사용

for i in range(n):
    wallet.append(int(input()))

bank = [10001] * (m + 1)  # 주어진 금액을 만들기 위해 최소 동전 개수를 보관한 은행

bank[0] = 0
for i in range(n):
    for j in range(wallet[i], m + 1):
        if bank[j - wallet[i]] != 10001:
            bank[j] = min(bank[j], bank[j - wallet[i]] + 1)

if bank[m] == 10001:
    print(-1)
else:
    print(bank[m])
