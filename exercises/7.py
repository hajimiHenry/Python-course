
n = int (input ('请输入循环次数'))
total = 0
for i in range(1,n+1):
    total += i
print (f"和是{total}")


j = 1
total_2 =0
while True :
    total_2 += j
    j+= 1
    if j == n:
        break

print(f"和是{total_2}")
