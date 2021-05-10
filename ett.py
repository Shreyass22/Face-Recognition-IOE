# import openpyxl as op
#
# col1 = input("Enter the name: ")
# col2 = int(input("Enter 0/1: "))
# wb = op.load_workbook('attend.xlsx')
# wb.sheetnames
# ws = wb["Sheet1"]
# ws.append([col1, col2])
# wb.save('attend.xlsx')
# wb.close()

# Import writer class from csv module
from csv import writer

col1 = input("Enter the name: ")
col2 = int(input("Enter 0/1: "))
List=[col1, col2]
with open('atten.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(List)
    f_object.close()