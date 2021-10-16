# 현실에서 만날만 한 Data05.xlsx 데이터를 가지고 실습해보자
# 데이터 구조가 진짜 개판인 엑셀

import pandas as pd

df1 = pd.read_excel('Data05.xlsx', engine='openpyxl', skiprows=1) # 파이썬쪽 안정성 문제로 엑셀은 이렇게 열어줘야됨

print(df1.shape)
'''
(93, 27)
'''

print(df1.columns)
'''
Index([                   '구분',                       0,
                       '카테고리명',                  '자재그룹',
                       '자재그룹명',                  '제품코드',
                         '제품명',            'Unnamed: 7',
                          '판매',     2019-12-01 00:00:00,
           2020-10-01 00:00:00,     2020-11-01 00:00:00,
           2020-12-01 00:00:00, '2019-12-01 00:00:00.1',
       '2020-10-01 00:00:00.1', '2020-11-01 00:00:00.1',
       '2020-12-01 00:00:00.1', '2019-12-01 00:00:00.2',
       '2020-10-01 00:00:00.2', '2020-11-01 00:00:00.2',
       '2020-12-01 00:00:00.2', '2019-12-01 00:00:00.3',
       '2020-10-01 00:00:00.3', '2020-11-01 00:00:00.3',
       '2020-12-01 00:00:00.3',                  '안전재고',
                         ' 분류'],
      dtype='object')
'''

# 필요한 열의 이름은 살려서 써보자

# print( df1.iloc[:, 0] ) # 특정열에있는 데이터를 쭉 불러오는 것임 (데이터를 추출할때 쓰는 느낌)

# iloc[ __ : __ ] 이것의 의미는
#      index column 의 느낌이다

# 결국 아래처럼 해보자

print( df1.iloc[ : , 8:-2] )
'''
          판매  2019-12-01 00:00:00  ...  2020-11-01 00:00:00.3  2020-12-01 00:00:00.3
0        0.0                  0.0  ...                    0.0                    0.0    
1        0.0                  0.0  ...                    0.0                    0.0    
2    10354.1               9474.3  ...                 6972.0                 3368.2    
3     3543.3               7702.6  ...                 4009.9                 2680.1    
4   234603.9              56309.6  ...                74942.2                84967.2    
..       ...                  ...  ...                    ...                    ...    
88       0.0                  0.0  ...                    0.0                    0.0    
89       0.0                  0.0  ...                    0.0                    0.0    
90       0.0                  0.0  ...                    0.0                    0.0    
91       0.0                  0.0  ...                    0.0                    0.0    
92  181331.6              40207.8  ...               110209.3                44002.2    

[93 rows x 17 columns]
'''
# 얘들을 우선 transpose해보자

print( df1.iloc[ : , 8:-2].T )
'''
                         0      1        2       3   ...   89   90     91        92
판매                      0.0    0.0  10354.1  3543.3  ...  0.0  0.0    0.0  181331.6   
2019-12-01 00:00:00     0.0    0.0   9474.3  7702.6  ...  0.0  0.0    0.0   40207.8     
2020-10-01 00:00:00     0.0    0.0   9741.7  6117.1  ...  0.0  0.0    0.0  107175.6     
2020-11-01 00:00:00     0.0    0.0   6965.7  4009.9  ...  0.0  0.0    0.0  110209.3     
2020-12-01 00:00:00     0.0    0.0   3368.2  2669.8  ...  0.0  0.0    0.0   43576.6     
2019-12-01 00:00:00.1   0.0    0.0      0.0     0.0  ...  0.0  0.0  243.8       0.0     
2020-10-01 00:00:00.1   0.0    0.0      0.0     0.0  ...  0.0  0.0    0.0       0.0     
2020-11-01 00:00:00.1   0.0    0.0      0.0     0.0  ...  0.0  0.0    0.0       0.0     
2020-12-01 00:00:00.1   0.0    0.0      0.0     0.0  ...  0.0  0.0    0.0       0.0     
2019-12-01 00:00:00.2  98.8  393.7      6.4     7.7  ...  3.0  6.5  609.5    1249.7     
2020-10-01 00:00:00.2   0.0    0.0      0.0    10.2  ...  0.0  0.0    0.0       0.0     
2020-11-01 00:00:00.2   0.0    0.0      6.4     0.0  ...  0.0  0.0    0.0       0.0     
2020-12-01 00:00:00.2   0.0    0.0      0.0    10.2  ...  0.0  0.0    0.0     425.6     
2019-12-01 00:00:00.3  98.8  393.7   9480.7  7710.3  ...  3.0  6.5  853.4   41457.5     
2020-10-01 00:00:00.3   0.0    0.0   9741.7  6127.3  ...  0.0  0.0    0.0  107175.6     
2020-11-01 00:00:00.3   0.0    0.0   6972.0  4009.9  ...  0.0  0.0    0.0  110209.3     
2020-12-01 00:00:00.3   0.0    0.0   3368.2  2680.1  ...  0.0  0.0    0.0   44002.2     

[17 rows x 93 columns]
'''

