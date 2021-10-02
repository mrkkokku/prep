import numpy as np

A = np.array([[1,2], [3,5]])


type(A)

print(A.ndim) # 배열의 차원

print(A.shape) # 배열의 크기

print(A.dtype) # 원소 자료형

print(A[0])
print(A[1])

print(A[A>1])