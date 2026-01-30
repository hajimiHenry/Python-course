
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


def sum_1_to_100_for():
    """用 for 循环计算 1~100 的和。"""
    total = 0
    for i in range(1, 101):
        total += i
    return total


def sum_odds_1_to_99_for():
    """用 for 循环计算 1~99 的奇数和。"""
    total = 0
    for i in range(1, 101, 2):
        total += i
    return total


def sum_evens_2_to_100_builtin():
    """用内置 sum + range 计算 2~100 的偶数和。"""
    return sum(range(2, 101, 2))


def sum_1_to_100_while():
    """用 while 循环计算 1~100 的和。"""
    total = 0
    i = 1
    while i <= 100:
        total += i
        i += 1
    return total


def sum_evens_2_to_100_while():
    """用 while 循环计算 2~100 的偶数和。"""
    total = 0
    i = 2
    while i <= 100:
        total += i
        i += 2
    return total


def sheet9x9():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f'{i}x{j}={i*j}', end='\t')
        print()


def run_all_x3():
    print("1) for: 1~100 求和 =", sum_1_to_100_for())
    print("2) for: 1~99 奇数和 =", sum_odds_1_to_99_for())
    print("3) sum(range): 2~100 偶数和 =", sum_evens_2_to_100_builtin())
    print("4) while: 1~100 求和 =", sum_1_to_100_while())
    print("5) while: 2~100 偶数和 =", sum_evens_2_to_100_while())
    print("6) 输出乘法表：")
    sheet9x9()
def time():
    import time

    for i in range(3600):
        print('hello')
        time.sleep(1)


def run():
    menu = (
        "\n选择运行的程序：\n"
        "  1) 最大公约数（for 试除法）\n"
        "  2) 最大公约数（辗转相除法）\n"
        "  3) 猜数字游戏\n"
        "  4) 每秒打印一次 hello（3600 秒）\n"
        "  5) for: 1~100 求和\n"
        "  6) for: 1~99 奇数和\n"
        "  7) sum(range): 2~100 偶数和\n"
        "  8) while: 1~100 求和\n"
        "  9) while: 2~100 偶数和\n"
        "  10) 9x9 乘法表\n"
        "  a) 运行 x3 全部\n"
        "请输入编号："
    )
    choice = input(menu).strip().lower()

    if choice == "1":
        gcd_1()
    elif choice == "2":
        gcd_2()
    elif choice == "3":
        random_number()
    elif choice == "4":
        time()
    elif choice == "5":
        print(sum_1_to_100_for())
    elif choice == "6":
        print(sum_odds_1_to_99_for())
    elif choice == "7":
        print(sum_evens_2_to_100_builtin())
    elif choice == "8":
        print(sum_1_to_100_while())
    elif choice == "9":
        print(sum_evens_2_to_100_while())
    elif choice == "10":
        sheet9x9()
    elif choice in {"a", "all"}:
        run_all_x3()
    else:
        print("输入无效：请输 1~10 或 a")

if __name__=="__main__":
    run()
