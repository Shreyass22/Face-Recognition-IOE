import pandas as pd
import matplotlib.pyplot as plt

excel_data_df = pd.read_csv('csvatten.csv')
V = excel_data_df['Auth'].tolist()
df = pd.DataFrame({'Auth': excel_data_df['Auth'].tolist()})
counts = df['Auth'].value_counts()
counts.plot.pie(autopct='%.2f%%')
plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# csv_file='csvatten.csv'
# data = pd.read_csv(csv_file)
# Name = data["Name"]
# Auth = data["Auth"]
# x=[]
# y=[]
# x=list(Auth)
# y=list(Name)
# plt.scatter(x,y)
# plt.xlabel('Auth->')
# plt.ylabel('Name->')
# plt.title('Data')
# plt.show()
# # plt.pie(x,labels=y,autopct='%.2f%%')