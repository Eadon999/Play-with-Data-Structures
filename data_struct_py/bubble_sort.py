def bubble_sort_ascending(src_arr):
    """两两相邻比较，由小到大小的往前放（冒泡），尾部为确定内层循环减去以放好的尾部index"""
    if len(src_arr) <= 1:
        return src_arr
    is_swap = False
    for i in range(len(src_arr) - 1):
        print(src_arr)
        for j in range(0, len(src_arr) - 1 - i):
            if src_arr[j] > src_arr[j + 1]:
                _temp = src_arr[j]
                src_arr[j] = src_arr[j + 1]
                src_arr[j + 1] = _temp
                is_swap = True
        if not is_swap:
            break
    return src_arr


def bubble_sort_deceding(src_arr):
    if len(src_arr) <= 1:
        return src_arr
    is_swap = False
    for i in range(len(src_arr) - 1):
        print(src_arr)
        for j in range(0, len(src_arr) - 1 - i):
            if src_arr[j] < src_arr[j + 1]:
                _temp = src_arr[j]
                src_arr[j] = src_arr[j + 1]
                src_arr[j + 1] = _temp
                is_swap = True
        if not is_swap:
            break
    return src_arr


if __name__ == '__main__':
    import random

    init_arr = list(range(13))
    random.shuffle(init_arr)
    source_arr = [3, 12, 7, 4, 10, 0, 2, 9, 1, 5, 6, 8, 11]
    source_arr = list(range(13))
    res = bubble_sort_ascending(source_arr)
    print(res)

    source_arr = [3, 12, 7, 4, 10, 0, 2, 9, 1, 5, 6, 8, 11]
    res = bubble_sort_deceding(source_arr)
    print(res)
