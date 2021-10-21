import random


def get_random_list(length: int=10, start: int=0, end: int=100) -> list:
    """获取随机数列表"""
    result = []
    for _ in range(length):
        result.append(random.choice(range(start, end)))
    return result


def my_sort(origin_list: list) -> list:
    """排序算法"""
    for i in range(len(origin_list)-1):
        min = i 
        for j in range(i, len(origin_list)):
            if origin_list[min] > origin_list[j]:
                min = j
        if min != i:
            origin_list[i], origin_list[min] = origin_list[min], origin_list[i]
    return origin_list


if __name__ == "__main__":
    for i in range(20):
        length = random.choice(range(0, 20))
        tmp = get_random_list(length)
        if my_sort(tmp) != sorted(tmp):
            print('排序失败', tmp)
            break
