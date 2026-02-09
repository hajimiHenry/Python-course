set1 = {1, 2, 3, 3, 3, 2}
print(set1)

set2 = {"banana", "pitaya", "apple", "apple", "banana", "grape"}
print(set2)

set3 = set("hello")
print(set3)

set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
print(set4)

set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set5)

# ========== 题目1：基础创建和去重 ==========
students = ["张三", "李四", "王五", "张三", "赵六", "李四", "孙七"]
print("原始列表:", students)

# 使用 set() 函数将列表转换为集合（自动去重）
unique_students = set(students)
print("转换后的集合:", unique_students)

# 打印去重后的学生数量
print(f"去重后共有 {len(unique_students)} 名学生")

# 如果需要以列表形式输出，可以再转回列表
print(f"学生名单：{list(unique_students)}")


# ========== 题目2：选课系统 ==========
python_class = {"张三", "李四", "王五", "赵六"}
java_class = {"李四", "王五", "孙七", "周八"}
cpp_class = {"王五", "赵六", "周八", "吴九"}

print("\n--- 题目2：选课系统 ---")

# 1. 同时选修了 Python 和 Java 的学生（交集）
# 思路：两个班都有的学生
both_py_java = python_class & java_class
print(f"1. 同时选修 Python 和 Java 的学生：{both_py_java}")

# 2. 至少选修了一门课的所有学生（并集）
# 思路：把三个班的学生全部合并（自动去重）
all_students = python_class | java_class | cpp_class
print(f"2. 至少选修了一门课的学生：{all_students}")
print(f"   共有 {len(all_students)} 名学生选课")

# 3. 只选修了 Python，没选修 Java 的学生（差集）
# 思路：在 Python 班但不在 Java 班
only_python = python_class - java_class
print(f"3. 只选修 Python，没选修 Java：{only_python}")

# 4. 选修了 Python 或 Java，但没选修 C++ 的学生
# 思路：先把 Python 和 Java 合并，再排除 C++ 的学生
py_or_java = python_class | java_class  # 先求并集
not_cpp = py_or_java - cpp_class  # 再求差集
print(f"4. 选修 Python 或 Java，但没选修 C++：{not_cpp}")

# ========== 题目3：数据过滤 ==========
print("\n--- 题目3：数据过滤 ---")

# 1. 创建集合：1-50之间能被3或5整除的数字
#    注意：% 后面必须有数字！num % 5 表示 num 除以 5 的余数
set_3_or_5 = {num for num in range(1, 51) if num % 3 == 0 or num % 5 == 0}
print(f"1. 能被3或5整除的数：{sorted(set_3_or_5)}")

# 2. 创建集合：1-50之间能被7整除的数字
#    注意：生成式条件前必须加 if 关键字！
set_7 = {num for num in range(1, 51) if num % 7 == 0}
print(f"2. 能被7整除的数：{sorted(set_7)}")

# 3. 交集：既能被(3或5)整除，又能被7整除的数
intersection = set_3_or_5 & set_7
print(f"3. 交集（同时满足两个条件）：{sorted(intersection)}")

# 4. 对称差：只满足一个条件，不同时满足两个条件的数
symmetric_diff = set_3_or_5 ^ set_7
print(f"4. 对称差（只满足一个条件）：{sorted(symmetric_diff)}")
