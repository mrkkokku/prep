# 파이썬의 장점을 살려 짧게 작성한 코드

array = [ 7, 5, 9, 0, 3, 1, 6, 2, 4, 8 ]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗은 첫 원소
    tail = array[1:] # 피벗 제외한 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))