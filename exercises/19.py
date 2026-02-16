s = input("请输入文本")

upper_count = 0
lower_count = 0
digit_count = 0
others_count = 0

for char in s:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        others_count += 1

print(upper_count, end=" ")
print(lower_count, end=" ")
print(digit_count, end=" ")
print(others_count, end=" ")