# 흠 이렇게 해도 뭔가 이상하다
# 다른 함수를 써보자

df2 = df1.iloc[ : , 8:-2]
df2.stack()      # 데이터를 컬럼 형태로 쌓는건데, 이건 생각 좀 해보자

# 어찌됐든 시리즈 형태로 스택이 됨 
print(df2.stack())
'''
0   판매                            0.0
    2019-12-01 00:00:00           0.0
    2020-10-01 00:00:00           0.0
    2020-11-01 00:00:00           0.0
    2020-12-01 00:00:00           0.0
                               ...
92  2020-12-01 00:00:00.2       425.6
    2019-12-01 00:00:00.3     41457.5
    2020-10-01 00:00:00.3    107175.6
    2020-11-01 00:00:00.3    110209.3
    2020-12-01 00:00:00.3     44002.2
Length: 1581, dtype: float64
'''

# 이걸 다시 DF로 만들자
print( pd.DataFrame(df2.stack()) )
'''
                                 0
0  판매                          0.0
   2019-12-01 00:00:00         0.0
   2020-10-01 00:00:00         0.0
   2020-11-01 00:00:00         0.0
   2020-12-01 00:00:00         0.0
...                            ...
92 2020-12-01 00:00:00.2     425.6
   2019-12-01 00:00:00.3   41457.5
   2020-10-01 00:00:00.3  107175.6
   2020-11-01 00:00:00.3  110209.3
   2020-12-01 00:00:00.3   44002.2

[1581 rows x 1 columns]
'''

# 이렇게 했더니, 데이터들이 인덱스가 되어버리는 문제가 생겼음

print( pd.DataFrame(df2.stack()).reset_index() )
'''
      level_0                level_1         0
0           0                     판매       0.0
1           0    2019-12-01 00:00:00       0.0
2           0    2020-10-01 00:00:00       0.0
3           0    2020-11-01 00:00:00       0.0
4           0    2020-12-01 00:00:00       0.0
...       ...                    ...       ...
1576       92  2020-12-01 00:00:00.2     425.6
1577       92  2019-12-01 00:00:00.3   41457.5
1578       92  2020-10-01 00:00:00.3  107175.6
1579       92  2020-11-01 00:00:00.3  110209.3
1580       92  2020-12-01 00:00:00.3   44002.2

[1581 rows x 3 columns]
'''

print( pd.DataFrame(df2.stack()).reset_index().iloc[1:] )
'''  이렇게하면 판매라는게 날아 감
      level_0                level_1         0
1           0    2019-12-01 00:00:00       0.0
2           0    2020-10-01 00:00:00       0.0
3           0    2020-11-01 00:00:00       0.0
4           0    2020-12-01 00:00:00       0.0
5           0  2019-12-01 00:00:00.1       0.0
...       ...                    ...       ...
1576       92  2020-12-01 00:00:00.2     425.6
1577       92  2019-12-01 00:00:00.3   41457.5
1578       92  2020-10-01 00:00:00.3  107175.6
1579       92  2020-11-01 00:00:00.3  110209.3
1580       92  2020-12-01 00:00:00.3   44002.2

[1580 rows x 3 columns]
'''

# 데이터 자체가 어떤 키값이나, 어떤 형태로 구성되어있는지 먼저 아는게 중요하고
# 그래야 어떻게 변경시켜가야할지 판단 할 수 있을 것임



# 이 뒤의 강의는 내가 하려는 것에 크게 필요한 부분이 아닌 것 같아서 생략한다
# 혹시나 유튜브 주소는 https://www.youtube.com/watch?v=3-iwY0_u0VA&list=PLhdHuKlSngGxvB0bMYigcn8zwD4zmewtt&index=7
# 18분~19분 정도에서 멈춤
