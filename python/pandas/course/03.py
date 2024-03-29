import pandas as pd

# df1 객체에? 인스턴스에? csv 로드 후 shape와 head를 확인
df1 = pd.read_csv('example.csv')

print(df1.shape)
'''
(705571, 20)
'''
print(df1.head())
'''
         공급일자 요일  공급월  공급주차        회원번호 조합원상태 물품대분류  ... 성별    연령    연령대   
구매금액 구매매장 반품_원거래일자   구매시각
0  2018-01-02  화    1     1   272369856  정상회원    과실  ...  여  45.0    40대  22207  매장C      NaN  10:04
1  2018-01-02  화    1     1  1506656256  정상회원    채소  ...  여  36.0  30대이하   4977  매장C      NaN  10:05
2  2018-01-02  화    1     1  1506656256  정상회원   축산물  ...  여  36.0  30대이하   7083  매장C      NaN  
10:05
3  2018-01-02  화    1     1  1023108864  정상회원    반찬  ...  여  36.0  30대이하    766  매장C      NaN  10:08
4  2018-01-02  화    1     1  1476143616  정상회원    간식  ...  여  34.0  30대이하   4403  매장C      NaN  10:09

[5 rows x 20 columns]
'''


# 이제 이거를 추출하거나 정렬하거나 등을 해보자

# DataFrame은 3가지로 구성되어있다
# df1.columns
# df1.index
# df1.values
# 이런 변수를 가지고 있다

# describe는 요약해서 빠르게 보여준다
print(df1.describe())
'''
                 공급월           공급주차          회원번호           구매수량             연령          구
매금액      반품_원거래일자
count  705571.000000  705571.000000  7.055710e+05  705571.000000  705538.000000  7.055710e+05  1.123400e+04  
mean        3.510817      13.500022  7.390639e+08       1.138203      50.756234  1.092004e+04  2.018034e+07  
std         1.719153       7.517818  4.251288e+08       0.754448      11.418854  1.670323e+04  5.229237e+02  
min         1.000000       1.000000  1.876416e+07     -50.000000       1.000000 -6.662160e+05  2.017121e+07  
25%         2.000000       7.000000  3.906917e+08       1.000000      42.000000  4.116000e+03  2.018021e+07  
50%         4.000000      13.000000  7.456573e+08       1.000000      49.000000  7.275000e+03  2.018040e+07  
75%         5.000000      20.000000  1.045186e+09       1.000000      58.000000  1.263500e+04  2.018052e+07  
max         6.000000      26.000000  1.670621e+09      50.000000     108.000000  2.751014e+06  2.018063e+07  

'''
# info는 전체 요약정보를 보여준다
print(df1.info())
'''
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

# 하나의 컬럼에대해 대괄로 하나로 입력하면 그 출력이 series로 나옴
# 하나 이상의 컬럼에 대해 대괄호 이중으로 입력하면 그 출력이 dataframe으로 나옴



# 데이터 행 추출을 해보자 (인덱싱 하듯이 하면 됨)
print(df1.iloc[0]) # 1행에 대한 정보만 싹 나옴
'''
공급일자         2018-01-02
요일                    화
공급월                   1
공급주차                  1
회원번호          272369856
조합원상태              정상회원
물품대분류                과실
물품중분류                과일
물품소분류                사과
물품명         사과/유(1.5kg)
구매수량                  1
주소-구                수지구
주소-동               풍덕천동
성별                    여
연령                   45
연령대                 40대
구매금액              22207
구매매장                매장C
반품_원거래일자            NaN
구매시각              10:04
Name: 0, dtype: object
'''

print(df1.iloc[-1]) # 마지막 행에 대한 정보만 나옴
'''
공급일자             2018-06-30
요일                        토
공급월                       6
공급주차                     26
회원번호              301961920
조합원상태                  정상회원
물품대분류                    음료
물품중분류                    음료
물품소분류                    빙과
물품명         포도꽁꽁(120ml)/매장용
구매수량                      1
주소-구                    수지구
주소-동                   풍덕천동
성별                        여
연령                       49
연령대                     40대
구매금액                   1914
구매매장                    매장A
반품_원거래일자                NaN
구매시각                  16:36
Name: 705570, dtype: object
'''

print(df1.iloc[0:11]) # 상위 10개의 데이터가 나오겠지
'''
          공급일자 요일  공급월  공급주차        회원번호 조합원상태 물품대분류  ... 성별    연령    연령대  
 구매금액 구매매장 반품_원거래일자   구매시각
