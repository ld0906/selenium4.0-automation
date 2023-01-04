import xlrd

def read_excel(filename,index,cloumn):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    print(sheet.nrows)
    print(sheet.ncols)
    data=[]
    for i in range(sheet.nrows):
        data.append(sheet.row_values(i)[0])
 #      print (sheet.row_values(i)[0])
    return  data