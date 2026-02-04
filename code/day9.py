def study_list():
    languages = ["Python", "Java", "C++"]
    languages.append("JavaScript")
    print(languages)  
    languages.insert(1, "SQL")
    print(languages)  
    if "Java" in languages:
        languages.remove("Java")
        print(languages)  
    if "Swift" not in languages:
        languages.append("Swift")
        print(languages)  

    languages.pop()
    print(languages)
    temp = languages.pop(1)
    print(languages)
    print(temp)
    languages.append(temp)
    print(languages)

    languages.clear()
    print(languages)


# 双色球问题
def double_color_ball():
    import random
    from rich import console
    from rich import table
    
    console = Console
    table = Table( show_header =True)
    table.add_column("序号",justify ="center")
    table.add_column("红球",justify ="center")
    table.add_column("蓝球",justify ="center")
    
    
    x= int(input('请输入想赌的次数'))
    for _ in range(x):
        red_balls=list(range(1,34))
        selected_balls= []
        
        for _ in range(6):
            index = random.randrange(len(red_balls))
            selected_balls.append(red_balls.pop(index))
            
        selected_balls.sort()
        
        for ball in selected_balls :
            print(f'\033[031m{ball:0>2d}\033[0m', end=' ')

        blue_ball= random.randrange(1,17)
        print(f'\033[034m{blue_ball:0>2d}\033[0m')


def run():
    while True:
        print("\n==== day9 菜单 ====")
        print("1. 列表练习 study_list")
        print("2. 双色球问题")
        print("0. 退出")

        try:
            n = int(input("选择运行程序"))
        except ValueError:
            print("请输入数字")
            continue

        match n:
            case 1:
                study_list()
            case 2:
                double_color_ball()
            case 0:
                break


if __name__ == "__main__":
    run()
