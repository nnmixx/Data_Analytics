import pandas as pd
#empty series
s1 = pd.Series()
print(s1)
s2 = pd.Series([12,20,30,40])
print(s2)
data = [1,2,3,4,5]
index = ['a','b','c','d','e']
s3 = pd.Series(data, index=index)
print(s3)