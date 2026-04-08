def guess_number():
    import random

    target = random.randint(1, 100)
    count = 0

    while True:
        guess = int(input("请输入你猜的数字（1-100）："))
        count += 1

        if guess > target:
            print("猜大了")
        elif guess < target:
            print("猜小了")
        else:
            print(f"猜对了，一共猜了{count}次")
            break

guess_number()


def fact(n,*args):
    s = 1
    
    