a = [x**2 for x in range(1, 21) if x % 2 == 0]
print(a)

word = ["hello", "world", "python"]
b = [s.upper() for s in word]
print(b)

num = [-3, 5, -1, 7, 0, -8, 12]
c = [x for x in num  if x>0]
print (c)
