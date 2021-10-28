import numpy as np

# 오늘은 shape 변경과 관련된 함수들을 배워본다

# arange(6)은 0,1,2,3,4,5 쭉 만드는거
a = np.arange(6)

print( a )
'''
[0 1 2 3 4 5]
'''

# 원소의 갯수와 reshape 대상의 수가 같으니 잘 작동함
a = np.arange(6).reshape((3, 2))

print( a )
'''
[[0 1]
 [2 3]
 [4 5]]
'''

# 이렇게 해도 같음
print( np.reshape(a, (3,2)) )
'''
[[0 1]
 [2 3]
 [4 5]]
'''


# numpy.ravel  : 직선으로 만들어 주는 것 (연속된 flattened array 반환)
# 사실 이건 reshape에 포함되는 내용이지만, 코드를 짧게칠 수 있는 장점이 있긴 함
print( np.ravel(a) )
'''
[0 1 2 3 4 5]
'''

# 위 처럼 np을 함수를 쓸 수도 있고
# 아래처럼 객체의 메소드로서도 사용 가능
print( a.ravel() )
'''
[0 1 2 3 4 5]
'''


# a.flatten()은 numpy의 함수로는 쓸 수 없고, 객체의 메소드로만 사용가능
print( a.flatten() )
'''
[0 1 2 3 4 5]
'''


# ravel과 flatten의 차이점은
# flatten의 객체의 메소드로만 사용 가능
# ravel은 뷰를 반환
# flatten은 복사본을 반환



# 연결과 관련된 함수

# numpy.concatenate
a = np.array([[1, 2], [3, 4]])
print( a )
'''
[[1 2]
 [3 4]]
'''

b = np.array([[5, 6]]) # 이거 지금 1차원이 아님, 1행 2열 구조에 주의
print( b )
'''
[[5 6]]
'''

print( np.concatenate((a, b), axis=0) )
'''
[[1 2]
 [3 4]
 [5 6]]
'''

# axis의 특성에 따라 오른쪽의 코드는 안돌아 감 print( np.concatenate((a, b), axis=1) )
# 저거 이해해 보자, 아래로 b를 T하면 돌아감
print( np.concatenate((a, b.T), axis=1) )
'''
[[1 2 5]
 [3 4 6]]
'''




# 다차원 배열 연산
# 기본적인 수학함수는 배열의 각 요소별로 동작하며 연산자를 통해 동작하거나 numpy 함수모듈을 통해 동작
# 다차원간 배열 연산시, shape가 맞아야 연산이 이루어짐
#   요소별로 합, 차, 곱, 나눗셈의 경우 shape가 일치해야 합니다
#   dot의 경우 앞 배열의 열과 뒤 배열의 행의 크기가 일치해야 합니다
# 아래의 것들이 별 것 아닌 것 같지만, 이 기능들이 없으면 반복문을 통해 엄청난 반복 연산을 해야하는걸
# numpy 기능으로 간단히 해결 하는 것

x = np.array([[1., 2.], [3., 4.]])
print( x )
'''
[[1. 2.]
 [3. 4.]]
'''

y = np.array([[5., 6.], [7., 8.]])
print( y )
'''
[[5. 6.]
 [7. 8.]]
'''

# 요소별 합, 같은 위치별로 합해 지는 것
print( x + y )
print( np.add(x,y) )
'''
[[ 6.  8.]
 [10. 12.]]
'''

# 요소별 차, 같은 위치별로 빼기 하는 것
print( x - y )
print( np.subtract(x,y) )
'''
[[-4. -4.]
 [-4. -4.]]
'''

# 요소별 곱, 같은 위치별로 곱해 지는 것
print( x * y )
print( np.multiply(x,y) )
'''
[[ 5. 12.]
 [21. 32.]]
'''

# 요소별 나누기, 같은 위치별로 나눠 지는 것
print( x / y )
print( np.divide(x,y) )
'''
[[0.2        0.33333333]
 [0.42857143 0.5       ]]
'''

# 요소별 제곱근, 같은 위치별로 나눠 지는 것
print ( np.sqrt(x) )
'''
[[1.         1.41421356]
 [1.73205081 2.        ]]
'''

print ( np.sqrt(y) )
'''
[[2.23606798 2.44948974]
 [2.64575131 2.82842712]]
'''


# numpy에선 벡터의 내적, 벡터와 행렬의 곱, 행렬곱을 위해 *대신 dot함수를 사용
# dot은 numpy모듈 함수로서도 배열 객체의 메소드로서도 이용 가능한 함수

x = np.array([[1, 2], [3, 4]])
print( x )
'''
[[1 2]
 [3 4]]
'''

y = np.array([[5, 6], [7, 8]])
print( y )
'''
[[5 6]
 [7 8]]
'''

v = np.array([9, 10])
print( v )
'''
[ 9 10]
'''

w = np.array([11, 12])
print( w )
'''
[11 12]
'''


# 대상이 둘다 벡터면, 내적
# 대상이 각 다르면 행렬과 벡터의 곱
# 대상이 둘다 행렬이면, 행렬곱


# 백터의 내적: 둘다 결과는 같음
print( v.dot(w) )
print( np.dot(v, w) )
'''
219
'''

# 행렬과 벡터의 곱 : 둘다 결과 dimension이 1인 배열
print( x.dot(v) )
print( np.dot(x, v) )
'''
[29 67]
'''

# 행렬곱: 둘 다 결과는 dimension 2인 배열
print( x.dot(y) )
print( np.dot(x, y) )
'''
[[19 22]
 [43 50]]
'''