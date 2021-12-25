from pathlib import Path
import re

filename = input("Enter the name of the file you want to read from : ")
filename2= input("Enter the name of the file you want to write to : ")

file = open('{0}/{1}.txt'.format(Path.cwd(),filename)).read()
file2 = open('{0}/{1}.txt'.format(Path.cwd(),filename2),'w')

madlib_regex = re.compile(r'(NOUN|VERB|ADVERB|ADJECTIVE)')
matches = madlib_regex.findall(file)

for match in matches:
    ans = input("Enter an {0} : ".format(match))
    file = file.replace(match,ans,1)
file2.write(file)

file.close()
file2.close()

print(file)