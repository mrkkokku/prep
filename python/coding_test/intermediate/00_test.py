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

def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
    else:
        answer = arr
        answer.remove(min(arr))
    return answer