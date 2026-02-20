# 1. 定义父类 Animal
class Animal:
    def run(self):
        print("动物在跑...")

# 2. 定义子类 Dog，继承自 Animal，并重写 run 方法
class Dog(Animal):
    def run(self):
        print("🐶 狗狗正在四条腿撒欢儿地跑！")

# 3. 定义子类 Cat，继承自 Animal，并重写 run 方法
class Cat(Animal):
    def run(self):
        print("🐱 猫咪正在迈着优雅的猫步跑！")

# 4. 定义一个新的子类 RoboDog，同样继承自 Animal
class RoboDog(Animal):
    def run(self):
        print("🤖 机器狗正伴随着滴滴的电子音在跑！")

# 5. 这就是体现“多态”的函数
def run_twice(animal):
    print(">>> 接收到指令：开始跑两次！")
    animal.run()
    animal.run()
    print(">>> 指令执行完毕。\n")

# ==========================================
# 下面是测试代码（主程序）
# ==========================================

# 创建不同的对象（生活中的实体）
my_dog = Dog()
my_cat = Cat()
my_robo_dog = RoboDog()

# 把它们塞进同一个函数里，看看会发生什么
run_twice(my_dog)
run_twice(my_cat)
run_twice(my_robo_dog)