# page 97

# 리스트에서 임의의 원소값을 업데이트하기

# call by val, call by ref 도 아닌
# 파이썬 특유의 call by object reference를 체험하는 예제

def change(lst, idx, val):
    lst[idx] = val

x = [11, 22, 33, 44, 55]
print("x = ", x)

index = int(input("업데이트할 인덱스를 선택하세요 : "))
value = int(input("새로운 값을 입력핫세요 : "))

change(x, index, value)
print(f"x = {x}")

# 인수가 mutable이면 call 상태, 그러니까
# 함수안에서도 값이 변경 될 수 있음을 알 수 있다
