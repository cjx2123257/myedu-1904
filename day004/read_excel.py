import xlrd

def read_excel_list(file):
    l = []
    wb = xlrd.open_workbook(filename=file)

    sheet1 = wb.sheet_by_index(0)
    for i in range (1,sheet1.nrows):
        d = []
        d = sheet1.row_values(i)
        l.append(d)
    return l

if __name__ == '__main__':
    excel_list = read_excel_list('exe.xlsx')
    print (excel_list)
