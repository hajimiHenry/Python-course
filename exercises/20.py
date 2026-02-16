string = input("请输入文本")
string = string.lower()
string = string.replace(' ','')

n = len(string)//2
first_half = string[:n]
second_half= string[-n:][::-1]

print(first_half == second_half)
