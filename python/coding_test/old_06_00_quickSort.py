# 이 예제는 데이터의 첫 수를 피벗으로 잡는 방법을 
# 사용한 것임

array = [ 7, 5, 9, 0, 3, 1, 6, 2, 4, 8 ]

def quick_sort(array, start, end):
    if start >= end:
        return # 원소 1개일때 종료시키려고
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 각 포인터가 엇갈렸다면 작은데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)

print(array)