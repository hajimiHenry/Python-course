s = "hello,## world"
print(s.find("or"))  # 8
print(s.find("xx"))  # -1

s.split("#")  # ['a', '', 'b']
print(s)


k = "  hello,PYthon "
print(k.strip())
print(k)
k_2 = k.lower()
print(k_2)
print("PYthon" in k)
print(k.replace("PYthon", "world"))
parts = k.split(",")
print(parts)

join_parts= "_".join(parts)
print(join_parts)