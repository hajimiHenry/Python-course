import datetime

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
import time

start = time.perf_counter()

for i in range(1000000):
    x = i * 2

end = time.perf_counter()

print(end - start)

n = 0
for i in range(50):
    print(f"\r =*n",end="")
    n += 1
