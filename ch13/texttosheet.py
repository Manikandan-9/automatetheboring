import openpyxl,os


folder = input("Enter folder path: ")

wb = openpyxl.Workbook()
sheet = wb.active

textfiles =[]

for file in os.listdir(folder):
    if file.endswith('.txt'):
        text = open(os.path.join(folder,file)).readlines()
        textfiles.append(text)


col = 1
for text in textfiles:
    row=1
    for line in text:
        sheet.cell(row=row,column=col).value = line
        row+=1
    col+=1

wb.save('texttosheet.xlsx')