0   2018-01-02  화    1     1   272369856  정상회원    과실  ...  여  45.0    40대  22207  매장C      NaN  10:04
1   2018-01-02  화    1     1  1506656256  정상회원    채소  ...  여  36.0  30대이하   4977  매장C      NaN  
10:05
2   2018-01-02  화    1     1  1506656256  정상회원   축산물  ...  여  36.0  30대이하   7083  매장C      NaN 
 10:05
3   2018-01-02  화    1     1  1023108864  정상회원    반찬  ...  여  36.0  30대이하    766  매장C      NaN  
10:08
4   2018-01-02  화    1     1  1476143616  정상회원    간식  ...  여  34.0  30대이하   4403  매장C      NaN  
10:09
5   2018-01-02  화    1     1   716128320  정상회원   축산물  ...  여  51.0    50대   7083  매장C      NaN  10:10
6   2018-01-02  화    1     1   743192512  정상회원    채소  ...  여  51.0    50대  17038  매장C      NaN  10:12
7   2018-01-02  화    1     1   743192512  정상회원    채소  ...  여  51.0    50대  11104  매장C      NaN  10:12
8   2018-01-02  화    1     1   743192512  정상회원    채소  ...  여  51.0    50대   7083  매장C      NaN  10:12
9   2018-01-02  화    1     1   743192512  정상회원    채소  ...  여  51.0    50대   2584  매장C      NaN  10:12
10  2018-01-02  화    1     1  1177875136  정상회원    채소  ...  여  34.0  30대이하   7179  매장C      NaN  
10:19

[11 rows x 20 columns]
'''


# 이제 데이터 정렬에 대해 알아보자
# 특정 컬럼 기준으로 오름차순 또는 내림차순 하기

# 구매금액 기준으로 데이터 정렳보기
print( df1.sort_values(by='구매금액') )# 이렇게하면 오름차순으로 정렬됨
'''
              공급일자 요일  공급월  공급주차        회원번호 조합원상태  물품대분류  ... 성별     연령    연
령대     구매금액 구매매장    반품_원거래일자   구매시각
157876  2018-02-09  금    2     6  1529962048  정상회원     건강  ...  남   29.0  30대이하  -666216  매장C  20180206.0  16:59
181579  2018-02-14  수    2     7   747242304  정상회원     건강  ...  여   54.0    50대  -666216  매장C  20180206.0  14:06
144210  2018-02-06  화    2     6   747242304  정상회원     건강  ...  여   54.0    50대  -499662  매장C  20180206.0  16:42
142077  2018-02-06  화    2     6   307284928  정상회원     건강  ...  여   53.0    50대  -499662  매장C  20180206.0  18:52
145272  2018-02-06  화    2     6  1031186176  정상회원     건강  ...  여   51.0    50대  -499662  매장C  20180206.0  16:04
...            ... ..  ...   ...         ...   ...    ...  ... ..    ...    ...      ...  ...         ...    
...
585654  2018-06-01  금    6    22   153723200  정상회원     채소  ...  여   52.0    50대  1445383  매장A     
    NaN  18:13
155255  2018-02-09  금    2     6   236805184  정상회원     건강  ...  여   39.0  30대이하  1448255  매장B   
      NaN  12:17
127674  2018-02-02  금    2     5   938963392  정상회원     간식  ...  여   40.0    40대  1588964  매장B     
    NaN  16:22
208148  2018-02-23  금    2     8   742461248  정상회원  양념/가루  ...  남  106.0  70대이상  1688514  매장D 
        NaN  11:30
182163  2018-02-14  수    2     7   854303808  정상회원     채소  ...  여   52.0    50대  2751014  매장B     
    NaN  12:36
[705571 rows x 20 columns]
'''
print( df1.sort_values(by='구매금액', ascending=False) ) # 이렇게하면 내림차순으로 정렬
'''
              공급일자 요일  공급월  공급주차        회원번호 조합원상태  물품대분류  ... 성별     연령    연
령대     구매금액 구매매장    반품_원거래일자   구매시각
182163  2018-02-14  수    2     7   854303808  정상회원     채소  ...  여   52.0    50대  2751014  매장B     
    NaN  12:36
208148  2018-02-23  금    2     8   742461248  정상회원  양념/가루  ...  남  106.0  70대이상  1688514  매장D 
        NaN  11:30
127674  2018-02-02  금    2     5   938963392  정상회원     간식  ...  여   40.0    40대  1588964  매장B     
    NaN  16:22
155255  2018-02-09  금    2     6   236805184  정상회원     건강  ...  여   39.0  30대이하  1448255  매장B   
      NaN  12:17
