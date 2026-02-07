a = ()
print(type(a))
print(a)  # <class 'tuple'>
b = "hello"
print(type(b))  # <class 'str'>
c = 100
print(type(c))  # <class 'int'>
d = ("hello",)
print(type(d))  # <class 'tuple'>
e = (100,)
print(type(e))  # <class 'tuple'>

# 打包操作
h = 1, 10, 100
i, j, k = h
print(type(h))  # <class 'tuple'>
print(h)  # (1, 10, 100)
print(i, j, k)

import timeit

print("%.3f 秒" % timeit.timeit("[1, 2, 3, 4, 5, 6, 7, 8, 9]", number=10000000))
print("%.3f 秒" % timeit.timeit("(1, 2, 3, 4, 5, 6, 7, 8, 9)", number=10000000))

infos = ("骆昊", 43, True, "四川成都")  # 将元组转换成列表
infos_list = list(infos)
print(infos_list)  # ['骆昊', 43, True, '四川成都']

frts = ["apple", "banana", "orange"]
# 将列表转换成元组
print(tuple(frts))  # ('apple', 'banana', 'orange')


