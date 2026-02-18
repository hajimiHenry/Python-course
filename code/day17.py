def count_calls(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1

        result = func(*args, **kwargs)

        print(f"函数{func.__name__}已被调用{count}次")

        return result

    return wrapper


@count_calls
def say_hello():
    print("hello!")


# say_hello()
# say_hello()
# say_hello()
# say_hello()


