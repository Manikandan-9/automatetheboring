import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    L = []
    for i in range(100):
      L.append(random.randint(0,1))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(1,len(L)):
      
      if L[i] == L[i-1]:
        streak += 1
      else:
        streak = 0

      if streak ==6:
        numberOfStreaks += 1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
