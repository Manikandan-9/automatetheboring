def CommaCode(L):
  s = ''
  for i in L:
    if i!= L[-1]:
      s+= str(i) + ', '
    else:
      s+= 'and ' + str(i)
  return s
f = list(input().split())
x = CommaCode(f)
print(x)
