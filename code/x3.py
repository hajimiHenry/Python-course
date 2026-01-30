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
    for i in range(1 , 10):
        for j in range( 1, 10):
            print(f'{i}x{j}={i*j}',end='\t')
    print()
    



def run_all():
    print("1) for: 1~100 求和 =", sum_1_to_100_for())
    print("2) for: 1~99 奇数和 =", sum_odds_1_to_99_for())
    print("3) sum(range): 2~100 偶数和 =", sum_evens_2_to_100_builtin())
    print("4) while: 1~100 求和 =", sum_1_to_100_while())
    print("5) while: 2~100 偶数和 =", sum_evens_2_to_100_while())
    print("6) 输出乘法表", sheet9x9())

    
def main():
    choice = input("要运行哪一段？输入 1~5 或 a(全部)：").strip().lower()
    if choice == "1":
        print(sum_1_to_100_for())
    elif choice == "2":
        print(sum_odds_1_to_99_for())
    elif choice == "3":
        print(sum_evens_2_to_100_builtin())
    elif choice == "4":
        print(sum_1_to_100_while())
    elif choice == "5":
        print(sum_evens_2_to_100_while())
    elif choice =="6":
        print(sheet9x9())
    elif choice in {"a", "all", ""}:
        run_all()
    else:
        print("输入无效：请输 1~6 或 a")


if __name__ == "__main__":
    main()
