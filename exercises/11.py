while True:
    try:
        x = int(input("请输入数字"))
    except ValueError:
        print("输入有错")

    if x >= 100:
        break
    else:
        print("必须是三位数及以上")
        continue

x_0 = x
total = 0
while True:
    temp = x % 10
    total += temp**3
    x //= 10
    if x == 0:
        break

if total == x_0:
    print("是水仙花数")
else:
    print("不是水仙花数")
