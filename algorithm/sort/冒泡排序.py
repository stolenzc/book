import random


def get_random_list(length: int=10, start: int=0, end: int=100) -> list:
    """获取随机数列表"""
    result = []
    for _ in range(length):
        result.append(random.choice(range(start, end)))
    return result


def my_sort(origin_list: list) -> list:
    """排序算法"""
    for i in range(len(origin_list), 0, -1):
        for j in range(1, i):
            if origin_list[j] < origin_list[j-1]:
                origin_list[j-1], origin_list[j] = origin_list[j], origin_list[j-1]
    return origin_list


if __name__ == "__main__":
    for i in range(20):
        length = random.choice(range(0, 20))
        tmp = get_random_list(length)
        if my_sort(tmp) != sorted(tmp):
            print(my_sort(tmp))
            print('排序失败', tmp)
            break
    print('排序成功')
