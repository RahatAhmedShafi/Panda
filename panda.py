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

import pandas as pd
data=pd.read_csv("datasate.csv")
new_data=data.dropna()
print(data.to_string())