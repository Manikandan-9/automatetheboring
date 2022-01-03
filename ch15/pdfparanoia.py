import sys,PyPDF2,os

password = sys.argv[1]
folder = input('Enter path of folder to be searched: ')

for folder, subfolders, files in os.walk(folder):
    for file in files:
        if file.endswith('.pdf'):
                        
            pdf = open(os.path.join(folder, file), 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf)
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_writer.encrypt(password)
        
            for pagenum in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(pagenum)
                    pdf_writer.addPage(page)
            
            newpdfpath = os.path.join(folder, file[:-4] + '_encrypted.pdf')
            newpdf = open(newpdfpath,'wb')
            pdf_writer.write(newpdf)
            pdf.close()
            newpdf.close()

print('Encryption Complete')