import pandas as pd

''' 
pandas는 Numpy를 바탕으로 만들어짐
pandas에는 기본 타입이 두가지 있음

이 강의에선 pandas에 사용되는 기본자료형 두가지에 대해서 다룸

Series
- index - value 가 짝을 이룸

Dataframe
- index - column - value 로 구성
'''

s1 = pd.Series([10, 20, 30, 40])
print(s1)
'''
0    10
1    20
2    30
3    40
dtype: int64
'''

s1.sum()
s1.mean()


s2 = pd.Series(['분식이', '쏜', '홍길동','변사또'], index=['하나', '둘', '셋', '넷'], name='출석부')
print(s2)
'''  series 안에 옵션으로 인덱스, 그리고 이 데이터 전체의 이름을 '출석부'로 설정하는 등의 작업이 가능 하다
하나    분식이
둘       쏜
셋     홍길동
넷     변사또
Name: 출석부, dtype: object
'''


s3 = pd.Series({'name':'김분식', 'age':30, 'gender':'male', 'job':'분석가'})
# 시리즈에 딕셔너리를 넣으면 키가 인덱스로, 밸류가 밸류로 들어간다
# 데이터 타입은 리스트를 넣었을때와는 다름을 확인
'''
하나    분식이
둘       쏜
셋     홍길동
넷     변사또
Name: 출석부, dtype: object
'''


# series도 indexing이 가능하다, 애초에 순서가 있는 자료형이기 때문
s4 = pd.Series(['국어', '수학', '사회', '과학'])
print(s4)
print(s4[0])
'''
0    국어
1    수학
2    사회
3    과학
dtype: object
국어
'''

print(s4[0:2])
'''
0    국어
1    수학
dtype: object
'''

print(s3 == '분석가')
'''
name      False
age       False
gender    False
job        True
dtype: bool
'''

# Series는 데이터의 순서를 표현하는 자료구조다. 라고 이해



# DataFrame에 대해 알아보자

print(pd.DataFrame([10,20,30,40,50]))
'''
    0
0  10
1  20
2  30
3  40
4  50
'''

print(pd.DataFrame([ 
                   [10,20,30,40], 
                   ['철수', '영희', '분식', '은희'] 
                   ])
                   )
''' 
    0     1     2     3
0  10     20   30    40
1  철수  영희  분식  은희
'''

df1 = pd.DataFrame([[1000, '과자', '2019-12-31', '반품'],
                    [2000, '음료', '2020-03-02', '정상'],
                    [3000, '크림', '2020-02-03', '정상'],
                    [1000, '과자', '2019-12-31', '반품']]
                    , columns=['가격','종류','판매일자','반품여부'])
print(df1)
'''
   가격  종류   판매일자    반품여부
0  1000  과자  2019-12-31   반품
1  2000  음료  2020-03-02   정상
2  3000  크림  2020-02-03   정상
3  1000  과자  2019-12-31   반품
'''

print(df1['가격'])
# 이 출력값은 series로 나오는 것에 유의,
'''
0    1000
1    2000
2    3000
3    1000
Name: 가격, dtype: int64
'''

print(df1['종류'])
# 문자를 출력한땐 타입이 달라짐
'''
0    과자
1    음료
2    크림
3    과자
Name: 종류, dtype: object
'''

print(df1['가격'].mean())
'''
1750.0
'''

print(df1[['가격']])
# 이렇게 대괄호안의 대괄호를 쓰면 그 출력값이 DataFrame으로 나옴
'''
     가격
0  1000
1  2000
2  3000
3  1000
'''

