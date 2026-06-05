import pandas as pd
#for reading csv file
data_read = pd.read_csv('student_records_100x20 (2) (1).csv')
# print(data)
# coll = data.loc[2]
# print(coll)
data_frame  = pd.DataFrame(data_read)
# print(data_frame)
# print(data_frame.columns)
#for deleting a column
# print(data_frame.ndim)
print(data_frame.shape)
# print(data_frame.T)
# print(data_frame.axes)
# print(data_frame.head())
# print(data_frame.tail())
# print(data_frame.values.ndim)
#for selecting a column
# a=data_frame['Math_Score']
# print(a)
b=data_frame.loc[ 'Math_Score':'History_Score']
# print(b)
# print(type(a))
# print(a.cumsum())
