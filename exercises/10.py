n = int(input("请输入项数"))
x = 0
y = 1
print("1")
for i in range(1, n):
    z = x + y
    print(z)
    x = y
    y = z
