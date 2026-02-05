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


# 双色球随机选号（Rich 表格版）
def double_color_ball():
    """
    生成 n 注双色球号码，并用 rich 输出“好看的表格”。

    规则（简化版）：
    - 红球：从 1~33 中选 6 个不重复数字
    - 蓝球：从 1~16 中选 1 个数字

    小提示：如果运行时报错 ModuleNotFoundError: rich，先安装：pip install rich
    """
    import random
    from rich.console import Console
    from rich.table import Table
    from rich import box

    # Console：可以理解成“高级打印机”，负责把表格/颜色等渲染到终端
    console = Console()

    # Table：可以理解成“终端里的 Excel 表格”，先定义列（表头），再一行行 add_row 填数据
    table = Table(
        title="双色球随机选号",
        show_header=True,
        header_style="bold",
        box=box.SQUARE,
        show_lines=False,
    )
    table.add_column("序号", justify="center", width=6)
    table.add_column("红球", justify="center")
    table.add_column("蓝球", justify="center", width=6)

    x = int(input("生成几注号码: "))
    for i in range(x):
        # 红球池：1~33。每抽一次就从池子里拿走（pop），保证不会重复。
        red_balls = list(range(1, 34))
        selected_balls = []

        for _ in range(6):
            index = random.randrange(len(red_balls))
            selected_balls.append(red_balls.pop(index))

        # 排序后展示更像真实彩票号码
        selected_balls.sort()

        # 把红球/蓝球格式化成两位数，并用 rich 的 markup 语法上色
        # join 的写法：
        # 1) 先把每个红球号码都转成“字符串”（join 只能拼字符串）
        # 2) 再用空格 " " 把它们连接起来
        red_ball_text_list = []
        for ball in selected_balls:
            red_ball_text_list.append("%02d" % ball)
        red_text = "[red]" + " ".join(red_ball_text_list) + "[/red]"
        blue_ball = random.randrange(1, 17)
        blue_text = "[blue]%02d[/blue]" % blue_ball

        # 把这一注号码作为一行添加到表格里
        table.add_row(str(i + 1), red_text, blue_text)

    # 最后统一打印表格（不在循环里 print，这样排版才整齐）
    console.print(table)


def run():
    while True:
        print("\n==== day9 菜单 ====")
        print("1. 列表练习 study_list")
        print("2. 双色球随机选号（Rich 表格）")
        print("0. 退出")

        try:
            n = int(input("请选择菜单项: "))
        except ValueError:
            print("请输入数字。")
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
