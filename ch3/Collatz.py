def collatz(number):
  if number % 2 == 0:
    print(number // 2)
    return number // 2
  elif number % 2 == 1:
    print(3 * number + 1)
    return 3 * number + 1


try:
  number = int(input())
except ValueError:
  print("Error : Enter an integer")
  
while True:
  number = collatz(number)
  if number == 1:
    break
