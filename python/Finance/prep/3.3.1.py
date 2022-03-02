import pandas as pd

df = pd.DataFrame( {'KOSPI' : [1915, 1961, 2026, 2467, 2041],
                    'KOSDAQ' : [541, 682, 631, 798, 675]},
                    index = [2014, 2015, 2016, 2017, 2018] )

print( df )
'''
      KOSPI  KOSDAQ
2014   1915     541
2015   1961     682
2016   2026     631
2017   2467     798
2018   2041     675
'''

print( df.describe() )
'''
             KOSPI     KOSDAQ
count     5.000000    5.00000
mean   2082.000000  665.40000
std     221.117616   93.01774
min    1915.000000  541.00000
25%    1961.000000  631.00000
50%    2026.000000  675.00000
75%    2041.000000  682.00000
max    2467.000000  798.00000
'''

print( df.info() )
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 5 entries, 2014 to 2018
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   KOSPI   5 non-null      int64
 1   KOSDAQ  5 non-null      int64
dtypes: int64(2)
memory usage: 120.0 bytes
None
'''

df = pd.DataFrame( {'KOSPI' : [1915, 1961, 2026, 2467, 2041],
                    'KOSDAQ' : [541, 682, 631, 798, 675]},
                    index = [2014, 2015, 2016, 2017, 2018] )

for i in df.index:
    print(i, df['KOSPI'][i], df['KOSDAQ'][i])
'''
2014 1915 541
2015 1961 682
2016 2026 631
2017 2467 798
2018 2041 675
'''