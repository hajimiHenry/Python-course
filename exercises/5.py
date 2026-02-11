while True:
    try:
        score = int(input("请输入成绩"))
    except ValueError:
        print("输入错误，请从新输入")
        continue

    if 0 <= score <= 100:
        break
    else:
        continue

match score // 10:
    case 10 | 9:
        level = "A"
    case 8:
        level = "B"
    case 7:
        level = "C"
    case 6:
        level = "D"
    case _:
        level = "E"

print(f"等级是{level}")
