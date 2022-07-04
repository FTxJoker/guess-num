import random
num = random.randint(1, 100)
while True:
    r = input('請猜一個數字: ')
    r = int(r)
    if r == num:
        print('終於猜對了!')
        break
    elif r < num and r >= 0:
        print('比答案小')
    elif r > num and r <= 100:
        print('比答案大')
    elif r > 100 or r < 0:
        print('只能輸入1 ~ 100!')
