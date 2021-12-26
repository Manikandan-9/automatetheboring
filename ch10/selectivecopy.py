import os,re,shutil

folder = input("Enter name of the folder to be searched: ")
filextention = input("Enter the file extension to be searched: ")
newfolder = input("Enter name of the folder to copy the files to:  ")

for foldername,subfolders,filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith(filextention):
            shutil.copy(os.path.join(foldername,filename),newfolder)

print("Done Copying.")
