def selection_sort(src_arr):
    """外层控选index最为最小值，内层更新已选index，已选选与记录的最小相比，交换位置"""
    for i in range(len(src_arr) - 1):
        mark_min_index = i
        for j in range(i + 1, len(src_arr)):
            if src_arr[j] < src_arr[mark_min_index]:
                mark_min_index = j
        if mark_min_index != i:
            _temp = src_arr[mark_min_index]
            src_arr[mark_min_index] = src_arr[i]
            src_arr[i] = _temp
    print(src_arr)


def selection_sort_decending(src_arr):
    for i in range(len(src_arr) - 1):
        mark_max_index = i
        for j in range(i + 1, len(src_arr)):
            if src_arr[j] > src_arr[mark_max_index]:
                mark_max_index = j
        if mark_max_index != i:
            _temp = src_arr[mark_max_index]
            src_arr[mark_max_index] = src_arr[i]
            src_arr[i] = _temp
    print(src_arr)


if __name__ == '__main__':
    init_arr = [1, 5, 3, 3, 10, 9, 8, 11, 12]
    selection_sort(init_arr)
    selection_sort_decending(init_arr)