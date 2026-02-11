while True:
    try:
        a = int(input("请输入第一个数"))
        b = int(input("请输入第二个数"))
        break
    except ValueError:
        print("请输入正确的数字")

while True:
    mark = input("请输入符号")
    if mark in ["+", "-", "*", "/"]:
        break
    else:
        continue

if mark == "/" and b == 0 :
    print('除数不能为0')
elif mark == "/" :
    answer = a / b
elif mark == "+":
    answer = a + b
elif mark == "*":
    answer = a * b
elif mark == "-":
    answer = a - b

print(f"答案是{answer:.2f}")
