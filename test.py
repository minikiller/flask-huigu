from openpyxl import load_workbook
workbook = load_workbook(filename="sun.xlsx")
print(workbook.sheetnames)
# sheet = workbook.active
sheet = workbook['学生基础信息']
# print(sheet)
# cell_obj = sheet.cell(row = 1, column = 1) 
  
# # Print value of cell object  
# # using the value attribute 
# print(cell_obj.value) 

# get max row count
max_row=sheet.max_row
# get max column count
max_column=sheet.max_column
# iterate over all cells 
# iterate over all rows
for i in range(1,max_row+1):
     
     # iterate over all columns
     for j in range(1,max_column+1):
          # get particular cell value    
          cell_obj=sheet.cell(row=i,column=j)
          # print cell value     
          print(cell_obj.value,end=' | ')
     # print new line
     print('\n')