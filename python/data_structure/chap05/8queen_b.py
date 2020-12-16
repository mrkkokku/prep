# 각 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기

pos = [0] * 8

def put() -> None:
    '''각 열에 배치한 퀸의 위치를 출력'''
    for i in range(8):
        print(f"{pos[i]:2}", end='') # 가운데 :2의 의미는 해당 텍스트가 2칸을 차지한단 뜻
    print()

def set(i : int) -> None:
    '''i열에 퀸을 배치'''
    for j in range(8):
        pos[i] = j
        if i == 7 :
            put()
        else:
            set(i+1)

#set(0) # 0 열에 퀸을 배치