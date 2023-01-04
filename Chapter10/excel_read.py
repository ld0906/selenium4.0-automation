import xlrd
xls = xlrd.open_workbook('test.xlsx')
# sheet = xls.sheets()[0] #通过sheets()方法获取sheet
# sheet = xls.sheet_by_name('Sheet1') #通过sheet_by_name()方法获取sheet
sheet = xls.sheet_by_index(0) #通过sheet_by_index()方法获取sheet
print(sheet.nrows) #打印表格总行数
print(sheet.ncols) #打印表格总列数
print(sheet.row_values(1)[0]) #打印表格第2行，第1列单元格

