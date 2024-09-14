# pandas store tabular  data using a dataframe
#a dataframe is a 2d labelled data structure like a table in databases
# every dataframe contains rows and column and therefore has both a row and cloumn index
#each column can have a different type of values


import pandas as pd
std_data=[(1,'monu',70,'male','delhi'),
          (2,'sonu',70,'male','delhi'),
          (3,'gonu',70,'male','delhi'),
          (4,'tonu',70,'male','delhi')]
df=pd.DataFrame(std_data)
print(df)


std_data=[(1,'monu',70,'male','delhi'),
          (2,'sonu',70,'male','delhi'),
          (3,'gonu',70,'male','delhi'),
          (4,'tonu',70,'male','delhi')]
df=pd.DataFrame(std_data,columns=['stud_id','name','age','gender','city'])
print(df)
df.loc[2,'student_age']=72

df=pd.read_csv("student.csv")
print(df)


# df['age']
# delete df['age']
# df=df.drop(4)
# df.head()
# df.shape()
# df.columns()
# df.size()
# df.dtypes()
# df.values()
# df.index()
