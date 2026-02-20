# 面向对象编程应用

> **说明**：本文在保留原讲义所有知识点与代码的前提下，对语言表述和排版结构进行了优化，使其更易阅读和理解。

---

## 前言

面向对象编程对初学者来说**不难理解，但很难应用**。

学会三步走（定义类 → 创建对象 → 给对象发消息）只是开始，真正掌握它需要：
- **大量的编程练习**
- **阅读优质的代码**

下面通过两个经典案例，把面向对象编程的知识串联起来。

---

## 例子 1：扑克游戏

> **需求**：52 张牌（无大小王），发给 4 名玩家，每人 13 张，按花色和点数排序。

### 第一步：找出对象和类

从需求描述里提取**名词**（→ 对象/属性）和**动词**（→ 行为）：

| 类 | 属性 | 行为 |
|----|------|------|
| `Card`（牌） | 花色、点数 | 显示自身 |
| `Poker`（扑克） | 一副牌、当前发牌位置 | 洗牌、发牌 |
| `Player`（玩家） | 名字、手上的牌 | 摸牌、整理手牌 |

类之间的关系：
- **Poker has-a Card**：一副扑克有 52 张牌
- **Player has-a Card**：玩家手上有牌
- **Player use-a Card**：玩家使用了牌

---

### 第二步：定义花色枚举

直接用数字 0~3 表示花色可读性太差，改用**枚举**来定义有意义的名称。

> Python 没有 `enum` 关键字，但可以继承 `enum` 模块的 `Enum` 类来实现。

```python
from enum import Enum

class Suite(Enum):
    """花色（枚举）"""
    SPADE, HEART, CLUB, DIAMOND = range(4)
    # 黑桃=0  红心=1  草花=2  方块=3
```

枚举类型可以直接放进 `for` 循环遍历：

```python
for suite in Suite:
    print(f'{suite}: {suite.value}')
# Suite.SPADE: 0
# Suite.HEART: 1
# Suite.CLUB: 2
# Suite.DIAMOND: 3
```

使用 `Suite.SPADE` 比数字 `0` 可读性高得多。

---

### 第三步：定义牌类 `Card`

```python
class Card:
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite   # 花色（Suite 枚举）
        self.face = face     # 点数（1~13）

    def __repr__(self):
        """控制对象打印时显示的内容"""
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'
```

测试：

```python
card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1)  # ♠5
print(card2)  # ♥K
```

---

### 第四步：定义扑克类 `Poker`

```python
import random

class Poker:
    """扑克"""

    def __init__(self):
        # 列表推导式生成 52 张牌
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]
        self.current = 0   # 当前发牌的位置

    def shuffle(self):
        """洗牌"""
        self.current = 0
        random.shuffle(self.cards)   # 随机打乱顺序

    def deal(self):
        """发一张牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发（属性式访问，无需括号）"""
        return self.current < len(self.cards)
```

测试：

```python
poker = Poker()
print(poker.cards)   # 洗牌前（有序）
poker.shuffle()
print(poker.cards)   # 洗牌后（随机）
```

---

### 第五步：定义玩家类 `Player`

```python
class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []   # 手上的牌

    def get_one(self, card):
        """摸一张牌"""
        self.cards.append(card)

    def arrange(self):
        """整理手牌（排序）"""
        self.cards.sort()
```

---

### 第六步：发牌并运行

```python
poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]

# 轮流发牌，每人 13 张
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())

# 整理手牌并输出
for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)
```

---

### 遇到的问题：`Card` 对象无法比较大小

运行上面的代码，`player.arrange()` 会报错：

```
TypeError: '<' not supported between instances of 'Card' and 'Card'
```

**原因**：`sort()` 需要比较两个 `Card` 对象的大小，但 Python 不知道怎么比较。

**解决方案**：在 `Card` 类里添加 `__lt__` 魔术方法（`lt` = less than，即 `<`）。

> 这种技术叫**运算符重载**，让 Python 知道如何对自定义对象使用运算符。

```python
class Card:
    """牌（完整版）"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __lt__(self, other):
        """定义 < 运算符的行为"""
        if self.suite == other.suite:
            return self.face < other.face      # 同花色：比点数
        return self.suite.value < other.suite.value   # 不同花色：比花色值
```

常用魔术方法对应关系：

| 魔术方法 | 对应运算符 |
|----------|-----------|
| `__lt__` | `<` |
| `__gt__` | `>` |
| `__le__` | `<=` |
| `__ge__` | `>=` |
| `__eq__` | `==` |
| `__ne__` | `!=` |

---

## 例子 2：工资结算系统

> **需求**：三类员工，计算月薪：
> - 部门经理：固定 15000 元
> - 程序员：200 元/小时 × 工作时长
> - 销售员：1800 元底薪 + 销售额 × 5%

---

### 第一步：设计父类 `Employee`（抽象类）

三类员工都是"员工"，共享员工的公共属性（如姓名），所以先定义一个父类。

但"结算月薪"这件事，父类不知道具体怎么算——这时候用**抽象方法**：只声明，不实现，强制子类去重写。

> Python 通过 `abc` 模块实现抽象类，不用纠结原理，照写即可。

```python
from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    """员工（抽象类，不能直接创建对象）"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪（抽象方法，子类必须实现）"""
        pass
```

**抽象方法** = 只有声明，没有实现，目的是强制所有子类都必须重写它。

---

### 第二步：派生三个子类

```python
class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0   # 固定月薪


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour   # 本月工作小时数

    def get_salary(self):
        return 200 * self.working_hour   # 200元/小时


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales   # 本月销售额

    def get_salary(self):
        return 1800 + self.sales * 0.05   # 底薪 + 提成
```

三个子类都重写了 `get_salary`，内容各不相同——这就是**多态**：
> **调用相同的方法，不同的对象做不同的事情。**

---

### 第三步：运行结算系统

这里用到了 `isinstance()` 函数，用来判断一个对象属于哪个类：

```python
emps = [
    Manager('刘备'),
    Programmer('诸葛亮'),
    Manager('曹操'),
    Programmer('荀彧'),
    Salesman('张辽')
]

for emp in emps:
    if isinstance(emp, Programmer):
        emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
    print(f'{emp.name}本月工资为: ￥{emp.get_salary():.2f}元')
```

> **`isinstance` vs `type`**：
> - `type(obj)` 精准匹配，只判断是否是这个类
> - `isinstance(obj, 类)` 模糊匹配，判断是否是这个类或它的子类（更常用）

---

## 总结

| 概念 | 含义 |
|------|------|
| **枚举** | 用有意义的名称代替数字常量，提升可读性 |
| **魔术方法** | 让自定义对象支持运算符（如 `<`、`==`）|
| **抽象类** | 定义"模板"，强制子类实现特定方法 |
| **抽象方法** | 只声明不实现，子类必须重写 |
| **多态** | 调用相同方法，不同子类有不同行为 |
| **isinstance** | 判断对象是否属于某个类（含子类）|

> 面向对象的抽象、封装、继承、多态，不是一下子就能灵活运用的——这需要长时间的练习积累，每多写一个案例，理解就深一分。
