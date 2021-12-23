import random,time

numofqns = 10
crctanswers = 0

for i in range(numofqns):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    ans = num1*num2
    prompt = '#%s: %s x %s = ' % (i,num1,num2)
    tries=1

    while True:
        start= time.time()
        user_ans = int(input(prompt))
        end=time.time()
        sec = int(end - start)

        if sec >= 8:
            print('Timeout')
            break
        if user_ans==ans:
            print('Correct !')
            crctanswers+=1
            time.sleep(1)
            break
        else:
            print('Wrong! Try again')
        if tries==3:
            print('Out of chances :(')
            break
        tries += 1

print('Score : %s/%s' % (crctanswers,numofqns))
