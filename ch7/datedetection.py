import re
c = re.compile('([0-3]\d)/([0-1]\d)/([1-2]\d{3})')
date_input = input()
date = c.findall(date_input)
if date!=[]:
  day,month,year = c.search(date_input).groups()

def check_date(day,month,year,date):
  leap_year=(int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 4 == 0 and int(year) % 100 == 0 and int(year) % 400 == 0)
  if date!=[]:
    if int(day)>31:
      return False
    if int(month)>12:
      return False
    if int(month) in [3,6,9,11] and int(day)>30:
      return False
    elif int(month)==2:
      if int(day)>28 and not leap_year:
        return False
      elif int(day)>29 and leap_year:
        return False
    return True
  
  else:
    return False

if check_date(day,month,year,date):
  print('It is a valid date')
else:
  print('Not a valid date')


