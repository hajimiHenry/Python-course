sentence = input("请输入句子")
words = sentence.split()
print(words)

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)

counted = sorted(count.items(), key=lambda x: x[1], reverse=True)
print(counted)

for word ,freq in counted:
    print(f"{word}:{freq}")