from random import *

# 리스트, 인덱스 2개를 넣으면
# 해당 리스트 내에서 리스트간에 스왑됨
def swap(t_list, n1, n2):
    temp = t_list[n1]
    t_list[n1] = t_list[n2]
    t_list[n2] = temp

# 함수 호출하면 정수입력 받게되고
# 그 수만큼 리스트로 출력하게 됨
def randint_generator():
    how_many = input("몇개 할래요? ")

    my_list = []
    for i in range(0, int(how_many)):
        my_list.append(randint(-10,10))
    
    return my_list

my_list = randint_generator()

print(my_list)
