# 面向对象编程进阶

> **说明**：本文在保留原讲义所有知识点与代码的前提下，对语言表述和排版结构进行了优化，使其更易阅读和理解。

---

## 你将学到什么

- `private` / `protected` / `public` 三种访问可见性的含义
- 为什么 `stu.__name` 会报错，`stu._Student__name` 却能访问
- 什么是动态语言，`__slots__` 如何限制动态添加属性
- 对象方法、类方法、静态方法的区别
- `@property` 的作用：把方法包装成属性式访问
- 继承、重写与多态的含义

---

## 1. 访问可见性

### 1.1 什么是访问可见性？

在面向对象编程中，属性的"可见性"决定了谁可以访问它：

| 可见性 | 语法 | 含义 |
|--------|------|------|
| **公开** (public) | `self.name` | 任何地方都能访问 |
| **受保护** (protected) | `self._name` | 约定只在类内部和子类中使用 |
| **私有** (private) | `self.__name` | 只在类内部使用，外部访问会报错 |

### 1.2 私有属性的行为

```python
class Student:

    def __init__(self, name, age):
        self.__name = name   # 私有属性
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')   # 类内部可以访问


stu = Student('王大锤', 20)
stu.study('Python程序设计')   # ✅ 正常

print(stu.__name)   # ❌ AttributeError: 'Student' object has no attribute '__name'
```

**为什么报错？**

Python 对 `__name` 做了**名称改写（Name Mangling）**：
- 你写 `self.__name`，Python 实际存成了 `_Student__name`
- 类外部用 `stu.__name` 找不到这个名字，所以报错

```python
# 绕后门（了解即可，实际不要这么用）
print(stu._Student__name)   # ✅ 能访问，但你得知道规则才行
```

### 1.3 Python 为什么不强制私有？

> 名言：**"We are all consenting adults here"**（大家都是成年人）

Python 的哲学是**信任程序员**，不做最严格的限制：
- `_name`（单下划线）纯粹是约定，能访问但请自觉不要乱动
- `__name`（双下划线）通过改名增加了访问难度，但不是真正的锁
- 知道规则的人，`_Student__name` 这样还是能访问

**核心思想**：这些机制是在告诉你"请确认你知道自己在干什么"，而不是真的阻止你。

---

## 2. 动态属性

### 2.1 什么是动态语言？

**动态语言**：程序运行时可以改变对象的结构（添加/删除属性和方法）。

- 动态语言：Python、JavaScript、PHP、Ruby
- 静态语言：C、C++、Java（属性在编译时就固定了）

### 2.2 Python 可以随时给对象添加属性

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
stu.sex = '男'   # ✅ 随时动态添加新属性，完全没问题
```

> **提醒**：对象的方法本质上也是属性。如果调用了一个不存在的方法，报的异常也是 `AttributeError`。

### 2.3 用 `__slots__` 限制动态添加

如果你希望对象只允许有固定的属性，使用 `__slots__`：

```python
class Student:
    __slots__ = ('name', 'age')   # 只允许这两个属性

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
stu.sex = '男'   # ❌ AttributeError: 'Student' object has no attribute 'sex'
```

`__slots__` 相当于在动态语言里**主动给自己加上静态语言的约束**。

---

## 3. 静态方法和类方法

### 3.1 三种方法的区别

之前定义的方法都是**对象方法**（需要具体对象才能调用）。
类里还可以有另外两种方法，它们的消息接收者是**类本身**，而不是某个具体对象。

| 方法类型 | 装饰器 | 第一个参数 | 调用方式 |
|----------|--------|-----------|---------|
| 对象方法 | 无 | `self`（具体对象）| `对象.方法()` |
| 类方法 | `@classmethod` | `cls`（类本身）| `类名.方法()` |
| 静态方法 | `@staticmethod` | 无 | `类名.方法()` |

### 3.2 为什么需要静态方法？——以三角形为例

**问题**：创建三角形时，需要先验证三条边是否合法。但验证发生在**创建对象之前**，没有对象就没法调用对象方法。

**解决**：把验证方法设计为静态方法，让它属于"三角形这个概念"，而不是"某个具体的三角形"。

```python
class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """验证三条边是否能构成三角形（静态方法）"""
        return a + b > c and b + c > a and a + c > b

    # 类方法版本（效果相同，但多了 cls 参数）
    # @classmethod
    # def is_valid(cls, a, b, c):
    #     return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """计算周长（对象方法）"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积（对象方法）"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
