
def gcd_1():
    x=int (input('x ='))
    y=int (input('y ='))

    for i in range (x ,0, -1):
        if x % i==0 and y%i==0:
            print(f'最大公约数是：{i}')
            break

def gcd_2():
    x=int (input('x ='))
    y=int (input('y ='))

    while y % x!=0:
        x, y= y % x, x
    print(f'最大公约数：{x}')

def random_number():
    import random

    answer = random.randrange(1, 101)
    counter = 0
    while True:
        counter += 1
        num= int (input('请输入'))
        if num < answer:
            print('小了')
        elif num > answer:
            print('大了')
        else:
            print('对了')
            break
    print(f'你一共猜对了{counter}次')



def run():
    m=int(input('选择运行的程序：'))
    if m==1:
        gcd_1()
    if m==2:
        gcd_2()
    if m==3:
        random_number()

if __name__=="__main__":
    run()