585654  2018-06-01  금    6    22   153723200  정상회원     채소  ...  여   52.0    50대  1445383  매장A     
    NaN  18:13
...            ... ..  ...   ...         ...   ...    ...  ... ..    ...    ...      ...  ...         ...    
...
144210  2018-02-06  화    2     6   747242304  정상회원     건강  ...  여   54.0    50대  -499662  매장C  20180206.0  16:42
145272  2018-02-06  화    2     6  1031186176  정상회원     건강  ...  여   51.0    50대  -499662  매장C  20180206.0  16:04
142077  2018-02-06  화    2     6   307284928  정상회원     건강  ...  여   53.0    50대  -499662  매장C  20180206.0  18:52
181579  2018-02-14  수    2     7   747242304  정상회원     건강  ...  여   54.0    50대  -666216  매장C  20180206.0  14:06
157876  2018-02-09  금    2     6  1529962048  정상회원     건강  ...  남   29.0  30대이하  -666216  매장C  20180206.0  16:59

[705571 rows x 20 columns]
'''

# 구매수량으로 정렬 해보기
df1.sort_values(by='구매수량', ascending=False)

# 정렬하고싶은 기준을 두개 이상 넣을 땐
df1.sort_values(by=['구매수량', '연령'], ascending=False) # 이런식으로 기준값을 list로 주면 됨

# 정렬대상이 둘 이상이고, ordering도 따로 2개 이상 조건으로 하고싶다면
df1.sort_values(by=['구매수량', '연령'], ascending=[False, True])

# 위의 것에 추가로 특정 범위만 뽑고 싶으면
df1.sort_values(by=['구매수량', '연령'], ascending=[False, True]).iloc[:10]





# 이제 데이터 중 특정조건을 만족하는 것만 뽑는 것을 해보자

# 연령 중 40대만 뽑는것
print(df1['연령대'].value_counts()) # 이러면 도메인별로 카운트가 나옴
'''
40대      270573
50대      174458
30대이하    106392
60대       95019
70대이상     59096
Name: 연령대, dtype: int64
'''

# 순서대로 해보자
cond1 = (df1['연령대'] == '40대') # 이렇게하면 현재 df1의 정렬순과 똑같이 40대 여부가 series로 출력되며 그 값을 cond1이 가지고 있을 것

print( df1.loc[cond1] ) # cond1과 loc의 조합으로 특정열만 출력하게 됨
'''
              공급일자 요일  공급월  공급주차        회원번호 조합원상태  물품대분류  ... 성별    연령  연령
대   구매금액 구매매장 반품_원거래일자   구매시각
0       2018-01-02  화    1     1   272369856  정상회원     과실  ...  여  45.0  40대  22207  매장C      NaN 
 10:04
17      2018-01-02  화    1     1  1049686784  정상회원     간식  ...  여  40.0  40대   5743  매장C      NaN 
 10:31
18      2018-01-02  화    1     1   164510272  정상회원     채소  ...  여  42.0  40대   8711  매장C      NaN 
 10:32
19      2018-01-02  화    1     1  1185171072  정상회원  양념/가루  ...  여  47.0  40대   5169  매장C      NaN  10:37
20      2018-01-02  화    1     1  1206815744  정상회원     채소  ...  여  42.0  40대   5265  매장C      NaN 
 10:39
...            ... ..  ...   ...         ...   ...    ...  ... ..   ...  ...    ...  ...      ...    ...     
705556  2018-06-30  토    6    26   572193664  정상회원     반찬  ...  여  46.0  40대   2202  매장A      NaN 
 13:48
705560  2018-06-30  토    6    26  1333795840  정상회원     반찬  ...  여  41.0  40대   7275  매장A      NaN 
 15:28
705561  2018-06-30  토    6    26  1333795840  정상회원     채소  ...  여  41.0  40대   3982  매장A      NaN 
 15:28
705569  2018-06-30  토    6    26  1209779776  정상회원     간식  ...  여  41.0  40대   3542  매장A      NaN 
 18:04
705570  2018-06-30  토    6    26   301961920  정상회원     음료  ...  여  49.0  40대   1914  매장A      NaN 
 16:36

[270573 rows x 20 columns]
'''


print(df1.loc[cond1].shape) # 위의 조건에 맞는 출력값에 대한 shape확인
'''
(270573, 20)
'''
# loc는 로케이션이며, 비슷하게 사용가능한게 많지만 이게 대표적임


# 또 다른조건으로 해보자, 남자면서 40대인것 찾기

print(df1['성별'].value_counts())
'''
여    662024
남     43542
Name: 성별, dtype: int64
'''

cond1 = (df1['연령대'] == '40대')
cond2 = (df1['성별'] == '남')

print(df1.loc[cond1 & cond2]) # 이렇게 비트연산으로 series 두개를 and해버리면 동시만족하는 조건의 것만 잡을 수 있는 것임
'''
              공급일자 요일  공급월  공급주차        회원번호 조합원상태 물품대분류  ... 성별    연령  연령대
   구매금액 구매매장 반품_원거래일자   구매시각
