import random

num = random.randint(1, 100)
count = 0
while True:
    count += 1
    r = input('請猜一個數字: ')
    r = int(r)
    if r == num:
        print('猜對了!')
        break
    elif r < num and r >= 0:
        print('比答案小')
    elif r > num and r <= 100:
        print('比答案大')
    else:
        print('只能輸入1 ~ 100!')
print('本次總共猜了', count, '次')
