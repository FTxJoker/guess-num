import random
start = input('請決定隨機數字起始值: ')
end = input('請決定隨機數字結束值: ')
start = int(start)
end = int(end)

num = random.randint(start, end)
count = 0
while True:
    count += 1
    r = input('請猜一個數字: ')
    r = int(r)
    if r == num:
        print('猜對了!')
        break
    elif r < num:
        print('比答案小')
    elif r > num:
        print('比答案大')
print('本次總共猜了', count, '次')
