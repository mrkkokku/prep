import numpy as np

# 산술평균
print( np.mean(range(1,11)) )
'''
5.5
'''

# 가중평균
print( np.average(range(1,11)) )
'''
5.5
'''

# 파이썬 리스트를 만든 후에 그걸 넘파이 어레이로 만들기 땜에
# 최초 생성때의 시간은 넘파이 어레이가 더 오래 걸림
# (넘파이 어레이 생성 때 입력값이 리스트이기 때문)


# ndarray 다차원 배열

# 배열안의 모든 데이터는 그 타입들이 모두 같아야 한다
# 같은 크기의 메모리를 차지하도록 만들어졌기때문, 속도를 위한 trade-off

# np.array()를 사용해 직접 원소를 입력해 다차원 배열을 생성할 수 있다
boolArray = np.array([True, False, True, True, False])
print(boolArray)
print(boolArray.dtype)
'''
[ True False  True  True False]
bool
'''

# 정수형으로 해보자
intArray = np.array([[1, 2], [3, 4]])
print(intArray)
print(intArray.dtype)
'''
[[1 2]
 [3 4]]
int32
'''

# data type을 명시해서 생성해보자
unitArray = np.array([[1, 2], [3, 4]], dtype='uint64')
print(unitArray)
print(unitArray.dtype)
'''
[[1 2]
 [3 4]]
uint64
'''

# 지금까지 만든것이 이미 다차원 배열이다.
# np.array()로 만든 결과값은 그렇게 만들어 짐
# 실습을 더 해보자

# 실수형
floatArray = np.array([[1.1, 2.2], [3.3, 4.4]], dtype='float16')
print(floatArray)
print(floatArray.dtype)
'''
[[1.1 2.2]
 [3.3 4.4]]
float16
'''


# 넘파이의 data type은 상당히 여러 종류가 있고,
# 제공되는 타입 중에서만 사용이 가능한 것이다

# 코딩스탠다드에 의해 실수형으로 만들땐 아래가 더 좋은 코드
floatArray2 = np.array([[1., 2.], [3., 4.]])
print(floatArray2)
print(floatArray2.dtype)
'''
[[1. 2.]
 [3. 4.]]
float64
'''


# 이외에도 실수를 넣고 dtype만 int로 하거나 할 순 있지만
# 형변환 도중 데이터 손실이 발생 함


# 3차원은 이렇게 만드는데
# img processing 아니면 쓸일이 잘 없을 듯
a = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a)
'''
[[[1 2 3]
  [4 5 6]]
'''



# 파일에서 데이터를 입력받아 다차원배열 생성하기
''' 
np.genfromtxt()를 활용해 이 기능을 수행할 수 있긴하지만
사용할 일이 많지않다.
왜냐하면 ndarray가 동일한 데이터타입만 가질 수 있고
대부분은 데이터시트를 다양한 데이터타입이 혼재 해 있음

그래서 파일에서 data를 읽을땐 Pandas의 read_csv('')나
read_excel('')를 많이 쓰게 된다
'''

