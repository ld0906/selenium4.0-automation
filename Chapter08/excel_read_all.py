import xlrd
xls = xlrd.open_workbook('test.xlsx')

sheet = xls.sheet_by_index(0)
print(sheet.nrows)
print(sheet.ncols)

for r in range(sheet.nrows):
    for c in range(sheet.ncols):
        print(sheet.row_values(r)[c])