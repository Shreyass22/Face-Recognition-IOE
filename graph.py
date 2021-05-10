import pandas as pd
import matplotlib.pyplot as plt

excel_data_df = pd.read_csv('attendz.csv')
V = excel_data_df['Total'].tolist()
print(V)
left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
height = V
tick_label = ['28/04/2021', '29/04/2021', '30/04/2021', '01/05/2021', '02/05/2021', '03/05/2021',
              '04/05/2021', '05/05/2021', '06/05/2021', '07/05/2021']
plt.bar(left, height, tick_label=tick_label, width=0.8)
plt.xlabel('Week wise')
plt.ylabel('Count of Students')
plt.title('Weekly report Count!')
plt.show()