import sys

_stdout_reconfigure = getattr(sys.stdout, "reconfigure", None)
if callable(_stdout_reconfigure):
    _stdout_reconfigure(encoding="utf-8")

_stderr_reconfigure = getattr(sys.stderr, "reconfigure", None)
if callable(_stderr_reconfigure):
    _stderr_reconfigure(encoding="utf-8")


def demo_1_list_create_and_print():
    a = list(range(1, 6))
    b = list("hello")
    print(a)
    print(*a)
    print(b)
    print(*b)
    print("".join(b))
    for x in a:
        print(x)


def demo_2_list_ops_and_membership():
    items_1 = [1, 2, 3]
    items_2 = [4, 5]
    items7 = ["Python", "Java", "JavaScript"]
    items_1 += items_2
    print(items_1)
    print(items_1 * 3)

    print(29 in items_1)
    print("Python" in items7)


def demo_3_list_comparisons():
    nums1 = [1, 2, 3, 4]
    nums2 = list(range(1, 5))
    nums3 = [3, 2, 1]
    print(nums1)
    print(nums2)
    print(nums3)
    print(f"nums1 == nums2 {nums1 == nums2}")  # True
    print(nums1 != nums2)  # False
    print(nums1 <= nums3)  # True
    print(nums2 >= nums3)  # False


def demo_4_iterate_with_index():
    languages = ["Python", "Java", "C++", "Kotlin"]
    for index in range(len(languages)):
        print(languages[index])


def throwing_shaizi_for_6000times():
    import random

    counters = [0] * 6
    for _ in range(6000):
        face = random.randrange(1, 7)
        counters[face - 1] += 1

    for face in range(1, 7):
        print(f'{face}点出现了{counters[face -1]}次')


def main():
    menu = {
        "1": ("列表创建/打印与遍历", demo_1_list_create_and_print),
        "2": ("列表拼接/重复与成员判断", demo_2_list_ops_and_membership),
        "3": ("列表比较运算示例", demo_3_list_comparisons),
        "4": ("用下标遍历列表", demo_4_iterate_with_index),
        "5": (
            "将一颗色子掷6000次，统计每种点数出现的次数",
            throwing_shaizi_for_6000times,
        ),
    }

    while True:
        print("\n==== day8 练习菜单 ====")
        for key, (title, _) in menu.items():
            print(f"{key}. {title}")
        print("0. 退出")

        choice = input("请选择要运行的编号：").strip()
        if choice in {"0", "q", "quit", "exit"}:
            return

        selected = menu.get(choice)
        if not selected:
            print("无效选择，请重新输入。")
            continue

        title, func = selected
        print(f"\n--- {choice}. {title} ---")
        try:
            func()
        except Exception as exc:
            print(f"运行出错：{exc!r}")


if __name__ == "__main__":
    main()
