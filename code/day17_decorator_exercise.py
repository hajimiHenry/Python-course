"""
函数装饰器练习题
请按照顺序依次完成以下练习题
"""

# ======== 练习题 1：计数器装饰器 ========
# 难度：⭐⭐
# 要求：
# 创建一个名为 count_calls 的装饰器，统计被装饰函数被调用的次数。
# 每次调用函数时，打印"函数 [函数名] 已被调用 [次数] 次"

# 提示：
# 1. 装饰器内部可以使用变量来保存调用次数
# 2. 可以使用 func.__name__ 获取函数名称
# 3. 注意可变参数的使用


# TODO: 在这里实现 count_calls 装饰器
def count_calls(func):
    pass  # 删除这行，实现你的代码


# 测试代码（请不要修改）
@count_calls
def say_hello():
    print("Hello!")


# 取消下面的注释来测试
# say_hello()  # 输出: Hello! \n 函数 say_hello 已被调用 1 次
# say_hello()  # 输出: Hello! \n 函数 say_hello 已被调用 2 次
# say_hello()  # 输出: Hello! \n 函数 say_hello 已被调用 3 次


# ======== 练习题 2：参数验证装饰器 ========
# 难度：⭐⭐⭐
# 要求：
# 创建一个名为 validate_positive 的装饰器，确保被装饰函数的所有参数都是正数。
# 如果发现负数或零，打印错误信息："错误：参数必须是正数！" 并返回 None
# 如果所有参数都是正数，正常执行函数

# 提示：
# 1. 使用 *args 接收所有位置参数
# 2. 使用 all() 函数检查所有参数
# 3. 注意要返回原函数的结果


# TODO: 在这里实现 validate_positive 装饰器
def validate_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <= 0:
                print("错误：参数必须是正数")
                return None

        result = func(*args, **kwargs)
        return result

    return wrapper


# 测试代码（请不要修改）
@validate_positive
def multiply(a, b):
    return a * b


# 取消下面的注释来测试
# print(multiply(3, 5))    # 输出: 15
# print(multiply(-2, 5))   # 输出: 错误：参数必须是正数！\n None
# print(multiply(0, 5))    # 输出: 错误：参数必须是正数！\n None


# ======== 练习题 3：日志装饰器 ========
# 难度：⭐⭐⭐
# 要求：
# 创建一个名为 log_function 的装饰器，记录函数调用的详细信息：
# - 在函数执行前打印："开始执行 [函数名]，参数：args=[位置参数], kwargs=[关键字参数]"
# - 在函数执行后打印："[函数名] 执行完毕，返回值：[返回值]"

# 提示：
# 1. 需要同时处理位置参数和关键字参数
# 2. 打印参数时可以直接使用 args 和 kwargs
# 3. 记得保存并返回函数的返回值


# TODO: 在这里实现 log_function 装饰器
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"开始执行[{func.__name__}],参数args={args},kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[{func.__name__}]执行完毕，返回值[{result}]")
        return result

    return wrapper


# 测试代码（请不要修改）
@log_function
def add(a, b, message="计算中"):
    print(f"{message}: {a} + {b}")
    return a + b


# 取消下面的注释来测试
# result = add(3, 5, message="正在计算")
# 预期输出：
# 开始执行 add，参数：args=(3, 5), kwargs={'message': '正在计算'}
# 正在计算: 3 + 5
# add 执行完毕，返回值：8


# ======== 练习题 4：带参数的装饰器（挑战题）========
# 难度：⭐⭐⭐⭐
# 要求：
# 创建一个名为 repeat 的装饰器，它接受一个参数 times，表示函数要重复执行的次数。
# 每次执行前打印："第 [次数] 次执行"

# 提示：
# 1. 带参数的装饰器需要三层嵌套函数
# 2. 最外层函数接收装饰器参数（times）
# 3. 中间层函数接收被装饰的函数（func）
# 4. 最内层函数接收函数的参数，并实际执行


# TODO: 在这里实现 repeat 装饰器
def repeat(times):
    def decorater(func):
        def wrapper(*args ,**kwargs ):
            for i in range(times):
                print(f"第{i+1}次执行")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorater

        


# 测试代码（请不要修改）
@repeat(times=3)
def greet(name):
    print(f"你好，{name}！")


# 取消下面的注释来测试
# greet("小明")
# 预期输出：
# 第 1 次执行
# 你好，小明！
# 第 2 次执行
# 你好，小明！
# 第 3 次执行
# 你好，小明！


# ======== 练习题 5：综合实战 ========
# 难度：⭐⭐⭐⭐⭐
# 要求：
# 创建一个名为 retry 的装饰器，当函数执行失败（抛出异常）时，自动重试。
# 装饰器接受两个参数：
# - max_attempts: 最大尝试次数（默认3次）
# - delay: 每次重试之间的延迟秒数（默认1秒）
# 如果所有尝试都失败，打印错误信息并重新抛出最后一次的异常

# 提示：
# 1. 使用 try-except 捕获异常
# 2. 使用 time.sleep() 实现延迟
# 3. 使用循环实现多次重试
# 4. 可以参考教材中的 @wraps(func) 来保留原函数信息
# 5. 需要使用三层嵌套（因为装饰器带参数）

# TODO: 在这里实现 retry 装饰器
import time
from functools import wraps


def retry(max_attempts=3, delay=1):
    def decorater(func):
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try :
                    result = func (*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"失败了：{e}")
                    time.sleep(delay)
                    if i == max_attempts - 1 :
                        print(f"最后一次（第{i+1}次）调用也失败了")
                        raise 
        return wrapper
    return decorater

        


# 测试代码（请不要修改）
# 这个函数会模拟一个不稳定的网络请求，前两次会失败
attempt_counter = 0


@retry(max_attempts=3, delay=0.5)
def unstable_network_request():
    global attempt_counter
    attempt_counter += 1
    if attempt_counter < 3:
        print(f"模拟网络错误（尝试 {attempt_counter}）")
        raise ConnectionError("网络连接失败")
    print("连接成功！")
    return "数据获取成功"


# 取消下面的注释来测试
try:
    result = unstable_network_request()
    print(f"最终结果：{result}")
except Exception as e:
    print(f"所有重试失败：{e}")
finally:
    attempt_counter = 0  # 重置计数器


print("\n" + "=" * 50)                          
print("提示：完成练习后，取消相应测试代码的注释来验证你的实现！")
print("建议按顺序完成，从简单到困难逐步提升！")
print("=" * 50)
