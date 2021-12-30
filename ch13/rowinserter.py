import sys,openpyxl

N = int(sys.argv[1])
M = int(sys.argv[2])
filename = sys.argv[3]

wb = openpyxl.load_workbook(filename)
sheet = wb.active
wb2 = openpyxl.Workbook()
sheet2 = wb2.active

for row in range(1,sheet.max_row + 1):
    for col in range(1,sheet.max_column + 1):
        if row<N:
            sheet2.cell(row=row,column=col).value = sheet.cell(row=row,column=col).value
        else:
            sheet2.cell(row=row+M,column=col).value = sheet.cell(row=row,column=col).value

wb2.save('rowinserter.xlsx')

