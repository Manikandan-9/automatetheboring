import re,os

userregexstr = input('Enter the regular expression to be searched: ')
userregex = re.compile(userregexstr)

files = os.listdir(os.getcwd())
txtfiles = []

txtregex = re.compile('.txt')


for file in files:
    if txtregex.search(file):
        txtfiles.append(file)

for file in txtfiles:
    file1 = open('{0}/{1}'.format(os.getcwd(),file)).read()
    matches = userregex.findall(file1)

print(','.join(matches))