```

使用时：

```python
# ① 先验证（对象还不存在，只能用静态方法）
if Triangle.is_valid(3, 4, 5):
    # ② 验证通过，才创建对象
    t = Triangle(3, 4, 5)
    # ③ 有对象了，才能调用对象方法
    print(t.perimeter())
    print(t.area())
```

> **静态方法 vs 类方法**：唯一区别是类方法的第一个参数是 `cls`（类本身），可以访问类属性；静态方法没有这个参数，完全独立。

### 3.3 `@property`：属性式访问

给方法加上 `@property` 装饰器后，调用时**不需要写括号**，像访问属性一样：

```python
class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    @property
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """计算面积"""
        p = self.perimeter / 2   # 注意：这里不用加括号
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


t = Triangle(3, 4, 5)
print(f'周长: {t.perimeter}')   # 不用加括号
print(f'面积: {t.area}')        # 不用加括号
```

**为什么用 `@property`？**
- 语义上"周长"是三角形的**特征**，不是一个"动作"，用属性访问更自然
- 每次访问时现算，始终反映最新的边长值

---

## 4. 继承和多态

### 4.1 为什么需要继承？

不用继承时，学生和老师会有大量重复代码（都有姓名、年龄、吃饭、睡觉）：

```
Student：name, age, eat(), sleep(), study()
Teacher：name, age, eat(), sleep(), teach()
           ↑ 重复！
```

**继承的做法**：把公共部分抽出来放进父类 `Person`，子类只写自己独有的部分。

### 4.2 继承代码示例

```python
class Person:
    """人（父类）"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭.')

    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student(Person):
    """学生（子类）"""

    def __init__(self, name, age):
        super().__init__(name, age)   # 调用父类的初始化方法

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):
    """老师（子类）"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title   # 老师独有的属性

    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')


stu1 = Student('白元芳', 21)
stu2 = Student('狄仁杰', 22)
tea1 = Teacher('武则天', 35, '副教授')

stu1.eat()                       # 从 Person 继承来的
stu2.sleep()                     # 从 Person 继承来的
tea1.eat()                       # 从 Person 继承来的
stu1.study('Python程序设计')
tea1.teach('Python程序设计')
stu2.study('数据科学导论')
```

### 4.3 继承的几个要点

**① 不指定父类时，默认继承 `object`**

```python
class Student:        # 等价于 class Student(object):
    pass
```

`object` 是 Python 所有类的顶级父类，所有类都直接或间接继承自它。

**② `super()` 用于调用父类**

```python
super().__init__(name, age)   # 调用父类的 __init__
```

**③ 子类比父类能力更多**

子类继承父类的一切，还能添加自己独有的属性和方法。

**④ 里氏替换原则**

实际开发中，常用**子类对象替换父类对象**——因为子类能做父类的所有事，甚至更多。

### 4.4 多态

子类可以**重写**父类的方法（用自己的版本覆盖父类的实现）。

不同子类对同一个方法有不同的实现 → 运行时表现出不同的行为 → 这就是**多态**：

> **调用相同的方法，不同的对象做不同的事情。**

```python
class Animal:
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):          # 重写父类方法
        print("汪汪汪！")

class Cat(Animal):
    def speak(self):          # 重写父类方法
        print("喵喵喵！")

# 同样调用 speak()，行为完全不同
Dog().speak()   # 汪汪汪！
Cat().speak()   # 喵喵喵！
```

多态是面向对象最精髓的部分，也是最需要练习才能灵活运用的部分。

---

## 5. 总结

| 概念 | 一句话总结 |
|------|-----------|
| **private `__`** | 名称被改写，类外访问报错，防止子类命名冲突 |
| **protected `_`** | 纯约定，告诉别人"这是内部实现，请自觉不乱动" |
| **动态属性** | Python 对象可随时添加属性，`__slots__` 可限制 |
| **对象方法** | 接收者是具体对象，有 `self` 参数 |
| **类方法** | 接收者是类本身，有 `cls` 参数，用 `@classmethod` |
| **静态方法** | 跟对象/类都无关，用 `@staticmethod`，逻辑上归属于类 |
| **`@property`** | 把方法变成不用写括号的属性式访问 |
| **继承** | 子类复用父类代码，`super()` 调用父类方法 |
| **多态** | 相同方法，不同子类有不同行为 |
