import re

string = input('Enter the string needed to be stringipped: ')
change = input('Enter the character you want to be removed: ')


def strip(string, change):
    if change != '':
        change_regex = re.compile(change)
        string = change_regex.sub('', string)
        return string
    else:
        change_regex = re.compile('^\s*')
        string = change_regex.sub('', string)
        change_regex = re.compile('\s*$')
        string = change_regex.sub('', string)
        return string


string = strip(string, change)
print(string)
