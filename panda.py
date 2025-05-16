# import pandas as pd
# df=pd.read_csv("sales_data_sample.csv",encoding="latin1")
# print(df)

# import pandas as pd
# data={
#     "name":["Rahat","Ahmed","Shafi"],
#     "age":[24,23,25],
#     "City":["Dhaka","Khulna","Sylhet"]
# }

# df=pd.DataFrame(data)
# print(data)
# df.to_csv("savingdata.csv")

# import pandas as pd
# a=[3,4,5,6,10]
# # data=pd.Series(a)
# data=pd.Series(a,index=["x","y","z","p","q"])
# print(data)
# fruits={
#     "name1":"Apple",
#     "name2":"Banana",
#     "name3":"Orange"
# }
# ft=pd.Series(fruits)
# print(ft)

# import pandas as pd
# car={
#     "name":["Toyota","Tesla","Oddy"],
#     "Miles":[400,300,500]
# }
# cr=pd.DataFrame(car)
# print(cr.loc[[0,1]])

# import pandas as pd
# df=pd.read_csv("IPL_2023_DATASET.csv")
# print(df.to_string()) # this is show all of the values
# print(df.tail(10))



# import pandas as pd
# from io import StringIO

# data = """Duration,Date,Pulse,Maxpulse,Calories
# 60,'2020/12/27',92,118,241.0
# 60,'2020/12/28',103,132,NaN
# 60,'2020/12/29',100,132,280.0
# 60,'2020/12/30',102,129,380.3
# 60,'2020/12/31',92,115,243.0
# """

# df = pd.read_csv(StringIO(data))
# print("Original:\n", df)

# new_df = df.dropna()
# print("\nAfter dropna():\n", new_df)

#----------------------------





# import pandas as pd

# # Load the CSV and treat standard missing values correctly
# df = pd.read_csv("datasate.csv")
# df['Date']=pd.to_datetime(df['Date'], format='mixed')
# print(df.to_string())



# import pandas as pd

# # Load the CSV and treat standard missing values correctly
# df = pd.read_csv("datasate.csv")
# df.loc[7,'Duration']=45
# print(df.to_string())

# import pandas as pd

# # Load the CSV and treat standard missing values correctly
# df = pd.read_csv("datasate.csv")
# print(df.duplicated())

import pandas as pd

# Load the CSV and treat standard missing values correctly
df = pd.read_csv("datasate.csv")
df.drop_duplicates(inplace=True)
print(df.to_string())