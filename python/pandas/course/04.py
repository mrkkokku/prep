# 오늘은 데이터를 처음 가져왔을 때 해야하는 전처리 방법들에 대해 알아 봄

# 크게는 정형데이터 or 비정형 데이터를 구분


# 정형 데이터는 column, row, value로 이뤄져 있고
# 반정형 데이터는 HTML, XML, JSON 같은 형태
# 비정형은 SNS, Image, Video 같은 것들

import pandas as pd

df1 = pd.read_csv('Data01.csv')

# 처음 데이터를 불러오면 shape를 확인해봄
# column과 row를 바로 확인할 수 있다
# 확인용으로 head함수, info함수, describe함수 등을 활용하면 됨
print(df1.shape)
print(df1.head())
print(df1.info())
print(df1.describe())

# 특별히 범주형데이터의 경우에는
# 시리즈의 유니크값을 확인 가능 (컬럼의 도메인 확인 가능)
print(df1['카테고리'].unique())
'''
['세탁세제' '헤어케어' '주방세제' 'ST' 'F&B' '덴탈케어' '기타' '매입브랜드']
'''

print(df1['카테고리'].value_counts()) # 범주형 데이터 항목 갯수
'''
세탁세제     4265
덴탈케어     3115
헤어케어     2750
ST       1732
주방세제     1709
F&B      1038
매입브랜드     238
기타        153
Name: 카테고리, dtype: int64
'''
print(df1['카테고리'].describe()) # 범주형 데이터의 요약 정리
'''
count     15000
unique        8
top        세탁세제
freq       4265
Name: 카테고리, dtype: object
'''


print(df1[['발주가능상태', '카테고리', '상품명']].describe()) # 열 여러개 쓰기가 어려우니까
'''
       발주가능상태   카테고리     상품명
count   15000  15000   15000
unique      3      8     528
top      발주가능   세탁세제  V2_114
freq    14700   4265      47
'''

print(df1.describe().columns.tolist()) # 이렇게하면 열들이 리스트로 반환됨
'''
['바코드', '입고수량', '출고수량']
'''

print(df1.columns.tolist()) # 전체 열을 확인 가능
'''
['날짜', '상품명', '바코드', '발주가능상태', '입고수량', '카테고리', '출고수량'] 
'''

total_list = df1.columns.tolist()

numeric_list = df1.describe().columns.tolist()

object_list = list( set(total_list) - set(numeric_list) )

# 범주형 데이터만 이렇게 뽑아낼수 있게 됨
print(object_list)
'''
['상품명', '발주가능상태', '날짜', '카테고리']
'''


# 입고수량 순서대로 정렬한다면
print(df1.sort_values(by='입고수량',ascending=True))
'''
               날짜     상품명           바코드 발주가능상태  입고수량  카테고리  출고수
량
7499   2019-06-23  V2_284  1.880105e+13   발주가능     0   F&B     0
8528   2019-06-28  V2_289  1.880105e+13   발주가능     0  덴탈케어     0
8529   2019-06-28  V2_290  1.880105e+13   발주가능     0  덴탈케어     0
8530   2019-06-28  V2_291  1.880105e+13   발주가능     0  주방세제     0
8531   2019-06-28  V2_292  1.880105e+13   발주가능     0  주방세제     0
...           ...     ...           ...    ...   ...   ...   ...
14062  2019-07-31  V2_129  8.801050e+12   발주가능  7287  덴탈케어    49
14051  2019-07-31   V2_86  1.880100e+13   발주가능  9480  세탁세제   141
13054  2019-07-23   V2_86  1.880105e+13   발주가능  9488  세탁세제   208
9719   2019-07-04   V2_86  1.880105e+13   발주가능  9539  세탁세제   205
3647   2019-06-03   V2_86  1.880105e+13   발주가능  9777  세탁세제   308

[15000 rows x 7 columns]
'''

# 입고수량, 출고수량 같이 정렬 한다면
print(df1.sort_values(by=['입고수량', '출고수량'], ascending=[True, True]))
'''
              날짜     상품명           바코드 발주가능상태  입고수량  카테고리  출고수
량
8      2019-05-16   V2_20  8.801046e+12   발주가능     0  주방세제     0
9      2019-05-16   V2_22  8.801047e+12   발주가능     0  세탁세제     0
13     2019-05-16   V2_28  8.801047e+12   발주가능     0  주방세제     0
14     2019-05-16   V2_29  8.801047e+12   발주가능     0  주방세제     0
16     2019-05-16   V2_38  8.801047e+12   발주가능     0  헤어케어     0
...           ...     ...           ...    ...   ...   ...   ...
14062  2019-07-31  V2_129  8.801050e+12   발주가능  7287  덴탈케어    49
14051  2019-07-31   V2_86  1.880100e+13   발주가능  9480  세탁세제   141
13054  2019-07-23   V2_86  1.880105e+13   발주가능  9488  세탁세제   208
9719   2019-07-04   V2_86  1.880105e+13   발주가능  9539  세탁세제   205
3647   2019-06-03   V2_86  1.880105e+13   발주가능  9777  세탁세제   308

[15000 rows x 7 columns]
'''
