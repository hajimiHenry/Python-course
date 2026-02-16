import random

x = random.randint(1,100)


while True:
    while True:
        try:
            guess = int (input ("请输入你的猜测数数字"))
            break
        except ValueError:
            print("输入数字不合法")
            continue

    if guess < x:
        print ("你猜小了")
    elif guess > x:
        print ("你猜大了")
    elif guess == x:
        print("你猜对了")
        break