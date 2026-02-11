year = int(input("请输入年份"))
if year % 400 == 0:
    is_runnian = True
elif year % 4 == 0 and year % 100 != 0:
    is_runnian = True
else:
    is_runnian = False

status = "是闰年" if is_runnian else "不是闰年"
print(f"{year}{status}")
