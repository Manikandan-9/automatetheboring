import PyPDF2

file = input('enter file to be decrypted: ')

words = open('dictionary.txt').readlines()
pdf = PyPDF2.PdfFileReader(open(file,'rb'))

for word in words:
    word = word.strip()
    if pdf.decrypt(word.upper())==1 or pdf.decrypt(word.lower())==1:
        print(word,'is the password!!!')
        break
