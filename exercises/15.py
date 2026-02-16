import random

score = [[random.randint(60, 100) for _ in range(3)] for _ in range(5)]
print(score)

total = []

for i in range(len(score)):
    total_0 = 0
    for j in range(len(score[i])):
        total_0 += score[i][j]
    total.append(total_0)

print(total)

average = []

for k in range(len(total)):
    average.append(round(total[k] / 3, 1))
print(average)

best = max(total)
best_index = total.index(best)
print(best_index)
