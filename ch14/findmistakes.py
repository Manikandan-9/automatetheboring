import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss[0]

for rownum in range(2,sheet.rowCount):
    if sheet.getRow(rownum)[0] != '':
        if int(sheet.getRow(rownum)[0])*int(sheet.getRow(rownum)[1]) == int(sheet.getRow(rownum)[2]):
            continue
        else:
            print('row no',rownum,'is incorrect')
   

