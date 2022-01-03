import os,csv,openpyxl

folder = input('Enter the folder to be searched: ')

for file in os.listdir(folder):
    if file.endswith('.xlsx'):
        wb = openpyxl.load_workbook(file)

        for sheetname in wb.get_sheet_names():
            
            sheet = wb.get_sheet_by_name(sheetname)
                       
            csvfile = open(file[: -5] + '_' + sheetname + '.csv', 'w', newline='')
            csvwriter = csv.writer(csvfile)

            for row in range(1, sheet.max_row + 1):
                rows = []
                for col in range(1, sheet.max_column + 1):
                    rows.append(sheet.cell(row=row, column=col).value)

                                
                csvwriter.writerow(rows)
            csvfile.close()