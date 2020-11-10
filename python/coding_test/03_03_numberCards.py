row, column = map(int, input().split())

result = 0
''' min을 이용해 행마다 최솟값을 미리 계산하는 방법
for i in range(row):
    data = list(map(int, input().split()))

    min_value = min(data)

    result = max(result, min_value)
'''

# 아래는 nested for를 이용한 방법

for i in range(row):
    data = list(map(int, input().split()))

    min_value = 10001 #문제 조건이 10000이하이니까

    for a in data:
        min_value = min(min_value, a)
    
    result = max(result, min_value)

print(result)