def solution(arr):
    
    if len(arr) <= 1:
        answer = [-1]
    else:
        arr = set(arr)
        arr.remove(min(arr))

        arr = list(arr)

        arr.sort(reverse=True)
        
        answer = arr
    
    return answer

print(solution([1]))
def solution(arr):
    answer = []
    if len(arr)==1:
        return [-1]
    else:
        arr.remove(min(arr))
    return arr