# 앞의 LRUD와 다르게 
# 미리 이동가능 방법을 steps에 박아 놓고 하는 풀이법
# input 형태는 a2, a3 이런식

input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
# 이 부분은 a - a + 1 이니까 a들어오면 1을 뜻함

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
result = 0
print(steps[0])
print(steps[1])
for step in steps:
    #이동 대상 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]

    # 대상위치로 이동 가능할때 카운트++
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

