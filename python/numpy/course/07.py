# 오늘은 브로드캐스팅과 벡터연산에 대해 배움

# 브로드캐스팅은 Numpy에서 shape가 다른 배열 간에도 산술 연산이 가능하게하는 메커니즘
# 종종 작은 배열과 큰 배열이 있을 때, 큰 배열을 대상으로 작을 배열을 여러번 연산하려고
# 할때가 있다. 예를들어 행렬의 각 행에 상수 벡터를 더하는 것과 같은 일.

# 실습해보자

import numpy as np


# 행렬 x의 각 행에 벡터 v를 더한 뒤,
# 그 결과를 행렬 y에 저장하려고 한다는 걸 가정해보자
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
print(x)
'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
'''

v = np.array([1, 0, 1])
print(v)
'''
[1 0 1]
'''
y = np.empty_like(x) # x와 동일한 shape를 가지며 비어있는 행렬 생성
print(y)
'''
[[7602259 7471215 7536741]
 [6619219 7733362 6488169]
 [4391013 6357100 7536755]
 [7209033 7274598       0]]
'''

for i in range(4):
    y[i, :] = x[i, :] + v

print(y) # y가 아래와 같이 변함
'''
[[ 2  2  4]
 [ 5  5  7]
 [ 8  8 10]
 [11 11 13]]
'''

# 그런데 위 처럼 반복문을 통하는 것은 x가 커질수록 느려질 가능성이 높다
# 벡터v를 행렬x의 각 행에 더하는 것은 v를 여러개 복사해 수직으로 쌓은 행렬 vv를 만들고
# 이 vv를 x에 더하는 것과 동일하다.

# 이 과정을 아래와 같이 구현할 수 있다.

vv = np.tile(v, (4, 1)) # v의 복사본 4개를 위로 차곡차곡 쌓는 느낌으로 vv 만듬
print(vv)
'''
[[1 0 1]
 [1 0 1]
 [1 0 1]
 [1 0 1]]
'''
print(vv.shape)
'''
(4, 3)
'''

y = x + vv
print(y)
'''
[[ 2  2  4]
 [ 5  5  7]
 [ 8  8 10]
 [11 11 13]]
'''
# 위와같이 tile을 활용하는 것도 좋지만 더 쉽게 할 수 있다
# 아래와 같이 브로드캐스팅을 
# 동일한 연산을 할 수 있다.
# 아래에서 추가 학습을 해보자

# 벡터v를 행렬 x의 각 행에 더한 뒤.
# 그 결과를 행렬 y에 저장하고자 한다
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
v = np.array([1, 0, 1])

y = x + v
print(y)
'''
[[ 2  2  4]
 [ 5  5  7]
 [ 8  8 10]
 [11 11 13]]
'''

# x의 sha가 (4, 3), v가 (3,) 이라도 브로드캐스팅으로 인해 y=x+v 연산이 문제없이 수행 됨
# 이때 v는 v의 복사본이 차곡차곡 쌓인 shape (4,3)으로 간주되어
# x와 동한일 shape가 되어 이들간의 요소별 덧셈연산이 y에 저장 됨

# 두 배열의 브로드캐스팅은 아래의 규칙을  따름
# 1. 두 배열이 동일한 dimension을 가지고 있지 않다면, 낮은 dimension의 1차원 배열이 높은
#    dimension배열의 shape로 간주합니다
# 2. 특정 차원에서 두 배열이 동일한 크기를 갖거나, 두 배열 중 하나의 크기가 1이라면
#    그 두 배열은 특정 차원에서 compatible하다고 여겨진다
# 3. 두 행렬이 모든 차원에서 compatible하다면 브로드캐스팅이 가능하다
# 4. 브로드캐스팅이 이뤄지면, 각 배열 shape의 요소별 최소공배수로 이루어진 shape가
#    두 배열의 shape로 간주함.
# 5. 차원에 상관없이 크기가 1인 배열과 1보다 큰 배열이 있을 때,
#    크기가 1인 배열은 자신의 차원 수 만큼 복사되어 쌓인것처럼 간주합니다.



# 브로드캐스팅을 지원하는 함수를 universal functions라고 합니다

# 브로드캐스팅을 응용한 실습을 해보자

v = np.array([1,2,3]) # shape: (3,)
w = np.array([4, 5])  # shape: (2,)
x = np.array([[1,2,3],
              [4,5,6]])
print(x)
'''
[[1 2 3]
 [4 5 6]]
'''
# 벡터를 행렬의 각 행에 더하기
# x는 shape가 (2, 3)이고 v는 shape가 (3,)이므로 이 둘을 브로드캐스팅하면
# shape가 (2, 3)인 아래와 같은 행렬이 나온다
print(x+v)
'''
[[2 4 6]
 [5 7 9]]
'''


# 벡터를 행렬의 각 행에 더하기 ( Transpose를 활용한 트릭으로 볼수도 있다 )
# x는 shape가 (2, 3)이고 w는 shape가 (2,) 입니다.
# x의 전치행렬은 shape가 (3,2)이며 이는 w와 브로드캐스팅이 가능하고
# 결과로 shape가 (3,2)인 행렬이 생긴다
# 이 행렬을 전치하면 shape가 (2,3)인 행렬이 나오며
# 이는 행렬 x의 각 열에 벡터 w를 더한 결과와 동일합니다
print( x.T )
'''
[[1 4]
 [2 5]
 [3 6]]
'''
print( (x.T + w) )
'''
[[ 5  9]
 [ 6 10]
 [ 7 11]]
'''
print( (x.T + w).T )
'''
[[ 5  6  7]
 [ 9 10 11]]
'''


# 다른 방법은 w를 shape가 (2,1)인 열벡터로 변환하는 것
# 그런 다음 이를 바로 x에 브로드캐스팅해 더하면
# 동일한 결과가 나옴
print( np.reshape(w, (2, 1)) )
'''
[[4]
 [5]]
'''
print( x + np.reshape(w, (2, 1)) )
'''
[[ 5  6  7]
 [ 9 10 11]]
'''