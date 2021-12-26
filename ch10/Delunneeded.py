import os

folder = input('Enter the absolute path of the folder you want to search: ')

for foldername,subfolders,filenames in os.walk(folder):
    for filename in filenames:
        size = os.path.getsize(os.path.join(foldername,filename))

        if size>100000000:
            print(os.path.join(foldername,filename) ,'is larger than 100 MB.')