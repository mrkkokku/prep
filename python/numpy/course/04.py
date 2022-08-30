import numpy as np

# 축, axis라는 개념이 등장한다
# 이게 좀 헷갈릴 수 있는데
# 아래처럼 있을 때에 
# 세로로 아래로 향하는게 axis = 0
# 가로로 오른쪽으로 향하는게 axis = 1
# 열을따라 움직이는게 0 축
# 행을따라 움직이는게 1 축
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

A = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(A)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
 '''

# numpy.amin
# 배열의 최소값을 축을따라 반환해준다
print( np.amin(A, 0) ) # 여기서 0은 axis=0 인데 생략해서 이렇게 나옴.
'''
[1 2 3]
'''  # 결국 이건, 1,4,7 중 작은 1. 2,5,8중 작은 2. 이런식으로 나온 것


print( np.amin(A, 1) )
'''
[1 4 7]
'''

print( np.amax(A, 0) )
'''
[7 8 9]
'''

print( np.amax(A, 1) )
'''
[3 6 9]
'''


# A
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
 '''
# numpy.ptp ~ peak to peak를 의미, 최대-최소 값을 보여주는 것임
print( np.ptp(A, 0) )
'''
[6 6 6]
'''

print( np.ptp(A, 1) )
'''
[2 2 2]
'''


# numpy.median 중간값을 출력
print( np.median(A, 0) )
'''
[4. 5. 6.]
'''

print( np.median(A, 1) )
'''
[2. 5. 8.]
'''


# numpy.mean ~ 산술평균 구하는 것, 가중평균 구하려면 numpy.average 써야됨
print( np.mean(A, 0) )
'''
[4. 5. 6.]
'''
print( np.mean(A, 1) )
'''
[2. 5. 8.]
'''


# numpy.var ~ 분산을 구할 수 있다
print( np.var(A, 0) )
'''
[6. 6. 6.]
'''

print( np.var(A, 1) )
'''
[0.66666667 0.66666667 0.66666667]
'''


# numpy.std ~ 표준편차를 구할 수 있음
print( np.std(A, 0) )
'''
[2.44948974 2.44948974 2.44948974]
'''

print( np.std(A, 1) )
'''
[0.81649658 0.81649658 0.81649658]
'''