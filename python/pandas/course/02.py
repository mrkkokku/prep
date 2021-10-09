import pandas as pd

# 파일 불러오기 등의 실습

# print(pd.read_csv('example.csv'))

df1 = pd.read_csv('example.csv')

# 가져온 뒤 data의 shape를 확인해보자

print(df1.shape)

# (705571, 20)
# 20개의 어트리뷰트를 가진 행이 70만개가 있는 걸 알수있음


print(df1.info())

''' 데이터의 전체적 구조와 특성을 확인할 수 있다
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 705571 entries, 0 to 705570
Data columns (total 20 columns):
 #   Column    Non-Null Count   Dtype
---  ------    --------------   -----
 0   공급일자      705571 non-null  object
 1   요일        705571 non-null  object
 2   공급월       705571 non-null  int64
 3   공급주차      705571 non-null  int64
 4   회원번호      705571 non-null  int64
 5   조합원상태     705571 non-null  object
 6   물품대분류     705571 non-null  object
 7   물품중분류     705571 non-null  object
 8   물품소분류     705571 non-null  object
 9   물품명       705571 non-null  object
 10  구매수량      705571 non-null  float64
 11  주소-구      705571 non-null  object
 12  주소-동      705571 non-null  object
 13  성별        705566 non-null  object
 14  연령        705538 non-null  float64
 15  연령대       705538 non-null  object
 16  구매금액      705571 non-null  int64
 17  구매매장      705571 non-null  object
 18  반품_원거래일자  11234 non-null   float64
 19  구매시각      705571 non-null  object
dtypes: float64(3), int64(4), object(13)
memory usage: 107.7+ MB
None
'''

print(df1.describe())
# 5-number summary를 보여줌. 평균이나 최소 최대 등 
# 이상한 데이터나, 다른형태의 데이터가 들어가있는 등의 정합성이 떨어지는 애들의 존재 유무를 어느정도 알아챌 수 있음
'''
                 공급월           공급주차          회원번호           구매수량             연령          구매금액      반품_원거래일자
count  705571.000000  705571.000000  7.055710e+05  705571.000000  705538.000000  7.055710e+05  1.123400e+04
mean        3.510817      13.500022  7.390639e+08       1.138203      50.756234  1.092004e+04  2.018034e+07
std         1.719153       7.517818  4.251288e+08       0.754448      11.418854  1.670323e+04  5.229237e+02
min         1.000000       1.000000  1.876416e+07     -50.000000       1.000000 -6.662160e+05  2.017121e+07
25%         2.000000       7.000000  3.906917e+08       1.000000      42.000000  4.116000e+03  2.018021e+07
50%         4.000000      13.000000  7.456573e+08       1.000000      49.000000  7.275000e+03  2.018040e+07
75%         5.000000      20.000000  1.045186e+09       1.000000      58.000000  1.263500e+04  2.018052e+07
max         6.000000      26.000000  1.670621e+09      50.000000     108.000000  2.751014e+06  2.018063e+07
'''


print(df1.head(2))
print(df1.tail(2))
print(df1.isnull())
print(df1.isnull().sum())
# 자료 전체 중 일부분만 보는 방법
# head는 상위 n개
# tail은 하위 n개
# isnull은 특정 데이터가 null인지 체크해주는 것
# isnull에 다시 sum쓰면 isnull의 결과값을 다시 summary해서 보여줌
'''
[705571 rows x 20 columns]
공급일자             0
요일               0
공급월              0
공급주차             0
회원번호             0
조합원상태            0
물품대분류            0
물품중분류            0
물품소분류            0
물품명              0
구매수량             0
주소-구             0
주소-동             0
성별               5
연령              33
연령대             33
구매금액             0
구매매장             0
반품_원거래일자    694337
구매시각             0
dtype: int64
'''

print(df1.columns)
# 컬럼명만 간략히 확인할 수 있다
'''
Index(['공급일자', '요일', '공급월', '공급주차', '회원번호', '조합원상태', '물품대분류', '물품중분류', '물품소분류',
       '물품명', '구매수량', '주소-구', '주소-동', '성별', '연령', '연령대', '구매금액', '구매매장',
       '반품_원거래일자', '구매시각'],
      dtype='object')
'''


print(df1[['구매금액']])
print(df1[['구매금액']].sum())
print(df1[['구매금액', '성별']])
# 특정 컬럼이나 범위 등 원하는 범위만 뽑아내기

# 복습 : dataframe을 인덱싱할때 괄호를 하나만 하면 출력이 series기땜에 두개의 컬럼을 동시에 콜 할순 없다
# 그래서 위를보면 두개의 대괄호로 2개의 컬럼을 콜 한걸 알 수 있고 그 결과는 dataframe으로 나온다