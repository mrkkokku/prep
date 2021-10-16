import pandas as pd

# 오늘은 날짜데이터를 처리하는 방법에 대해서 알아보자

df1 = pd.read_csv('Data01.csv')
print(df1.shape)
print(df1.head())

print(df1['날짜']) 
'''
14998    2019-08-07
14999    2019-08-07
Name: 날짜, Length: 15000, dtype: object
'''
# 날짜데이터는 object로 인식되고 있음을 알수 있다

# 요일별 수량, 특정기간 수량 등의 작업을 위해선 이게 object로는 쉽지않으니
# 다른 처리 방법을 알아보자

print( pd.to_datetime(df1['날짜']) )
'''
14998   2019-08-07
14999   2019-08-07
Name: 날짜, Length: 15000, dtype: datetime64[ns]
'''
# 이렇게 to_datetime 함수를 통해 날짜 형식으로 변환을 시켜주게 됨


df1['날짜_datetime'] = pd.to_datetime(df1['날짜']) # 이렇게 새로운 열을 만들어 줌

print( df1['날짜_datetime'].dt.year ) # 이렇게하면 년도만 쫙 출력 됨
'''
14997    2019
14998    2019
14999    2019
'''

df1['연도'] = df1['날짜_datetime'].dt.year # 연도 컬럼을 새로 만들어 줌


print( pd.pivot_table(data=df1, index='연도', values='출고수량', aggfunc='sum') )
# 연도별 출고수량을 피벗테이블 출력
'''
     출고수량
연도
2019  108078
'''

df1['월'] = df1['날짜_datetime'].dt.month
df1['주차'] = df1['날짜_datetime'].dt.week
df1['일자'] = df1['날짜_datetime'].dt.day
df1['요일'] = df1['날짜_datetime'].dt.day_name()


print( df1.head() )


print( pd.pivot_table(data=df1, index='월', values='출고수량', aggfunc='sum') )
''' 
   출고수량
월
5  19427
6  39397
7  40584
8   8670
''' 
# 월별 출고수량을 쉽게 알 수 있다

# 심지어 이걸 그래프로도 바로 볼 수 있다
print( pd.pivot_table(data=df1, index='월', values='출고수량', aggfunc='sum').plot(kind='bar') )
