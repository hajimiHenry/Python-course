time_second = int(input("请输入秒数"))
hour = time_second // 3600
hour_left = time_second % 3600
minute = hour_left // 60
second = hour_left % 60

print(f"{hour}小时{minute}分钟{second}秒")