# AI 엔지니어인 현식이는 데이터를 분석하는 작업을 진행하고 있습니다.
# 데이터는 ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]으로 구성되어 있으며 현식이는 이 데이터들 중 조건을 만족하는 데이터만 뽑아서 정렬하려 합니다.
# 이중 배열
# 주어진 데이터 중 "제조일이 20300501 이전인 물건들을 현재 수량이 적은 순서"로 정렬해야 한다면 조건에 맞게 가공된 데이터는 다음과 같습니다.
# 정렬한 데이터들이 담긴 이차원 정수 리스트 data와 어떤 정보를 기준으로
# 데이터를 뽑아낼지를 의미하는 문자열 ext,
# 뽑아낼 정보의 기준값을 나타내는 정수 val_ext, 정
# 보를 정렬할 기준이 되는 문자열 sort_by가 주어집니다.


# 1. ext 의 값을 enum 또는 dict 로 관리해서 date 일 경우 -> index 1, maximun 일 경우  index 2 등으로 변환시키는 kv 만들자
# 2. 1과 마찬가지로 sort_by 도 kv 로 index 로 변환하는 과정을 거치자


convert_index = {
    "code": 0,
    "date": 1,
    "maximum": 2,
    "remain": 3,
}


def solution(data, ext, val_ext, sort_by):
    ext = convert_index.get(ext)
    sort_by = convert_index.get(sort_by)

    answer = list(filter(lambda x: x[ext] < val_ext, data))
    answer = sorted(answer, key=lambda x: x[sort_by])
    return answer


data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"

assert solution(data, ext, val_ext, sort_by) == [
    [3, 20300401, 10, 8],
    [1, 20300104, 100, 80],
]

data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
assert solution(data, ext, val_ext, sort_by) == []
