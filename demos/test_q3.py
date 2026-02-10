# ========== 题目3：数据过滤 ==========
print("--- 题目3：数据过滤 ---\n")

# 1. 创建集合：1-50之间能被3或5整除的数字
set_3_or_5 = {num for num in range(1, 51) if num % 3 == 0 or num % 5 == 0}
print(f"1. 能被3或5整除的数：")
print(f"   {sorted(set_3_or_5)}")
print(f"   共 {len(set_3_or_5)} 个数\n")

# 2. 创建集合：1-50之间能被7整除的数字
set_7 = {num for num in range(1, 51) if num % 7 == 0}
print(f"2. 能被7整除的数：")
print(f"   {sorted(set_7)}")
print(f"   共 {len(set_7)} 个数\n")

# 3. 交集：既能被(3或5)整除，又能被7整除的数
intersection = set_3_or_5 & set_7
print(f"3. 交集（同时满足两个条件）：")
print(f"   {sorted(intersection)}")
print(f"   解释：这些数既能被(3或5)整除，又能被7整除\n")

# 4. 对称差：只满足一个条件，不同时满足两个条件的数
symmetric_diff = set_3_or_5 ^ set_7
print(f"4. 对称差（只满足一个条件）：")
print(f"   {sorted(symmetric_diff)}")
print(f"   解释：这些数只满足一个条件，不同时满足两个条件")
print(f"   共 {len(symmetric_diff)} 个数")
