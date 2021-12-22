import re

passw = input()

lenRegx = re.compile('.{8,}')
upRegx = re.compile('[A-Z]')
lowRegx = re.compile('[a-z]')
digRegx = re.compile('\d')

def checkpass(passw):
  if not lenRegx.findall(passw):
    return False
  if not upRegx.findall(passw):
    return False
  if not lowRegx.findall(passw):
    return False
  if not digRegx.findall(passw):
    return False
  return True

if checkpass(passw):
  print('That is a strong password!')
else:
  print('That is weak password, I would recommend changing it.')
