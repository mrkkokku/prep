array = [ 7, 5, 9, 0, 3, 1, 6, 2, 4, 8 ]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            # 반복문 돌릴필요없다면 바로 종료시키기 위해
            # 어차피 왼쪽 part는 정렬된 part로 보니까
            # 걱정할 필요 없음
            break

print(array)