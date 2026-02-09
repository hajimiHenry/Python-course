"""
index() 和 find() 到底在查什么？

它们都是在字符串里查找"子串"，然后告诉你：这个子串从第几个位置开始。
"""

# ============================================
# 第一步：理解"索引"是什么
# ============================================

s = "hello, world"

# 字符串的每个字符都有一个"位置编号"，叫做"索引"
# 索引从 0 开始数！

# h  e  l  l  o  ,     w  o  r  l  d
# 0  1  2  3  4  5  6  7  8  9  10 11

print("字符串是:", s)
print("长度是:", len(s))
print()

# 用索引取单个字符
print("s[0] =", s[0])  # h（第 0 个位置）
print("s[7] =", s[7])  # w（第 7 个位置）
print("s[8] =", s[8])  # o（第 8 个位置）
print()

# ============================================
# 第二步：index() 在查什么？
# ============================================

# index("子串") 的意思是：
# 这个"子串"在原字符串里，从第几个位置开始出现？

print("=" * 40)
print("index() 的作用：查找子串的起始位置")
print("=" * 40)

# 例子 1：查 "or"
# h  e  l  l  o  ,     w  o  r  l  d
# 0  1  2  3  4  5  6  7  8  9  10 11
#                         ↑  ↑
#                         o  r  ← "or" 从索引 8 开始

result = s.index("or")
print(f's.index("or") = {result}')
print('解释："or" 这两个字符，从第 8 个位置开始出现')
print()

# 例子 2：查 "world"
# h  e  l  l  o  ,     w  o  r  l  d
# 0  1  2  3  4  5  6  7  8  9  10 11
#                      ↑
#                      w  o  r  l  d  ← "world" 从索引 7 开始

result = s.index("world")
print(f's.index("world") = {result}')
print('解释："world" 这 5 个字符，从第 7 个位置开始出现')
print()

# 例子 3：查 "o"（有多个 o）
# h  e  l  l  o  ,     w  o  r  l  d
# 0  1  2  3  4  5  6  7  8  9  10 11
#             ↑           ↑
#             第一个 o     第二个 o

result = s.index("o")
print(f's.index("o") = {result}')
print('解释：有两个 "o"，index() 只返回【第一个】的位置')
print()

# ============================================
# 第三步：index() 和 find() 的区别
# ============================================

print("=" * 40)
print("index() 和 find() 的区别")
print("=" * 40)

# 当找得到时，两个都一样
print(f's.find("or")  = {s.find("or")}')  # 8
print(f's.index("or") = {s.index("or")}')  # 8
print("找得到时，两个结果一样")
print()

# 当找不到时，区别来了！
print("当找不到时：")
print(f's.find("xyz")  = {s.find("xyz")}')  # -1（表示没找到）

# 下面这行会报错！先注释掉
# print(f's.index("xyz") = {s.index("xyz")}')  # ❌ ValueError!

print('s.index("xyz") = ❌ 会报错 ValueError: substring not found')
print()

# ============================================
# 第四步：实际演示报错
# ============================================

print("=" * 40)
print("演示 index() 找不到时报错")
print("=" * 40)

try:
    result = s.index("xyz")
    print(f"找到了，位置是 {result}")
except ValueError as e:
    print(f"报错了！错误信息: {e}")

print()

# ============================================
# 总结
# ============================================

print("=" * 40)
print("总结")
print("=" * 40)
print(
    """
1. index() 和 find() 都是查找子串的【起始位置】
2. 索引从 0 开始数
3. 如果有多个相同的子串，只返回第一个的位置
4. 区别：
   - find()  找不到 → 返回 -1
   - index() 找不到 → 报错 ValueError

建议：初学时用 find()，这样程序不会突然崩溃
"""
)
