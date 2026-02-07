s = "hello,## world"
print(s.find("or"))   # 8
print(s.find("xx"))   # -1

s.split("#")   # ['a', '', 'b']
print(s)


print(s.index("xx"))  # ValueError


k = "  hello,python  "
