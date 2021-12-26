import os,re,shutil

folder = input("Enter the absolute path of the folder to be searched: ")
prefix = input("Enter the prefix of the files to be searched: ")
extension = input("Enter the extension of the file to be searched: ")

prefixregex = re.compile('({})(\d\d\d)({})'.format(prefix,extension))

i=1

for filename in os.listdir(folder):
    prefixfile = prefixregex.search(filename)
    if prefixfile:
        oldfile = os.path.join(folder,filename)
        newfilename = prefixfile.group(1) + str(i).zfill(3) + prefixfile.group(3)
        newfile = os.path.join(folder,newfilename)
        shutil.move(oldfile,newfile)
        print('renaming {} to {}'.format(oldfile,newfile))
        i+=1


