a = [1, 2, 3, 2, 4, 5]

a.append(5)
print(a)

a.insert(2, 99)
print(a)

a.remove(2)  # remove是删除某个特定元素
print(a)

a.pop(2)
print(a)  # pop是删除某个特定下标

a.sort()
print(a)

a.reverse()
print(a)


print(a[0:3])