import ezsheets
ss = ezsheets.Spreadsheet('https://docs.google.com/spreadsheets/d/1PP_84jk0HkDU8M4krSXTC04UOJQkSirbDOqlD3GSr9Y/edit?resourcekey#gid=1436516852')
sheet = ss[0]
columns = sheet.getColumn(3)
emails = []
for data in columns:
    if data.endswith('.com'):
        emails.append(data)
print(emails)