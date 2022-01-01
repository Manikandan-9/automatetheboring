import ezsheets,os

input_file = input('Enter the name of the file to be uploaded: ')

ss = ezsheets.upload(input_file)

ss.downloadAsODS()
ss.downloadAsHTML()
ss.downloadAsCSV()
ss.downloadAsPDF()