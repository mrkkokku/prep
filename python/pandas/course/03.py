import pandas as pd

# df1 객체에? 인스턴스에? csv 로드 후 shape와 head를 확인
df1 = pd.read_csv('example.csv')

print(df1.shape)

print(df1.head())


# 이제 이거를 추출하거나 정렬하거나 등을 해보자

# DataFrame은 3가지로 구성되어있다
# df1.columns
# df1.index
# df1.values
# 이런 변수를 가지고 있다

# describe는 요약해서 빠르게 보여준다
print(df1.describe())

# info는 전체 요약정보를 보여준다
print(df1.info())

# 하나의 컬럼에대해 대괄로 하나로 입력하면 그 출력이 series로 나옴
# 하나 이상의 컬럼에 대해 대괄호 이중으로 입력하면 그 출력이 dataframe으로 나옴



# 데이터 행 추출을 해보자 (인덱싱 하듯이 하면 됨)
print(df1.iloc[0]) # 1행에 대한 정보만 싹 나옴

print(df1.iloc[-1]) # 마지막 행에 대한 정보만 나옴

print(df1.iloc[0:11]) # 상위 10개의 데이터가 나오겠지



# 이제 데이터 정렬에 대해 알아보자
# 특정 컬럼 기준으로 오름차순 또는 내림차순 하기

# 구매금액 기준으로 데이터 정렳보기
df1.sort_values(by='구매금액') # 이렇게하면 오름차순으로 정렬됨
df1.sort_values(by='구매금액', ascending=False) # 이렇게하면 내림차순으로 정렬

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

# 순서대로 해보자
cond1 = (df1['연령대'] == '40대') # 이렇게하면 현재 df1의 정렬순과 똑같이 40대 여부가 series로 출력되며 그 값을 cond1이 가지고 있을 것

print(df1.loc[cond1]) # cond1과 loc의 조합으로 특정열만 출력하게 됨

print(df1.loc[cond1].shape) # 위의 조건에 맞는 출력값에 대한 shape확인

# loc는 로케이션이며, 비슷하게 사용가능한게 많지만 이게 대표적임


# 또 다른조건으로 해보자, 남자면서 40대인것 찾기

print(df1['성별'].value_counts())

cond1 = (df1['연령대'] == '40대')
cond2 = (df1['성별'] == '남')

print(df1.loc[cond1 & cond2]) # 이렇게 비트연산으로 series 두개를 and해버리면 동시만족하는 조건의 것만 잡을 수 있는 것임

# bit 연산에는 & , | , ~ 있을 것임


# 연습 몇가지 해보기

# 30대 여성 중 구매금액 내림차순으로 정리해보기
cond1 = (df1['연령대'] == '30대이하')
cond2 = (df1['성별'] == '여')

print(df1.loc[cond1 & cond2].sort_values(by='구매금액', ascending=False))

# 새로만들어진 테이블을 df3로 저장해서 파일로 보내기까지 해보자

df3 = df1.loc[cond1 & cond2].sort_values(by='구매금액', ascending=False)

df3.to_csv('result.csv') # 이렇게하면 한글이 모두 깨짐

df3.to_csv('result.csv', encoding='cp949') # 한글 지원해주는 인코더 옵션 추가