34      2018-01-02  화    1     1   570500992  정상회원    간식  ...  남  47.0  40대   3829  매장C      NaN  
11:19
38      2018-01-02  화    1     1  1314239168  정상회원    간식  ...  남  48.0  40대  20676  매장C      NaN  
11:22
196     2018-01-02  화    1     1   850970432  정상회원    채소  ...  남  45.0  40대   4786  매장C      NaN  
17:11
197     2018-01-02  화    1     1   850970432  정상회원   축산물  ...  남  45.0  40대   6892  매장C      NaN 
 17:11
328     2018-01-02  화    1     1  1090633856    탈퇴    채소  ...  남  41.0  40대   4403  매장D      NaN  17:09
...            ... ..  ...   ...         ...   ...   ...  ... ..   ...  ...    ...  ...      ...    ...      
705197  2018-06-30  토    6    26   273041728  정상회원    반찬  ...  남  44.0  40대   9668  매장C      NaN  
13:53
705258  2018-06-30  토    6    26   163435648  정상회원    수산  ...  남  49.0  40대  26802  매장C      NaN  
17:20
705334  2018-06-30  토    6    26   408947328  정상회원   축산물  ...  남  46.0  40대  23739  매장D      NaN 
 12:31
705335  2018-06-30  토    6    26   408947328  정상회원    반찬  ...  남  46.0  40대   3733  매장D      NaN  
12:31
705542  2018-06-30  토    6    26   932214976  정상회원    간식  ...  남  41.0  40대   7466  매장A      NaN  
11:36

[12514 rows x 20 columns]
'''

# bit 연산에는 & , | , ~ 있을 것임


# 연습 몇가지 해보기

# 30대 여성 중 구매금액 내림차순으로 정리해보기
cond1 = (df1['연령대'] == '30대이하')
cond2 = (df1['성별'] == '여')

print(df1.loc[cond1 & cond2].sort_values(by='구매금액', ascending=False))
'''
              공급일자 요일  공급월  공급주차        회원번호 조합원상태 물품대분류  ... 성별    연령    연령
대     구매금액 구매매장    반품_원거래일자   구매시각
155255  2018-02-09  금    2     6   236805184  정상회원    건강  ...  여  39.0  30대이하  1448255  매장B     
    NaN  12:17
154682  2018-02-09  금    2     6   236805184  정상회원    건강  ...  여  39.0  30대이하   631757  매장B     
    NaN  12:17
154683  2018-02-09  금    2     6   236805184  정상회원    수산  ...  여  39.0  30대이하   604955  매장B     
    NaN  12:17
124021  2018-02-01  목    2     5   796003136  정상회원    건강  ...  여  39.0  30대이하   499662  매장A     
    NaN  15:51
682834  2018-06-25  월    6    26   678182400  정상회원    건강  ...  여  33.0  30대이하   499662  매장A     
    NaN  11:12
...            ... ..  ...   ...         ...   ...   ...  ... ..   ...    ...      ...  ...         ...    ...
638874  2018-06-15  금    6    24  1023108864  정상회원    건강  ...  여  36.0  30대이하  -118694  매장C  20180611.0  10:28
357637  2018-04-02  월    4    14   678182400  정상회원    건강  ...  여  33.0  30대이하  -126351  매장C  20180402.0  16:27
330306  2018-03-26  월    3    13   584736512  정상회원  생활용품  ...  여  39.0  30대이하  -127309  매장A   
      NaN  17:14
482357  2018-05-04  금    5    18  1438455680  정상회원    수산  ...  여  37.0  30대이하  -127691  매장A  20180504.0  16:32
209220  2018-02-23  금    2     8  1122725952  정상회원    건강  ...  여  37.0  30대이하  -166554  매장D  20180223.0  16:43

[94886 rows x 20 columns]
'''

# 새로만들어진 테이블을 df3로 저장해서 파일로 보내기까지 해보자

df3 = df1.loc[cond1 & cond2].sort_values(by='구매금액', ascending=False)

df3.to_csv('result.csv') # 이렇게하면 한글이 모두 깨짐

df3.to_csv('result.csv', encoding='cp949') # 한글 지원해주는 인코더 옵션 추가
