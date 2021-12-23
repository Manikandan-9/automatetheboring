import pyinputplus as pyin

prices = {'wheat':10,'white':15,'sourdough':20,'chicken':80,'turkey':90,'ham':90,'tofu':70,'cheddar':5,'swiss':10,'mozarella':10,'mayo':5,'mustard':5,'lettuce':5,'tomato':5}

bread = pyin.inputMenu(['wheat','white','sourdough'])
protien = pyin.inputMenu(['chicken', 'turkey', 'ham','tofu'])

total_price = prices[bread]+prices[protien]

cheese = pyin.inputYesNo('Do you want cheese? ')
if cheese=='yes':
    cheesetype = pyin.inputMenu(['cheddar', 'swiss', 'mozzarella'])
    total_price+=prices[cheesetype]

mayo = pyin.inputYesNo('Do you want mayo? ')
if mayo=='yes':
    total_price+=prices['mayo']
mustard=pyin.inputYesNo('Do you want mustard? ')
if mustard=='yes':
    total_price+=prices['mustard']
lettuce=pyin.inputYesNo('Do you want lettuce? ')
if lettuce=='yes':
    total_price+=prices['lettuce']
tomato=pyin.inputYesNo('Do you want tomato? ')
if tomato=='yes':
    total_price+=prices['tomato']

sandwiches = pyin.inputInt('How many sandwiches do you want? ',min=1)

total_price *= sandwiches

print('Your total price: ',total_price)